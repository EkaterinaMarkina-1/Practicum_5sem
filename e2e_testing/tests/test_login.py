import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
        m = LoginPage(browser)
        m.login_user()
