from django.test import TestCase
from django.urls import resolve
from routes.views import home_page
from routes.models import RouteSet, Route, RouteRecord, Profile
from django.test import Client
import routes.services as services
from routes.services import Utils
from datetime import datetime
import routes.conf as conf
from django.db.models.functions import Cast, Coalesce
from django.db.models import DateField
import os


def add_sample_route_set(colour='black', grade=['high', 'medium'], down_date=None, up_date='03/06/2019'):
    dal = services.get_dal()
    dal.add_route_set(colour, grade, up_date, down_date=down_date)


def create_superuser_named_admin():
    os.system("""echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell""")


def create_auth_user():
    from django.contrib.auth.models import User
    user = User.objects.create_user(
        'Chevy Chase', 'chevy@chase.com', 'chevyspassword')


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        c = Client()
        response = c.get('/')
        self.assertTemplateUsed(response, 'home_page.html')


# class RoutePageTest(TestCase):
    # def test_route_page_returns_correct_html(self):
    #     c = Client()
    #     response = c.get('/')
    #     html = response.content.decode('utf')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertTrue(html.endswith('</html>'))

    # def test_user_records_route_completion(self):
    #     add_sample_route_set(colour='green')

    #     response = Client().get('routes/')

    #     self.fail('Please complete the test!')
    #     pass

    # def test_access_to_route_data(self):
    #     r = Route()
    #     r.grade = 'Green'
    #     Route.objects.all()


class EdenRockMapTest(TestCase):
    def test_colour(self):
        for e in conf.Grade:
            mapped_value = services._EdenRockConfMapper().colour(e.name)
            self.assertEqual(mapped_value, e.value)

    def test_colour_with_mixed_case(self):
        mapped_value = services._EdenRockConfMapper().colour('GreeN')
        self.assertEqual(mapped_value, conf.Grade.green.value)


class TestDal(TestCase):

    def test_get_all_routes_with_zero_in_database(self):
        dal = services.get_dal()
        data = dal.get_routes_all()
        self.assertFalse(data.get_count())

    def test_add_route_set(self):

        dal = services.get_dal()
        data = dal.get_routes_all()
        self.assertEqual(data.get_count(), 0,
                         'ensure that there is zero routes in db initially')

        add_sample_route_set()

        dataNew = dal.get_routes_all()
        self.assertEqual(dataNew.get_count(), 2)
        self.assertEqual(dataNew.get_colour()[0], conf.Grade.black.name)
        self.assertEqual(dataNew.get_grade()[0], conf.GradeSub.high.name)

    def test_get_all_routes_are_ordered_by_up_date(self):
        dates = ['04/07/2019', '04/07/2021', '04/06/2019']
        add_sample_route_set(grade=['medium'], up_date=dates[0])
        add_sample_route_set(grade=['medium'], up_date=dates[1])
        add_sample_route_set(grade=['medium'], up_date=dates[2])

        dal = services.get_dal()
        data = dal.get_routes_all()

        self.assertEqual(data.get_up_date()[
                         0], Utils.convert_str_to_datetime(dates[1]))
        self.assertEqual(data.get_up_date()[
                         1], Utils.convert_str_to_datetime(dates[0]))
        self.assertEqual(data.get_up_date()[
                         2], Utils.convert_str_to_datetime(dates[2]))

    def test_add_route_with_down_date(self):
        dal = services.get_dal()
        down_date = '04/07/2019'
        down_date_exp = datetime.strptime(
            down_date, "%d/%m/%Y").date()
        add_sample_route_set(down_date=down_date)
        data = dal.get_routes_all()
        self.assertEqual(data.get_down_date()[0], down_date_exp)

    def test_add_route_without_down_date(self):
        dal = services.get_dal()
        down_date_exp = datetime.strptime(
            '01/01/2000', "%d/%m/%Y").date()
        add_sample_route_set()
        data = dal.get_routes_all()
        self.assertEqual(data.get_down_date()[0], down_date_exp)

    def test_get_colour(self):
        up_date_old = '11/06/2019'
        up_date_new = '11/07/2019'
        colour_old = 'black'
        colour_new = 'red'
        add_sample_route_set(up_date=up_date_old, grade=[
            'medium'], colour=colour_old)
        add_sample_route_set(up_date=up_date_new, grade=[
            'medium'], colour=colour_new)
        dal = services.get_dal()
        data = dal.get_route_set_of_colour(colour_new, is_active=False)

        colour_act = data.get_colour()
        self.assertEqual(colour_act[0], colour_new)
        self.assertEqual(data.get_count(), 1)

    def test_get_colour_that_is_active(self):
        ''' This test asserts that only an active date is returned'''
        up_date_old = '11/06/2019'
        up_date_active = '15/06/2019'
        up_date_future = '11/07/2020'
        colour_exp = 'red'

        # Add dates out of order to ensure that it simply is not picking
        # up the latest and is instead ordering query by date
        add_sample_route_set(up_date=up_date_active, grade=[
            'medium'], colour=colour_exp)
        add_sample_route_set(up_date=up_date_future, grade=[
            'medium'], colour=colour_exp)
        add_sample_route_set(up_date=up_date_old, grade=[
            'medium'], colour=colour_exp)

        dal = services.get_dal()
        data = dal.get_route_set_of_colour(colour_exp, is_active=True)

        colour_act = data.get_colour()[0]
        up_date_act = data.get_up_date()[0]
        self.assertEqual(colour_act, colour_exp)
        self.assertEqual(
            up_date_act, Utils.convert_str_to_datetime(up_date_active))
        self.assertEqual(data.get_count(), 1)


