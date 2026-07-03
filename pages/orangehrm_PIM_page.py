from playwright.sync_api import Page


class PIMPage:
    def __init__(self, page: Page):
        self.page = page
        self.PIM_page = page.get_by_role("link", name = "PIM")
        self.employee_list = page.get_by_role("link", name = "Employee List")
        self.employee_name = page.get_by_placeholder("Type for hints...").first
        self.search_button = page.get_by_role("button", name = "Search")
        self.records_found_text = page.locator(".oxd-text.oxd-text--span").filter(has_text="(1) Record")
        self.add_button = page.get_by_role("button", name = "Add")
        self.enter_first_name = page.get_by_placeholder("First Name")
        self.enter_last_name = page.get_by_placeholder("Last Name")
        self.save_button = page.get_by_role("button", name = "Save")


    def get_pim_page(self):
        self.PIM_page.click()


    def get_employee_list(self):
        self.employee_list.click()

    def enter_employee_name(self, name):
        self.employee_name.fill(name)
        self.search_button.click()


    def get_records_found_text(self):
        return self.records_found_text

    def click_add_button(self):
        self.add_button.click()

    def add_employee(self, firstname, lastname):
        self.enter_first_name.fill(firstname)
        self.enter_last_name.fill(lastname)
        self.save_button.click()

    def get_employee_result_row(self,firstname, lastname):
        return self.page.get_by_role("row").filter(has_text = firstname).filter(has_text = lastname)