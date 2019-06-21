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
        map_obj = services.EdenRockDbMap()
        for e in services.Grade:
            mapped_value = map_obj.colour(e.name)
            self.assertEqual(mapped_value, e.value)

    def test_colour_with_mixed_case(self):
        map_obj = services.EdenRockDbMap()
        mapped_value = map_obj.colour('GreeN')
        self.assertEqual(mapped_value, services.Grade.green.value)


class TestDal(TestCase):
    def add_sample(self, down_date=None):
        dal = services.get_dal()
        colour = 'black'
        grade = ['high', 'medium']
        up_date = '03/06/2019'

        dal.add_route_set(colour, grade, up_date, down_date=down_date)

    def test_add_route_set(self):

        dal = services.get_dal()
        routes = dal.get_routes_all()
        self.assertEqual(routes.count(), 0,
                         'ensure that there is zero routes in db initially')

        self.add_sample()

        routes = dal.get_routes_all()
        r = routes[0]
        self.assertEqual(routes.count(), 2)
        self.assertEqual(r.grade, conf.Grade.black.value)
        self.assertEqual(r.grade_sub, conf.GradeSub.high.value)

    def test_deactivate_all_active_route_sets_of_a_colour(self):
        self.fail()

    def test_add_route_with_down_date(self):
        dal = services.get_dal()
        down_date = '04/07/2019'
        self.add_sample(down_date=down_date)
        routes = dal.get_routes_all()
        r = routes[0]
        self.assertEqual(r.down_date, down_date)

    def test_add_route_without_down_date(self):
        dal = services.get_dal()
        self.add_sample()
        routes = dal.get_routes_all()
        r = routes[0]
        with self.assertRaises(AttributeError):
            r.down_date


class TestEdenRockPoD(TestCase):

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
        erd = services.EdenRockData(query)
        colour = erd.get_colour()
        self.assertEqual(colour[0], 'orange')

    def test_get_grade(self):
        query = self.get_query()
        erd = services.EdenRockData(query)
        grade = erd.get_grade()
        self.assertEqual(grade[0], 'high')

    def test_get_down_date(self):
        query = self.get_query()
        erd = services.EdenRockData(query)
        down_date = erd.get_down_date()
        down_date_exp = datetime.strptime('01/01/2000', "%d/%m/%Y").date()
        self.assertEqual(down_date[0], down_date_exp)

    def test_get_up_date(self):
        query = self.get_query()
        erd = services.EdenRockData(query)
        up_date = erd.get_up_date()
        up_date_exp = datetime.strptime('01/02/1989', "%d/%m/%Y").date()
        self.assertEqual(up_date[0], up_date_exp)
