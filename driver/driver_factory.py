from appium import webdriver

from config.android_caps import get_android_options


APPIUM_SERVER_URL = "http://127.0.0.1:4723"


def create_android_driver():
    return webdriver.Remote(
        command_executor=APPIUM_SERVER_URL,
        options=get_android_options(),
    )