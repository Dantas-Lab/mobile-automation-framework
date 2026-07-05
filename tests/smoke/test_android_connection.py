from driver.driver_factory import create_android_driver
from pages.home_page import HomePage


def test_android_connection():
    driver = create_android_driver()

    try:
        home_page = HomePage(driver)

        assert home_page.get_session_id() is not None
    finally:
        driver.quit()