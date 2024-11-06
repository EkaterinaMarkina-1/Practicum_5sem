import pytest
from pages.login_page import LoginPage
from data.utils import Error_messeges


@pytest.mark.regression
class TestLoginEmpty:
    def test_user_login_empty(self, browser):
        m = LoginPage(browser)
        m.try_login("", "")
        m.error_messege(Error_messeges.empty_login_messege)
