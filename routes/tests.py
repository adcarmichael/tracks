from django.test import TestCase
from django.urls import resolve
from routes.views import home_page
from django.http import HttpRequest
from routes.models import RouteSet, Route
from django.test import Client
# Create your tests here.


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


# class TestEdenRouteSet(TestCase):

#     def setup(self):
#         self.route_grades = [1, 1, 2, 1, 2, 1, 2, 1, 4]
#         self. up_date = '2019-05-06'
#         self.down_date = '2010-06-14'
#         # climber.route.eden(colour='green',routes=route_grades,up_date=up_date,down_date=down_date)
#         self.fail()

#     def test_get_all_routes_in_set(self):

#         self.fail()
