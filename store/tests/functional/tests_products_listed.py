from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class SiteProductListingTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_card_exists(self):
        server_url = "http://127.0.0.1:8000"
        self.driver.get(server_url)

        card = self.driver.find_element(By.CLASS_NAME, "card-text")

    def test_click_details(self):
        server_url = "http://127.0.0.1:8000"
        self.driver.get(server_url)

        detail_link = self.driver.find_element(By.LINK_TEXT, 'View Details')

        # Perform actions on the element if needed
        detail_link.click()

        # TODO: Verify that the product details are displayed correctly.



