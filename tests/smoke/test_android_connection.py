from driver.driver_factory import create_android_driver


def test_android_connection():
    driver = create_android_driver()

    try:
        assert driver.session_id is not None
    finally:
        driver.quit()