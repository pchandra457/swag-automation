from time import sleep

from selenium.webdriver.common.by import By

class InventoryPage:

    add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        sleep(2)
        self.driver.find_element(*self.add_to_cart).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()
        sleep(2)