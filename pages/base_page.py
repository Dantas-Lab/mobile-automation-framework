class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_session_id(self):
        return self.driver.session_id