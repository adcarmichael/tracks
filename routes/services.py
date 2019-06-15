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
    def _add_route_for_set(number, grade, grade_sub, up_date, down_date):
        r = Route(grade=grade,
                  grade_sub=grade_sub,
                  number=number)
        r.route_set = RouteSet(up_date=Cast(up_date,DateField()), down_date=Cast(down_date,DateField()))

        r.route_set.save()
        r.save()


class _DalEdenRocks(_DalBase):
    def __init__(self, is_active=True):
        self.is_active = True
        pass

    def get_routes_all(self):
        a = Route.objects.all()
        student_list = Route.objects.all()
        for student in student_list:
            print(student.grade)
        return a
        

    def add_route_set(self, colour, grade_list, up_date, down_date=None):
        eden_map = _EdenRockConfMapper()
        grade = eden_map.colour(colour)
        up_date_clean = datetime.datetime.strptime(up_date, "%d/%m/%Y").date()
        for ind, grade_sub_str in enumerate(grade_list):
            route_number = ind + 1
            grade_sub = eden_map.grade(grade_sub_str)
            self._add_route_for_set(route_number, grade, grade_sub, up_date_clean, down_date)


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
