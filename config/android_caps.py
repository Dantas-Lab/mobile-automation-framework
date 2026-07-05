from appium.options.android import UiAutomator2Options


def get_android_options() -> UiAutomator2Options:
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app_package = "com.appiumpro.the_app"
    options.app_activity = ".MainActivity"

    return options