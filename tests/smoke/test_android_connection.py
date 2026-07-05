from appium import webdriver
from appium.options.android import UiAutomator2Options


def test_android_connection():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options,
    )

    assert driver.session_id is not None

    driver.quit()