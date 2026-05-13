import pytest

from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.quick_sale_page import QuickSalePage

from data.test_data import DISCOUNT_AMOUNT
from data.test_data import TIP_AMOUNT

def test_qs_001(page):

        login_page = LoginPage(page)

        quick_sale_page = QuickSalePage(page)

        login_page.login()

        page.wait_for_load_state("networkidle")

        quick_sale_page.go_to_salon_center()

        quick_sale_page.open_quick_sale()

        quick_sale_page.select_tech()

        quick_sale_page.select_service()

        quick_sale_page.add_discount(DISCOUNT_AMOUNT)

        quick_sale_page.add_tip(TIP_AMOUNT)

        quick_sale_page.payment_full_cash()
        
        quick_sale_page.close_bill()

        expect(
            page.get_by_text("Bill is closed")
        ).to_be_visible(timeout=10000)