class Test_EdenRockData(TestCase):

    def get_query(self):
        up_date = datetime.strptime('01/02/1989', "%d/%m/%Y").date()
        rs = RouteSet.objects.create(up_date=Cast(up_date, DateField()))
        Route.objects.create(grade=2,
                             grade_sub=4,
                             number=1,
                             route_set=rs)
        Route.objects.create(grade=3,
                             grade_sub=4,
                             number=2,
                             route_set=rs)
        return Route.objects.all()

    def test_get_colour(self):
        query = self.get_query()
        erd = services._EdenRockData(query)
        colour = erd.get_colour()
        self.assertEqual(colour[0], 'orange')

    def test_get_grade(self):
        query = self.get_query()
        erd = services._EdenRockData(query)
        grade = erd.get_grade()
        self.assertEqual(grade[0], 'high')

    def test_get_down_date(self):
        query = self.get_query()
        erd = services._EdenRockData(query)
        down_date = erd.get_down_date()
        down_date_exp = datetime.strptime('01/01/2000', "%d/%m/%Y").date()
        self.assertEqual(down_date[0], down_date_exp)

    def test_get_up_date(self):
        query = self.get_query()
        erd = services._EdenRockData(query)
        up_date = erd.get_up_date()
        up_date_exp = datetime.strptime('01/02/1989', "%d/%m/%Y").date()
        self.assertEqual(up_date[0], up_date_exp)

    def test_get_count(self):
        query = self.get_query()
        data = services._EdenRockData(query)
        count = data.get_count()
        self.assertEqual(count, 2)

    def test_get_number(self):
        query = self.get_query()
        data = services._EdenRockData(query)
        number = data.get_number()
        self.assertEqual(number[0], 1)
        self.assertEqual(number[1], 2)

    def test_get_route_id(self):
        query = self.get_query()
        data = services._EdenRockData(query)
        id = data.get_route_id()
        self.assertEqual(id[0], 1)
        self.assertEqual(id[1], 2)

    def test_get_route_set_id(self):
        query = self.get_query()
        data = services._EdenRockData(query)
        id = data.get_route_set_id()
        self.assertEqual(id[0], 1)


class TestRouteRecord(TestCase):
    def create_sample_route_record(self, status=[1], is_climbed=[True], route_num=1):
        create_auth_user()
        add_sample_route_set()
        route = Route.objects.all()
        profile = Profile.objects.first()

        for ind, stat in enumerate(status):
            RouteRecord.objects.create(
                route=route[ind], user=profile, status=status[ind], is_climbed=is_climbed[ind])

    def test_get_route_record(self):

        user_id = 1
        route_id = 1

        self.create_sample_route_record(
            status=[1, 0], is_climbed=[True, False])
        status, is_climbed = services.get_route_record_for_user(
            user_id, route_id)

        self.assertEqual(status[0], 1)
        self.assertEqual(is_climbed[0], True)

    def test_get_rooute_record_for_multi_routes(self):
        user_id = 1
        route_id = [1, 2]

        self.create_sample_route_record(
            status=[1, 0], is_climbed=[True, False])
        status, is_climbed = services.get_route_record_for_user(
            user_id, route_id)

        self.assertEqual(status[0], 1)
        self.assertEqual(status[1], 0)
        self.assertEqual(is_climbed[0], True)
        self.assertEqual(is_climbed[1], False)

    def test_get_rooute_record_for_non_existent_route(self):
        user_id = 1
        route_id = 100

        self.create_sample_route_record(
            status=[1, 0], is_climbed=[True, False])
        status, is_climbed = services.get_route_record_for_user(
            user_id, route_id)

        self.assertEqual(status, [])
        self.assertEqual(is_climbed, [])

    def test_get_rooute_record_for_non_existent_user(self):
        user_id = 100
        route_id = 1

        self.create_sample_route_record(
            status=[1, 0], is_climbed=[True, False])
        status, is_climbed = services.get_route_record_for_user(
            user_id, route_id)

        self.assertEqual(status, [])
        self.assertEqual(is_climbed, [])
