from .base import RoutesTestCase
from django.test import TestCase
import routes.services.route_set as service_rs
import routes.tests.sampledata as sampledata
import routes.models as models


class TestCreateRouteSet(RoutesTestCase):
    gym_id = 1
    grade = [1, 2, 3, 1]
    grade_sub = [1, 1, 2, 4]
    up_date = '2020-01-01'
    down_date = '2020-03-01'
    number = [3, 4, 5, 6]
    zone = 'HELLO'

    def test_create_route_set(self):
        sampledata.create_auth_user()
        sampledata.add_gym()

        service_rs.create_route_set(self.gym_id, self.grade, self.grade_sub,
                                    self.up_date, self.down_date, self.zone, self.number)

        rs = models.RouteSet.objects.get(id=1)

        r_all = models.Route.objects.all()

        self.assertEqual(r_all[0].route_set.zone, self.zone)
        self.assertEqual(r_all[1].route_set.zone, self.zone)
        self.assertEqual(r_all[0].number, self.number[0])
        self.assertEqual(r_all[3].number, self.number[3])

    def test_create_route_set_no_number(self):
        sampledata.create_auth_user()
        sampledata.add_gym()

        service_rs.create_route_set(self.gym_id, self.grade, self.grade_sub,
                                    self.up_date, self.down_date, zone=self.zone)

        rs = models.RouteSet.objects.get(id=1)

        r_all = models.Route.objects.all()

        self.assertEqual(r_all[0].number, 1)
        self.assertEqual(r_all[3].number, 4)

    def test_create_route_set_invalid_gym_id(self):
        sampledata.create_auth_user()
        sampledata.add_gym()

        service_rs.create_route_set(101, self.grade, self.grade_sub,
                                    self.up_date, self.down_date, zone=self.zone)

        self.assertEqual(models.RouteSet.objects.filter(id=1).exists(), False)

    def test_create_route_set_grade(self):
        sampledata.create_auth_user()
        sampledata.add_gym()

        service_rs.create_route_set(self.gym_id, self.grade, self.grade_sub,
                                    self.up_date, self.down_date, zone=self.zone)
        rs = models.RouteSet.objects.get(id=1)

        r_all = models.Route.objects.all()
        self.assertEqual(r_all[0].grade, self.grade[0])
        self.assertEqual(r_all[1].grade, self.grade[1])

    def test_create_route_set_grade(self):
        sampledata.create_auth_user()
        sampledata.add_gym()

        service_rs.create_route_set(self.gym_id, self.grade[0], self.grade_sub,
                                    self.up_date, self.down_date, zone=self.zone)
        rs = models.RouteSet.objects.get(id=1)

        r_all = models.Route.objects.all()
        self.assertEqual(r_all[0].grade, self.grade[0])
        self.assertEqual(r_all[1].grade, self.grade[0])
