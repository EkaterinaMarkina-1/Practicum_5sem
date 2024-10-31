from pages.base import Base
from Locators.auth import Auth
from data.assertions import Assertions
from playwright.sync_api import Page


class LoginPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def login_user(self, username, password):
        self.open("")
        self.input(Auth.USERNAME_INPUT, username)
        self.input(Auth.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(Auth.LOGIN_BTN)

    def check_message_error(self, message):
        self.assertion.contain_text(
            Auth.ERROR_MESSAGE, message, "True Authorization")
