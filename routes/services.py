from routes.models import RouteSet, Route, RouteRecord, Profile
from enum import Enum
import routes.conf as conf
from datetime import datetime
from django.db.models import DateField
from django.db.models.functions import Cast, Coalesce
# if __name__ == "__main__":
#     import django
#     import os

#     os.environ['DJANGO_SETTINGS_MODULE'] = 'tracks.settings'
#     django.setup()


def get_dal(key='eden'):
    if key == 'eden':
        _dal = _DalEdenRocks()
    else:
        _dal = _DalEdenRocks()
    return _dal


class _DalBase:

    def _get_all_routes(self):
        query = Route.objects.all().order_by('-route_set__up_date')
        return query

    def _create_route_set_for_list_of_grade_sub(self, grade, grade_sub_list, up_date, down_date=None):
        up_date = Cast(up_date, DateField())
        is_dup = self._check_for_duplicate_based_on_grade_and_up_date(
            grade, up_date)
        if not is_dup:
            rs = RouteSet.objects.create(up_date=up_date)

            if down_date:
                rs.down_date = Cast(down_date, DateField())
                rs.save()

            for ind, grade_sub in enumerate(grade_sub_list):
                number = ind + 1
                Route.objects.create(grade=grade,
                                     grade_sub=grade_sub,
                                     number=number,
                                     route_set=rs)

    def _check_for_duplicate_based_on_grade_and_up_date(self, grade, up_date):
        query = Route.objects.all().filter(grade=grade).filter(route_set__up_date=up_date)

        if query:
            return True
        else:

            return False

    def _filter_query_to_active_based_on_up_date(self, query):
        for index in range(0, query.count()):
            date_search = query[index].route_set.up_date
            if date_search < datetime.now().date():
                id = query[index].route_set.id
                query = query.filter(route_set__id=id)
                return query
        return query


class _DalEdenRocks(_DalBase):
    def __init__(self):
        pass

    def get_routes_all(self):
        query = self._get_all_routes()
        data = _EdenRockData(query)
        return data

    def get_route_set_of_grade(self, colour, is_active=False):
        query = self._get_all_routes()
        grade = _EdenRockConfMapper.grade(colour)
        query = query.filter(grade=grade)
        if is_active:
            query = self._filter_query_to_active_based_on_up_date(query)

        return _EdenRockData(query)

    def add_route_set(self, colour, grade_list, up_date, down_date=None):
        grade = _EdenRockConfMapper().grade(colour)
        up_date = datetime.strptime(up_date, "%d/%m/%Y").date()
        if down_date:
            down_date = datetime.strptime(down_date, "%d/%m/%Y").date()

        grade_sub_list = [_EdenRockConfMapper().grade_sub(grade_sub_str)
                          for grade_sub_str in grade_list]
        self._create_route_set_for_list_of_grade_sub(
            grade, grade_sub_list, up_date, down_date)


class _EdenRockData:
    def __init__(self, query):
        self.query = query

    def _convert_query_to_list(self, field_str):

        return [tmp[field_str] for tmp in self.query.values(field_str)]

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


class _EdenRockConfMapper:

    @staticmethod
    def grade(colour):
        g = conf.Grade
        return g.get_value_from_name(colour)

    @staticmethod
    def grade_sub(grade):
        g = conf.GradeSub
        return g.get_value_from_name(grade)


class Utils:
    @staticmethod
    def convert_str_to_datetime(date_str):
        date = datetime.strptime(date_str, "%d/%m/%Y").date()
        return date


def get_route_record_for_user(user_id, route_id):
    rr = _get_route_record_for_user(user_id, route_id)
    status = [record.status for record in rr]
    is_climbed = [record.is_climbed for record in rr]
    return status, is_climbed


def _get_route_record_for_user(user_id, route_id):
    if not isinstance(route_id, (list,)):
        route_id = [route_id]
    query = RouteRecord.objects.filter(
        user__id=user_id).filter(route__id__in=route_id)
    return query


def set_route_record_for_user(user_id, route_id, status, is_climbed):
    query = _get_route_record_for_user(user_id, route_id)
    if query:
        _update_route_record(
            query[0].id, status=status, is_climbed=is_climbed)
    else:
        _create_route_record(
            user_id, route_id, status=status, is_climbed=is_climbed)


def _update_route_record(route_record_id, is_climbed=[], status=[]):
    rr = RouteRecord.objects.get(id=route_record_id)
    if status != []:
        rr.status = status
    if is_climbed != []:
        rr.is_climbed = is_climbed
    rr.save()


def _create_route_record(user_id, route_id, is_climbed=False, status=0):
    profile = Profile.objects.all().filter(user__id=user_id)
    route = Route.objects.all().filter(id=route_id)
    if profile and route:
        RouteRecord.objects.create(
            user=profile[0], route=route[0], status=status, is_climbed=is_climbed)
