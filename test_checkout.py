import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutInfoPage, CheckoutOverviewPage, CheckoutCompletePage


@pytest.fixture
def checkout_info_page():
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service)
    drv.implicitly_wait(5)
    drv.get("https://www.saucedemo.com/")

    LoginPage(drv).login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(drv)
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    CartPage(drv).checkout()

    yield CheckoutInfoPage(drv)
    drv.quit()

def test_valid_checkout_info(checkout_info_page):
    checkout_info_page.fill_info("John", "Doe", "12345")
    assert "checkout-step-two" in checkout_info_page.driver.current_url

def test_blank_first_name_shows_error(checkout_info_page):
    checkout_info_page.fill_info("", "Doe", "12345")
    assert "First Name is required" in checkout_info_page.get_error_text()


def test_order_total_is_calculated(checkout_info_page):
    checkout_info_page.fill_info("John", "Doe", "12345")
    overview_page = CheckoutOverviewPage(checkout_info_page.driver)
    assert "Total" in overview_page.get_total_text()


def test_finish_completes_order(checkout_info_page):
    checkout_info_page.fill_info("John", "Doe", "12345")
    overview_page = CheckoutOverviewPage(checkout_info_page.driver)
    overview_page.finish()

    complete_page = CheckoutCompletePage(checkout_info_page.driver)
    assert "Thank you" in complete_page.get_confirmation_text()