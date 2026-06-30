from playwright.sync_api import Page, expect
from utils.config import URL, USERNAME, PASSWORD

def test_valid_login(page: Page):
    page.goto(URL)
    page.get_by_placeholder("Username").fill(USERNAME)
    page.get_by_placeholder("Password").fill(PASSWORD)
    page.get_by_role("button", name = "Login").click()
    expect(page.locator("h6")).to_have_text("Dashboard")


