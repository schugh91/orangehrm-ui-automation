from playwright.sync_api import expect

def test_valid_login(logged_in_user):
    expect(logged_in_user.get_by_role("heading", name="Dashboard")).to_be_visible()


