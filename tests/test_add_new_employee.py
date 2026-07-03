from playwright.sync_api import expect
from pages.orangehrm_PIM_page import PIMPage

def test_add_new_employee(logged_in_user):
    pim_page = PIMPage(logged_in_user)
    pim_page.get_pim_page()
    pim_page.get_employee_list()
    expect(logged_in_user.get_by_text("Employee Information")).to_be_visible()
    pim_page.click_add_button()
    expect(logged_in_user.get_by_role("heading", name="Add Employee")).to_be_visible()
    pim_page.add_employee("Regency", "Langer")
    expect(logged_in_user.get_by_role("heading", name="Personal Details")).to_be_visible()
    expect(logged_in_user.get_by_placeholder("First Name")).to_have_value("Regency")