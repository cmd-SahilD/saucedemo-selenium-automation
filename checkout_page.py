from selenium.webdriver.common.by import By


class CheckoutInfoPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def fill_info(self, first_name="", last_name="", zip_code=""):
        if first_name:
            self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        if last_name:
            self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        if zip_code:
            self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_error_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text


class CheckoutOverviewPage:
    FINISH_BUTTON = (By.ID, "finish")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def get_total_text(self):
        return self.driver.find_element(*self.TOTAL_LABEL).text

    def finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()


class CheckoutCompletePage:
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_text(self):
        return self.driver.find_element(*self.COMPLETE_HEADER).text