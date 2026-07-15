from pages.orangehrm_pim_page import PIMPage
from playwright.sync_api import expect
import pytest

@pytest.mark.smoke
def test_navigate_to_pim_page(logged_in_user):
    pim_page = PIMPage(logged_in_user)
    pim_page.go_to_pim_page()
    expect(logged_in_user.locator("h6")).to_have_text("PIM")

