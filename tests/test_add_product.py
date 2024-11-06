import pytest
from pages.shop_page import ShopPage


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestAddProduct:
    def test_add_product(self, browser):
        m = ShopPage(browser)
        m.click_product_btn(1)
        m.check_products_number(1)
