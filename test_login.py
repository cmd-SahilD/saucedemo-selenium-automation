import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service)
    drv.get("https://www.saucedemo.com/")
    yield drv
    drv.quit()


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url


def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")
    assert "locked out" in login_page.get_error_text()


def test_blank_username(driver):
    login_page = LoginPage(driver)
    login_page.login("", "secret_sauce")
    assert "Username is required" in login_page.get_error_text()


def test_blank_password(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "")
    assert "Password is required" in login_page.get_error_text()


def test_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.login("invalid_user", "wrong_pass")
    assert "do not match" in login_page.get_error_text()