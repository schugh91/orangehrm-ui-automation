import pytest
from playwright.sync_api import Page
from pages.orangehrm_login_page import LoginPage
from utils.config import USERNAME, PASSWORD, URL

@pytest.fixture
def logged_in_user(page:Page):
    login_page = LoginPage(page)
    page.goto(URL)
    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()
    return page