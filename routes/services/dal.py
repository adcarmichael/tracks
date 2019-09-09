from routes.models import RouteSet, Route, RouteRecord, Profile, Gym
from enum import Enum
import routes.services.conf as conf
from datetime import datetime
from django.db.models import DateField
from django.db.models.functions import Cast, Coalesce
# if __name__ == "__main__":
#     import django
#     import os

#     os.environ['DJANGO_SETTINGS_MODULE'] = 'tracks.settings'
#     django.setup()


def get_dal(gym_key=conf.GymKey.eden_rock_edinburgh):
    if gym_key == conf.GymKey.eden_rock_edinburgh:
        _dal = _DalEdenRocks(_EdenDataMap)
    else:
        _dal = _DalEdenRocks(_EdenDataMap)
    return _dal


class _DataMap():
    @staticmethod
    def grade(grade):
        pass

    @staticmethod
    def grade_sub(grade_sub):
        pass


class _EdenDataMap(_DataMap):

    @staticmethod
    def grade(grade):
        g = conf.Grade
        return g.get_value_from_name(grade)

    @staticmethod
    def grade_sub(grade_sub):
        g = conf.GradeSub
        return g.get_value_from_name(grade_sub)


class _DalBase:
    def __init__(self, DataMap):
        self.DataMap = DataMap()

    def _get_all_routes(self, gym_id=[]):
        query = Route.objects.all().order_by('-route_set__up_date')
        query = self._filter_route_query_by_gym(query, gym_id)
        return query

    def get_routes_all(self):
        query = self._get_all_routes()
        data = _Data(query)
        return data

    def _filter_route_query_by_gym(self, query, gym_id):
        if query:
            if gym_id:
                query = query.filter(route_set__gym__id=gym_id)
        return query

    def _filter_route_set_query_by_gym(self, query, gym_id):
        if query:
            if gym_id:
                query = query.filter(gym__id=gym_id)
        return query

    def _filter_route_record_query_by_gym(self, query, gym_id):
        if gym_id:
            query = query.filter(route__route_set__gym__id=gym_id)
        return query

    def _filter_query_to_active_based_on_up_date(self, query):
        for index in range(0, query.count()):
            date_search = query[index].route_set.up_date
            if date_search < datetime.now().date():
                id = query[index].route_set.id
                query = query.filter(route_set__id=id)
                return query
        return query

    def get_route_record_for_user(self, user_id, route_id, gym_id=[]):
        if not isinstance(route_id, (list,)):
            route_id = [route_id]

        query = self._get_route_record_for_user(user_id, route_id, gym_id)
        status = [record.status for record in query]
        is_climbed = [record.is_climbed for record in query]
        date_climbed = [record.date for record in query]
        route_id_returned = [a.route.id for a in query]

        is_climbed_list = [False] * len(route_id)
        status_list = [0] * len(route_id)
        date_climbed_list = [0] * len(route_id)

        # Ensure that the returned is_climbed and status are in sync with input route ids
        for num, i_route_id in enumerate(route_id_returned):
            index = route_id.index(i_route_id)
            is_climbed_list[index] = is_climbed[num]
            status_list[index] = status[num]
            date_climbed_list[index] = date_climbed[num]

        if not status_list:
            status_list = [0]
        if not is_climbed_list:
            is_climbed_list = [False]
        if not is_climbed_list:
            date_climbed_list = []

        record = {'status': status_list, 'is_climbed':
                  is_climbed_list, 'date': date_climbed_list}

        return record

    def set_route_record_for_user(self, user_id, route_id, status, is_climbed):
        query = self._get_route_record_for_user(user_id, route_id)
        if query:
            self._update_route_record(
                query[0].id, status=status, is_climbed=is_climbed)
        else:
            self._create_route_record(
                user_id, route_id, status=status, is_climbed=is_climbed)

    def _get_route_record_for_user(self, user_id, route_id, gym_id=[]):
        if not isinstance(route_id, (list,)):
            route_id = [route_id]

        query = RouteRecord.objects.filter(
            user__id=user_id).filter(route__id__in=route_id)
        query = self._filter_route_record_query_by_gym(query, gym_id)
        return query

    def _create_route_record(self, user_id, route_id, is_climbed=False, status=0):
        profile = Profile.objects.all().filter(user__id=user_id)
        route = Route.objects.all().filter(id=route_id)
        if profile and route:
            RouteRecord.objects.create(
                user=profile[0], route=route[0], status=status, is_climbed=is_climbed)

    def _update_route_record(self, route_record_id, is_climbed=[], status=[]):
        rr = RouteRecord.objects.get(id=route_record_id)
        if rr:
            if status != []:
                rr.status = status
            if is_climbed != []:
                rr.is_climbed = is_climbed
            rr.save()

    def get_route_set_of_grade(self, colour, is_active=False, gym_id=[]):
        query = self._get_all_routes()
        grade = self.DataMap.grade(colour)
        query = query.filter(grade=grade)
        if is_active:
            query = self._filter_query_to_active_based_on_up_date(query)
        query = self._filter_route_query_by_gym(query, gym_id)
        return _Data(query)

    def add_route_set(self, gym_id, colour, grade_list, up_date, down_date=None):
        grade = self.DataMap.grade(colour)
        up_date = datetime.strptime(up_date, "%d/%m/%Y").date()
        if down_date:
            down_date = datetime.strptime(down_date, "%d/%m/%Y").date()

        grade_sub_list = [self.DataMap.grade_sub(grade_sub_str)
                          for grade_sub_str in grade_list]
        self._create_route_set_for_list_of_grade_sub(
            gym_id, grade, grade_sub_list, up_date, down_date)

    def _create_route_set_for_list_of_grade_sub(self, gym_id, grade, grade_sub_list, up_date, down_date=None):
        gym = self.get_gym(gym_id)
        # up_date = Cast(up_date, DateField)
        is_dup = self._check_for_duplicate_based_on_grade_and_up_date(
            grade, up_date, gym_id)
        if not is_dup:
            rs = RouteSet.objects.create(up_date=up_date, gym=gym)
            if down_date:
                rs.down_date = Cast(down_date, DateField())
                rs.save()

            for ind, grade_sub in enumerate(grade_sub_list):
                number = ind + 1
                Route.objects.create(grade=grade,
                                     grade_sub=grade_sub,
                                     number=number,
                                     route_set=rs)

    def _check_for_duplicate_based_on_grade_and_up_date(self, grade, up_date, gym_id):

        query = Route.objects.all()
        if not query:
            return False

        query = query.filter(grade=grade).filter(route_set__up_date=up_date)
        # breakpoint()
        query = self._filter_route_query_by_gym(query, gym_id)
        if query:
            return True
        else:
            return False

    def create_gym(self, name, email, city):
        return Gym.objects.create(name=name, email=email, city=city)

    def update_gym(self, gym_id, city=[], name=[], email=[]):
        query = Gym.objects.get(id=gym_id)
        if query:
            if name != []:
                query.name = name
            if city != []:
                query.city = city
            if email != []:
                query.email = email
            query.save()

    def _delete_gym(self, gym_id):
        Gym.objects.get(id=gym_id).delete()

    def get_gym(self, gym_id):
        return Gym.objects.get(id=gym_id)

    def _get_gym_all(self):
        return Gym.objects.all()

    def get_gym_all(self):
        return _GymData(self._get_gym_all())


