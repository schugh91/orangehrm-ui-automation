from playwright.sync_api import Page


class PIMPage:
    def __init__(self, page: Page):
        self.page = page
        self.pim_page = page.get_by_role("link", name = "PIM")
        self.employee_list = page.get_by_role("link", name = "Employee List")
        self.employee_name = page.get_by_placeholder("Type for hints...").first
        self.search_button = page.get_by_role("button", name = "Search")
        self.records_found_text = page.locator(".orangehrm-horizontal-padding.orangehrm-vertical-padding").filter(has_text="Record")
        self.add_button = page.get_by_role("button", name = "Add")
        self.enter_first_name = page.get_by_placeholder("First Name")
        self.enter_last_name = page.get_by_placeholder("Last Name")
        self.enter_employee_id = page.locator(".oxd-input-group").filter(has_text="Employee Id").locator("input")
        self.save_button = page.get_by_role("button", name = "Save")
        self.confirm_delete_button = page.get_by_role("button", name = "Yes, Delete")


    def go_to_pim_page(self):
        self.pim_page.click()


    def go_to_employee_list(self):
        self.employee_list.click()

#searching the employee
    def enter_employee_name(self, name,emp_id):
        self.employee_name.fill(name)
        self.enter_employee_id.fill(emp_id)
        self.search_button.click()

    def get_records_found_text(self):
        return self.records_found_text

    def get_employee_result_row(self, emp_id):
        return self.page.get_by_role("row").filter(has_text = emp_id)

#adding new employee

    def click_add_button(self):
        self.add_button.click()

    def add_employee(self, firstname, lastname, emp_id):
        self.enter_first_name.fill(firstname)
        self.enter_last_name.fill(lastname)
        self.enter_employee_id.fill(emp_id)
        self.save_button.click()


#deleting the employee

    def delete_employee(self, emp_id):
        employee_row =  self.get_employee_result_row(emp_id)
        employee_row.locator(".oxd-icon.bi-trash").click()


    def confirm_delete(self):
        self.confirm_delete_button.click()

    def get_no_records_found_text(self):
        return self.page.locator(".oxd-text.oxd-text--span").filter(has_text="No Records Found")