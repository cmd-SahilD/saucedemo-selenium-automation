import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage


@pytest.fixture
def logged_in_driver():
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service)
    drv.implicitly_wait(5)  # new line
    drv.get("https://www.saucedemo.com/")

    login_page = LoginPage(drv)
    login_page.login("standard_user", "secret_sauce")

    yield drv
    drv.quit()
def test_all_products_displayed(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    assert inventory_page.get_item_count() == 6

def test_sort_price_low_to_high(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.sort_by("Price (low to high)")
    prices = inventory_page.get_prices()
    assert prices == sorted(prices)


def test_add_item_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_first_item_to_cart()
    assert inventory_page.get_cart_count() == "1"


def test_cart_starts_empty(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    assert inventory_page.get_cart_count() == "0"

def test_cart_shows_added_item(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(logged_in_driver)
    assert cart_page.get_item_count() == 1


def test_remove_item_from_cart_page(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(logged_in_driver)
    cart_page.remove_first_item()
    assert cart_page.get_item_count() == 0