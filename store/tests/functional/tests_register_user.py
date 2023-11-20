from django.test import TestCase
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import environ

env = environ.Env()
env.read_env('.env_test')


class RegisterUserTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        server_url = "http://127.0.0.1:8000"
        url_path = "register"

        username = env('ACCOUNT')
        password = env('PASSWORD')
        email = env('EMAIL')

        print(f"Registering user {username}")

        self.driver.get(server_url + "/" + url_path)

        title = self.driver.title
        assert "Register" in title

        # Register new user
        input_box = self.driver.find_element(By.ID, "register_user")
        input_box.send_keys(username)
        input_box = self.driver.find_element(By.ID, "email")
        input_box.send_keys(email)
        input_box = self.driver.find_element(By.ID, "register_password")
        input_box.send_keys(password)
        input_box = self.driver.find_element(By.ID, "confirm_password")
        input_box.send_keys(password)
        button = self.driver.find_element(By.XPATH, "//button[text()='Register']")
        time.sleep(1)
        button.click()

        time.sleep(1)
        try:
            error_detected = self.driver.find_element(By.CLASS_NAME, "error")
            print(error_detected.text)
        except NoSuchElementException:
            print("User account created successfully.")

        time.sleep(1)
        self.driver.get(server_url + "/" + url_path)

        title = self.driver.title
        assert "Register" in title
        time.sleep(1)

        # Sign in with new user
        username = env('ACCOUNT')
        password = env('PASSWORD')

        input_box = self.driver.find_element(By.ID, "username")
        input_box.send_keys(username)
        input_box = self.driver.find_element(By.ID, "password")
        input_box.send_keys(password)
        button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        time.sleep(1)
        button.click()
        time.sleep(2)
