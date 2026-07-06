from playwright.sync_api import expect
from pages.orangehrm_PIM_page import PIMPage
from test_data.names_data import names_data
import pytest
import random

@pytest.mark.parametrize("data", names_data)
def test_search_an_employee(logged_in_user,data):
   pim_page = PIMPage(logged_in_user)

   emp_id = str(random.randint(100, 1000))
   pim_page.get_pim_page()
   pim_page.get_employee_list()
   pim_page.click_add_button()
   pim_page.add_employee(data['firstname'], data['lastname'], emp_id)
   expect(logged_in_user.get_by_role("heading", name="Personal Details")).to_be_visible()
   pim_page.get_employee_list()
   pim_page.enter_employee_name(f"{data['firstname']} {data['lastname']}",emp_id)
   expect(pim_page.get_records_found_text()).to_be_visible()
   expect(pim_page.get_employee_result_row(emp_id)).to_be_visible()
