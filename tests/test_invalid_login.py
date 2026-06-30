from playwright.sync_api import Page, expect
from utils.config import URL
from pages.orangehrm_login_page import LoginPage
from test_data.invalid_credentials import invalid_login_data
import pytest

@pytest.mark.parametrize("data", invalid_login_data)
def test_invalid_login(page: Page,data):
    login_page = LoginPage(page)
    page.goto(URL)
    login_page.get_username(data["username"])
    login_page.get_password(data["password"])
    login_page.get_login_button()
    expect(page.get_by_text("Invalid credentials")).to_be_visible()