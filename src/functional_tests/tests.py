from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os
from django.test import LiveServerTestCase
from routes import models as mdl
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import socket

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SeleniumTest(TestCase):
    def setUp(self):
        self.chrome = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.chrome.implicitly_wait(10)
        self.firefox = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
        self.firefox.implicitly_wait(10)

    def test_visit_site_with_chrome(self):
        self.chrome.get('http://web:8000')
        print(f'{self.chrome.title}')
        self.assertIn(
            self.chrome.title, 'ChalkTracks')

    # def test_visit_site_with_firefox(self):
    #     self.firefox.get('http://web')
    #     self.assertIn(self.firefox.title,
    #                   'Django: the Web framework for perfectionists with deadlines.')

# class NewUserRecord(LiveServerTestCase):

#     def setUp(self):
#         self.browser = webdriver.Chrome()

#     def tearDown(self):
#         self.browser.quit()

#     def test_that_user_can_record_route_completion(self):
#         # User goes to the routes page
#         self.browser.get(self.live_server_url)
#         breakpoint()

#         # User selects green and rounte number 2 and marks it complete
#         inputbox = self.browser.find_element_by_id('sign-up')
#         time.sleep(1)
#         inputbox.send_keys(Keys.ENTER)
#         time.sleep(10)


# os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = '0.0.0.0:8000'


# class RoutesTests(StaticLiveServerTestCase):
#     user_name = 'user_test'
#     user_password = 'password'
#     admin_name = 'admin_test'
#     admin_password = 'password'
#     live_server_url = 'http://{}:8000'.format(
#         socket.gethostbyname(socket.gethostname())
#     )

#     def setUp(self):
#         self.browser = webdriver.Remote(
#             command_executor="http://selenium:4444/wd/hub",
#             desired_capabilities=DesiredCapabilities.CHROME
#         )

#     def tearDown(self):
#         self.browser.quit()
#         super().tearDown()

#     def test_home(self):
#         self.browser.get(self.live_server_url)
    # def create_superuser(self):

    #     user = mdl.User.objects.create_superuser(
    #         self.admin_name, 'admin@myproject.com', self.admin_password)
    #     prof = mdl.Profile.objects.first()
    #     prof.email_confirmed = True
    #     prof.save

    # def create_user(self):

    #     user = mdl.User.objects.create_user(
    #         self.user_name, 'admin@myproject.com', self.user_password)
    #     prof = mdl.Profile.objects.first()
    #     prof.email_confirmed = True
    #     prof.save

    # def add_sample_route_data():
    #     add_sample_data(colour='purple')

    # def create_user_and_add_cookie(self, is_admin=False):
    #     if not is_admin:
    #         self.create_user()
    #     else:
    #         self.create_superuser()

    #     self.client.login(username=self.user_name, password=self.user_password)

    #     cookie = self.client.cookies['sessionid']
    #     self.browser.add_cookie(
    #         {'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
    #     self.browser.refresh()  # need to update page for logged in user

    # def test_user_recording_a_climb(self):

    #     add_sample_data(colour='purple')

    #     self.browser.get(self.live_server_url)
    #     self.create_user_and_add_cookie()

    #     # User goes to routes page
    #     self.browser.get(self.live_server_url + '/users/1/1/routes')

    #     # User clicks on route one to record a climb
    #     route_card = self.browser.find_element_by_id('id-card-1')
    #     route_card.click()

    #     # a modal pops up with the option to record climb; the user clicks
    #     modal_record_climb = self.browser.find_element_by_id(
    #         'modal-sections-record-climb-1')
    #     modal_record_climb.click()

    #     # confirm that route has been recorded
    #     rr = mdl.RouteRecord.objects.all()
    #     self.assertEqual(rr[0].id, 1)
    #     self.assertEqual(rr[0].is_climbed, True)
