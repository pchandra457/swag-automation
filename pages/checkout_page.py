from time import sleep

from selenium.webdriver.common.by import By

class CheckoutPage:

    checkout = (By.ID, "checkout")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def start_checkout(self):
        self.driver.find_element(*self.checkout).click()

    def enter_details(self, first, last, zip):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal).send_keys(zip)
        sleep(2)

    def continue_checkout(self):
        self.driver.find_element(*self.continue_btn).click()
        sleep(2)