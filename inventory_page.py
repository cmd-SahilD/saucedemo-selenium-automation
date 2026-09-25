from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")          # new

    def __init__(self, driver):
        self.driver = driver

    def get_item_count(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEM))

    def sort_by(self, option_text):
        Select(self.driver.find_element(*self.SORT_DROPDOWN)).select_by_visible_text(option_text)

    def get_prices(self):
        elements = self.driver.find_elements(*self.ITEM_PRICE)
        return [float(e.text.replace("$", "")) for e in elements]

    def add_first_item_to_cart(self):
        self.driver.find_elements(*self.ADD_TO_CART_BTN)[0].click()

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return badges[0].text if badges else "0"

    def go_to_cart(self):                                       # new
        self.driver.find_element(*self.CART_LINK).click()