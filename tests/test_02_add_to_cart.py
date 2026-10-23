from time import sleep

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import USERNAME, PASSWORD

def test_add_product_to_cart(driver):

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_product()
    inventory.open_cart()
    sleep(2)
    assert "cart" in driver.current_url