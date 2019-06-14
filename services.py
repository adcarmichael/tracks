if __name__ == "__main__":
    import django
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tracks.settings'
    django.setup()


from routes.models import RouteSet, Route
from enum import Enum
from unittest import TestCase

class Grade(Enum):
    null = 0
    purple = 1
    orange = 2
    green = 3
    yellow = 4
    blue = 5
    white = 6
    red = 7
    black = 8


class GradeSub(Enum):
    null = 0
    lowest = 1
    low = 2
    medium = 3
    high = 4
    highest = 5


class ClimbStatus(Enum):
    unclimbed = 0
    attempted = 1
    climbed = 2

    def get_default():
        self = ClimbStatus()
        return self.unclimbed


class ConfUtil:
    def __init__(self, conf_obj):
        self.conf_obj = conf_obj

    def map_value_from_name(self, name):
        for e in self.conf_obj:
            if e.name is name:
                return e.value
        return None


class EdenRocks():
    def __init__(self, is_active=True):
        self.is_active = True
        pass

    def get_routes_all(self):
        # Route.objects.get()
        pass

    def get_route_for_set(self):
        pass

    def add_routes(self, colour, routes, up_date, down_date=None):
        conf_grade_util = ConfUtil(Grade)
        conf_grade_sub_util = ConfUtil(GradeSub)
        Route(grade=conf_grade_util.map_value_from_name(colour),
              grade_sub=conf_grade_sub_util)


class EdenRockDbMap():
    def colour(self, colour):
        for e in Grade:
            if e.name.lower() is colour.lower():
                return e.value
        return None

    def routes(self, routes):
        return None

    def up_date(self, up_date):
        pass

    def down_date(self, down_date):
        pass


class EdenRockMapTest(TestCase):
    def test_colour(self):
        map_obj = EdenRockDbMap()
        for e in Grade:
            mapped_value = map_obj.colour(e.name)
            self.assertEqual(mapped_value, e.value)

    def test_colour_with_mixed_case(self):
        map_obj = EdenRockDbMap()
        mapped_value = map_obj.colour('GreeN')
        self.assertEqual(mapped_value, Grade.green.value)
