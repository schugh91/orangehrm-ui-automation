from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_dropdown = page.locator(".oxd-userdropdown-tab")
        self.logout_link = page.get_by_role("menuitem", name="Logout")

    def logout(self):
        self.user_dropdown.click()
        self.logout_link.click()