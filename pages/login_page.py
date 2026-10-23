from time import sleep

from selenium.webdriver.common.by import By

class LoginPage:

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        sleep(2)
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        sleep(2)
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        sleep(2)
        self.driver.find_element(*self.login_btn).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        sleep(2)