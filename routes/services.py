if __name__ == "__main__":
    import django
    import os

    os.environ['DJANGO_SETTINGS_MODULE'] = 'tracks.settings'
    django.setup()

from routes.models import RouteSet, Route
from enum import Enum
import routes.conf as conf
import datetime
from django.db.models import DateField
from django.db.models.functions import Cast, Coalesce



def get_dal(key='eden'):
    if key == 'eden':
        _dal = _DalEdenRocks()
    else:
        _dal = _DalEdenRocks()
    return _dal


class _DalBase:
    @staticmethod
    def _create_route_set_for_list_of_grade_sub(grade, grade_sub_list, up_date, down_date=None):

        rs = RouteSet.objects.create(up_date=Cast(up_date, DateField()))
        
        if down_date:
            rs.down_date = Cast(down_date, DateField())
            rs.save()
        
        for ind, grade_sub in enumerate(grade_sub_list):
            number = ind + 1
            Route.objects.create(grade=grade,
                                grade_sub=grade_sub,
                                number=number,
                                route_set=rs)
            # r.objects.create = Route(grade=grade,
            #         grade_sub=grade_sub,
            #         number=number,
            #         route_set=rs)
            # rs.routes.add_route_set(r)
            # r.save()


class _DalEdenRocks(_DalBase):
    def __init__(self, is_active=True):
        self.is_active = True
        pass

    def get_routes_all(self):
        query = Route.objects.all()
        data = _EdenRockData(query)
        return data
       
    def add_route_set(self, colour, grade_list, up_date, down_date=None):
        eden_map = _EdenRockConfMapper()
        grade = eden_map.colour(colour)
        up_date = datetime.datetime.strptime(up_date, "%d/%m/%Y").date()
        if down_date:
            down_date = datetime.datetime.strptime(down_date, "%d/%m/%Y").date()

        grade_sub_list = [eden_map.grade(grade_sub_str) for grade_sub_str in grade_list]
        self._create_route_set_for_list_of_grade_sub(grade, grade_sub_list, up_date, down_date)


class _EdenRockData:
    def __init__(self, query):
        self.query = query

    def _convert_query_to_list(self, field_str):
        
        return [tmp[field_str] for tmp in self.query.values(field_str)]

    def get_colour(self):
        colour = [conf.Grade(a).name for a in self._convert_query_to_list('grade')]
        return colour

    def get_down_date(self):
        return [a.route_set.down_date for a in self.query]

    def get_up_date(self):
        return [a.route_set.up_date for a in self.query]

    def get_grade(self):
        return [conf.GradeSub(a).name for a in self._convert_query_to_list('grade_sub')]

    def get_count(self):
        return self.query.count()

    def get_number(self):
        return self._convert_query_to_list('number')

    def get_route_id(self):
        return self._convert_query_to_list('id')

    def get_route_set_id(self):
        return [a.route_set.id for a in self.query]

    def get_route_set_is_active(self):
        return [a.route_set.is_active for a in self.query]


def _deactivate_all_active_route_sets_of_a_colour(colour):
    Route.objects.all()


class _EdenRockConfMapper:
    def colour(self, colour):
        g = conf.Grade
        return g.get_value_from_name(colour)

    def grade(self, grade):
        g = conf.GradeSub
        return g.get_value_from_name(grade)

    def up_date(self, up_date):
        pass

    def down_date(self, down_date):
        pass
