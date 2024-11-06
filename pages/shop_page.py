from pages.base import Base
from data.constants import Constants
from Locators.shop_page import SHOP
from data.assertions import Assertions
from playwright.sync_api import Page


class ShopPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def click_product_btn(self, idx):
        self.click_element_by_index(SHOP.PRODUCT_BTN, idx)

    def check_products_number(self, expected_number):
        self.assertion.have_text(SHOP.PRODUCT_NUMBER, str(
            expected_number), "wrong number")
