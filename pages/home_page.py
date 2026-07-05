from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class HomePage(BasePage):
    LOGIN_SCREEN_OPTION = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Login Screen")',
    )

    def open_login_screen(self):
        self.click(self.LOGIN_SCREEN_OPTION)