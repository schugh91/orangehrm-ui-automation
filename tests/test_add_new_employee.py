from playwright.sync_api import expect
from pages.orangehrm_pim_page import PIMPage
from test_data.names_data import names_data
import pytest
from utils.data_generator import generate_employee_id

@pytest.mark.parametrize("data", names_data)
def test_add_new_employee(logged_in_user,data):
    pim_page = PIMPage(logged_in_user)
    emp_id = generate_employee_id()
    pim_page.go_to_pim_page()
    pim_page.go_to_employee_list()
    expect(logged_in_user.get_by_text("Employee Information")).to_be_visible()
    pim_page.click_add_button()
    expect(logged_in_user.get_by_role("heading", name="Add Employee")).to_be_visible()
    pim_page.add_employee(data["firstname"], data["lastname"], emp_id)
    expect(logged_in_user.get_by_role("heading", name="Personal Details")).to_be_visible(timeout=10000)
    expect(logged_in_user.get_by_placeholder("First Name")).to_have_value(data["firstname"])
    expect(logged_in_user.get_by_placeholder("Last Name")).to_have_value(data["lastname"])
    expect(logged_in_user.locator(".oxd-input-group").filter(has_text="Employee Id").locator("input")).to_have_value(emp_id)