from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "username")
    PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "password")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "loginBtn")

    def enter_username(self, username: str):
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.type(self.PASSWORD_INPUT, password)

    def tap_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.tap_login()