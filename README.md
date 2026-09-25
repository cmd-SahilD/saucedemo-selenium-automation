# SauceDemo Automation — Selenium + Python

Automated regression suite for [saucedemo.com](https://www.saucedemo.com/), built with
Selenium WebDriver, Pytest, and the Page Object Model (POM) pattern.

## Coverage

- **Login** — valid login, locked-out user, blank username/password, invalid credentials
- **Inventory** — product listing, sorting, add to cart
- **Cart** — item display, remove item
- **Checkout** — form validation, order total, full purchase flow

15 automated test cases in total, mapped to a manual test case sheet in `test_cases/`.

## Structure

\```
saucedemo-automation/
├── test_cases/
│   └── saucedemo_testcase.xlsx   # Manual test case sheet
├── login_page.py                  # Page Object: login page
├── inventory_page.py              # Page Object: inventory page
├── cart_page.py                   # Page Object: cart page
├── checkout_page.py               # Page Objects: checkout flow (3 pages)
├── test_login.py                  # 5 login tests
├── test_inventory.py              # 6 inventory/cart tests
└── test_checkout.py               # 4 checkout tests
\```

## Setup

\```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install selenium pytest webdriver-manager
\```

## Running the tests

\```bash
pytest -v              # run everything
pytest test_login.py -v    # run one file
\```

## Notes

- Uses the Page Object Model — locators live in page classes, not in tests, so a UI
  change only requires updating one file.
- Uses `implicitly_wait()` to handle page-load timing instead of hardcoded sleeps.