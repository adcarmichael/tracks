from django.test import TestCase
from django.urls import resolve
from routes.views import home_page
from routes.models import RouteSet, Route
from django.test import Client
import routes.services as services
from datetime import datetime
import routes.conf as conf
from django.db.models.functions import Cast, Coalesce
from django.db.models import DateField


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        c = Client()
        response = c.get('/')
        self.assertTemplateUsed(response, 'home_page.html')


class RoutePageTest(TestCase):
    def test_route_page_returns_correct_html(self):
        c = Client()
        response = c.get('/')
        html = response.content.decode('utf')
        self.assertTrue(html.startswith('<html>'))
        self.assertTrue(html.endswith('</html>'))

    def test_access_to_route_data(self):
        r = Route()
        r.grade = 'Green'
        Route.objects.all()
        # class TestEdenRouteSet(TestCase):

        #     def setup(self):
        #         self.route_grades = [1, 1, 2, 1, 2, 1, 2, 1, 4]
        #         self. up_date = '2019-05-06'
        #         self.down_date = '2010-06-14'
        #         # climber.route.eden(colour='green',routes=route_grades,up_date=up_date,down_date=down_date)
        #         self.fail()

        #     def test_get_all_routes_in_set(self):

        #         self.fail()


class EdenRockMapTest(TestCase):
    def test_colour(self):
        for e in conf.Grade:
            mapped_value = services._EdenRockConfMapper().colour(e.name)
            self.assertEqual(mapped_value, e.value)

    def test_colour_with_mixed_case(self):
        mapped_value = services._EdenRockConfMapper().colour('GreeN')
        self.assertEqual(mapped_value, conf.Grade.green.value)


class TestDal(TestCase):
    def add_sample(self, colour='black', grade=['high', 'medium'], down_date=None, up_date='03/06/2019'):
        dal = services.get_dal()
        dal.add_route_set(colour, grade, up_date, down_date=down_date)

    def test_add_route_set(self):

        dal = services.get_dal()
        data = dal.get_routes_all()
        self.assertEqual(data.get_count(), 0,
                         'ensure that there is zero routes in db initially')

        self.add_sample()

        dataNew = dal.get_routes_all()
        self.assertEqual(dataNew.get_count(), 2)
        self.assertEqual(dataNew.get_colour()[0], conf.Grade.black.name)
        self.assertEqual(dataNew.get_grade()[0], conf.GradeSub.high.name)

    def test_deactivate_all_active_route_sets_of_a_colour(self):
        self.add_sample()
        self.add_sample()
        self.fail()

    def test_add_route_with_down_date(self):
        dal = services.get_dal()
        down_date = '04/07/2019'
        down_date_exp = datetime.strptime(
            down_date, "%d/%m/%Y").date()
        self.add_sample(down_date=down_date)
        data = dal.get_routes_all()
        self.assertEqual(data.get_down_date()[0], down_date_exp)

    def test_add_route_without_down_date(self):
        dal = services.get_dal()
        down_date_exp = datetime.strptime(
            '01/01/2000', "%d/%m/%Y").date()
        self.add_sample()
        data = dal.get_routes_all()
        self.assertEqual(data.get_down_date()[0], down_date_exp)

    def test_get_colour(self):
        up_date_old = '11/06/2019'
        up_date_new = '11/07/2019'
        colour_old = 'black'
        colour_new = 'red'
        self.add_sample(up_date=up_date_old, grade=[
                        'medium'], colour=colour_old)
        self.add_sample(up_date=up_date_new, grade=[
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
        self.add_sample(up_date=up_date_active, grade=[
                        'medium'], colour=colour_exp)
        self.add_sample(up_date=up_date_future, grade=[
                        'medium'], colour=colour_exp)
        self.add_sample(up_date=up_date_old, grade=[
                        'medium'], colour=colour_exp)

        dal = services.get_dal()
        data = dal.get_route_set_of_colour(colour_exp, is_active=True)

        colour_act = data.get_colour()[0]
        up_date_act = data.get_up_date()[0]
        self.assertEqual(colour_act, colour_exp)
        self.assertEqual(up_date_act, Utils.convert_to_date(up_date_active))
        self.assertEqual(data.get_count(), 1)


class Utils:
    @staticmethod
    def convert_to_date(date_str):
        date = datetime.strptime(date_str, "%d/%m/%Y").date()
        return date


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

    def test_get_route_set_is_active(self):
        query = self.get_query()
        data = services._EdenRockData(query)
        is_active = data.get_route_set_is_active()
        self.assertEqual(is_active[0], True)
