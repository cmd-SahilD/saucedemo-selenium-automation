from selenium.webdriver.common.by import By


class CartPage:
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.cart_button")
    CHECKOUT_BUTTON = (By.ID, "checkout")          # new

    def __init__(self, driver):
        self.driver = driver

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEM))

    def remove_first_item(self):
        self.driver.find_elements(*self.REMOVE_BUTTON)[0].click()

    def checkout(self):                             # new
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()