import pytest
from pages.shop_page import ShopPage


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestAddProducts:
    def test_add_products(self, browser):
        m = ShopPage(browser)
        m.click_product_btn(1)
        m.click_product_btn(2)
        m.check_products_number(2)
