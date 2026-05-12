import re
from locators.quick_sale_locator import QuickSaleLocator

class QuickSalePage:
    def __init__(self, page):

        self.page = page

    # def go_to_salon_center(self):

    #     self.page.get_by_text(
    #         "Salon Center",
    #         exact=True
    #     ).click()

    #     self.page.wait_for_load_state("networkidle")

    def open_quick_sale(self):

        self.page.locator(
            QuickSaleLocator.QUICK_SALE_BUTTON
        ).click()

        self.page.wait_for_load_state("networkidle")

    def select_tech(self):

        self.page.locator(
            QuickSaleLocator.TECH_CARD
        ).click()

    def select_service(self):

        self.page.locator(
            QuickSaleLocator.MANICURE_BUTTON
        ).click()

        self.page.locator(
            QuickSaleLocator.SERVICE_BUTTON
        ).click()

        self.page.get_by_text(
            "Continue"
        ).click()

    def input_keypad_amount(self, amount):

        for digit in amount:

            self.page.get_by_role(
                "button",
                name=digit,
                exact=True
            ).click()

        self.page.locator(
            QuickSaleLocator.ADD_BUTTON
        ).click()

    def add_discount(self, amount):

        self.page.locator(
            QuickSaleLocator.DISCOUNT_BUTTON
        ).click()

        self.input_keypad_amount(amount)

    def add_tip(self, amount):

        self.page.locator(
            QuickSaleLocator.TIP_BUTTON
        ).click()

        self.input_keypad_amount(amount)

    def save_ticket(self):

        self.page.locator("div").filter(
            has_text=re.compile(r"^Save$")
        ).first.click()

    def payment_full_cash(self):

        self.page.locator(
            QuickSaleLocator.FULL_CASH_BUTTON
        ).click()

        self.page.locator(
            QuickSaleLocator.CHARGE_BUTTON
        ).click()

    def close_bill(self):

        self.page.locator(
            QuickSaleLocator.CLOSE_BILL_BUTTON
        ).click()
