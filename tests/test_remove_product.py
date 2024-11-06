import pytest
from pages.shop_page import ShopPage


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestRemoveProduct:
    def test_remove_product(self, browser):
        m = ShopPage(browser)
        m.click_product_btn(1)
        m.click_product_btn(2)
        m.click_product_btn(1)
        m.check_products_number(1)
