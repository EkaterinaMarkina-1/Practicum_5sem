from pages.base import Base
from data.constants import Constants
from Locators.auth import Auth
from data.assertions import Assertions
from playwright.sync_api import Page


class LoginPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_login(self):
        self.open("")
        self.input(Auth.USERNAME_INPUT, Constants.login)
        self.input(Auth.PASSWORD_INPUT, Constants.password)
        self.click(Auth.LOGIN_BTN)
        self.assertion.check_URL("inventory.html", "Wrong URL")

    def try_login(self, username, password):
        self.open("")
        self.input(Auth.USERNAME_INPUT, username)
        self.input(Auth.PASSWORD_INPUT, password)
        self.click(Auth.LOGIN_BTN)

    def error_messege(self, messege):
        self.assertion.have_text(Auth.ERROR_MESSEGE, messege, "no")
