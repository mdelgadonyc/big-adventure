from django.test import TestCase
from selenium import webdriver


class SiteRunningTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_server_is_online(self):
        server_url = "http://127.0.0.1:8000"
        self.driver.get(server_url)

        title = self.driver.title
        assert "Big Adventure Store" in title
