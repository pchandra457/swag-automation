import pytest
from utils.driver_factory import get_driver
from utils.config import BASE_URL

@pytest.fixture(scope="function")
def driver():

    driver = get_driver()
    driver.get(BASE_URL)

    yield driver

    driver.quit()