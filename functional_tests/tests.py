from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewUserRecord(unittest.TestCase):

    def set_up(self):
        self.browser = webdriver.Chrome()

    def tear_down(self):
        self.browser.quit()

    def test_that_user_can_record_route_completion(slef):
        # User goes to the routes page
        self.browser.get('http://localhost:8000/routes')

        # User selects green and rounte number 2 and marks it complete
        inputbox = self.browser.find_element_by_id('id_green_route_2')
        time.sleep(1)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)
