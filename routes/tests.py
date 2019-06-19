from django.test import TestCase
from django.urls import resolve
from routes.views import home_page
from routes.models import RouteSet, Route
from django.test import Client
import routes.services as services
from datetime import datetime


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
    def test_add_route_set(self):

        dal = services.get_dal()
        routes = dal.get_routes_all()
        self.assertEqual(routes.count(), 0)

        colour = 'black'
        grade = ['high']
        up_date = '03/06/2019'
        dal.add_route_set(colour, grade, up_date)
        routes = dal.get_routes_all()

        self.assertEqual(routes.count(), 1)

    def test__deactivate_all_active_route_sets_of_a_colour(self):
        self.fail()

    def test_add_route_with_down_date(self):
        self.fail()
