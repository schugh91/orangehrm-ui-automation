from pages.orangehrm_PIM_page import PIMPage
from playwright.sync_api import expect


def test_navigate_to_pim_page(logged_in_user):
    pim_page = PIMPage(logged_in_user)
    pim_page.get_pim_page()
    expect(logged_in_user.locator("h6")).to_have_text("PIM")

