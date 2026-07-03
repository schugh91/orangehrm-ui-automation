from playwright.sync_api import expect
from pages.orangehrm_PIM_page import PIMPage


def test_search_an_employee(logged_in_user):
   pim_page = PIMPage(logged_in_user)

   pim_page.get_pim_page()
   pim_page.get_employee_list()
   expect(logged_in_user.get_by_text("Employee Information")).to_be_visible()
   pim_page.enter_employee_name("Regency")
   expect(pim_page.get_records_found_text()).to_be_visible()
   expect(pim_page.get_employee_result_row("Regency", "Langer")).to_be_visible()