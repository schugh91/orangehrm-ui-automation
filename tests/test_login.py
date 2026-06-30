from playwright.sync_api import Page, expect
from utils.config import URL, USERNAME, PASSWORD
from pages.orangehrm_login_page import LoginPage

def test_valid_login(page: Page):
    login_page = LoginPage(page)
    page.goto(URL)
    login_page.get_username(USERNAME)
    login_page.get_password(PASSWORD)
    login_page.get_login_button()
    expect(page.locator("h6")).to_have_text("Dashboard")


