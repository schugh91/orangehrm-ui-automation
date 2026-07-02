from playwright.sync_api import Page, expect

def test_valid_login(logged_in_user):
    expect(logged_in_user.locator("h6")).to_have_text("Dashboard")