class _DalEdenRocks(_DalBase):
    pass


class _DataBase:
    def __init__(self, query):
        self.query = query

    def _convert_query_to_list(self, field_str):

        return [tmp[field_str] for tmp in self.query.values(field_str)]


class _Data(_DataBase):

    def get_grade(self):
        colour = [conf.Grade(
            a).name for a in self._convert_query_to_list('grade')]
        return colour

    def get_down_date(self):
        return [a.route_set.down_date for a in self.query]

    def get_up_date(self):
        return [a.route_set.up_date for a in self.query]

    def get_grade_sub(self):
        return [conf.GradeSub(a).name for a in self._convert_query_to_list('grade_sub')]

    def get_count(self):
        return self.query.count()

    def get_number(self):
        return self._convert_query_to_list('number')

    def get_route_id(self):
        return self._convert_query_to_list('id')

    def get_route_set_id(self):
        return [a.route_set.id for a in self.query]

    def __repr__(self):
        return f"Colour: {self.get_colour()[0]} \nNum Routes: {self.get_count()} "


class _GymData(_DataBase):
    def __init__(self, query):
        self.query = query

    def get_id(self):
        return self._convert_query_to_list('id')

    def get_city(self):
        return self._convert_query_to_list('city')

    def get_name(self):
        return self._convert_query_to_list('name')

    def get_email(self):
        return self._convert_query_to_list('email')
