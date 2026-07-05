from driver.driver_factory import create_android_driver
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_with_valid_credentials():
    driver = create_android_driver()

    try:
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.open_login_screen()
        login_page.login("alice", "mypassword")

        assert driver.session_id is not None
    finally:
        driver.quit()