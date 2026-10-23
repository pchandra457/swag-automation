from time import sleep

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from utils.config import USERNAME, PASSWORD

def test_checkout_process(driver):

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_product()
    inventory.open_cart()

    checkout = CheckoutPage(driver)
    checkout.start_checkout()
    checkout.enter_details("John", "Doe", "110001")
    checkout.continue_checkout()
    sleep(2)

    assert "checkout-step-two" in driver.current_url