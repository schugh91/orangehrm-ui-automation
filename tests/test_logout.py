from playwright.sync_api import Page, expect
from pages.orangehrm_dashboard_page import DashboardPage

def test_logout(logged_in_user):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.logout()
    expect(logged_in_user.get_by_role("button", name = "Login")).to_be_visible()
