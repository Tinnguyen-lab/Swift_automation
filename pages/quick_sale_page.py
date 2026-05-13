import re
from playwright.sync_api import TimeoutError, expect
from locators.quick_sale_locator import QuickSaleLocator

class QuickSalePage:
    def __init__(self, page):

        self.page = page

    def go_to_salon_center(self):

        try:
            self.page.locator(
                QuickSaleLocator.SALON_CENTER_BUTTON
            ).click()
        except Exception:
            self.page.get_by_role("button").first.click()

        self.page.wait_for_load_state("networkidle")

    def open_quick_sale(self):

        self.page.locator(
            QuickSaleLocator.QUICK_SALE_BUTTON
        ).click()

        self.page.locator(
            QuickSaleLocator.QUICK_SALE_PANEL
        ).get_by_text("Add technician").wait_for(state="visible")

    def select_tech(self):

        self.page.locator(
            QuickSaleLocator.QUICK_SALE_PANEL
        ).get_by_text("Now").click()

    def select_service(self):

        self.page.get_by_role(
            "button",
            name="manicure",
            exact=True
        ).click()

        self.page.get_by_role(
            "button",
            name=") GEL - SWEET ESCAPE 60' $40"
        ).click()

        self.page.locator(QuickSaleLocator.QUICK_SALE_PANEL).get_by_text(
            "Continue"
        ).click()

        self.page.get_by_role(
            "button",
            name=re.compile(r"Discount\s+\$?\d*", re.I)
        ).wait_for(state="visible")

    def input_keypad_amount(self, amount):

        for digit in amount:

            self.page.get_by_role(
                "button",
                name=digit,
                exact=True
            ).click()

    def open_bill_discount(self):

        bill_discount_button = self.page.locator(
            "#qs-discount-txt"
        ).locator("xpath=ancestor::button")

        bill_discount_button.wait_for(state="visible")
        bill_discount_button.scroll_into_view_if_needed()
        bill_discount_button.click(force=True)

        try:
            self.page.locator(
                QuickSaleLocator.DISCOUNT_PERCENTAGE_BUTTON
            ).wait_for(state="visible", timeout=3000)
            return
        except TimeoutError:
            pass

        box = bill_discount_button.bounding_box()

        if box:
            self.page.mouse.click(
                box["x"] + box["width"] / 2,
                box["y"] + box["height"] / 2
            )

        self.page.locator(
            QuickSaleLocator.DISCOUNT_PERCENTAGE_BUTTON
        ).wait_for(state="visible", timeout=10000)

    def add_discount(self, amount):

        self.open_bill_discount()
        
        self.page.locator(
            QuickSaleLocator.DISCOUNT_PERCENTAGE_BUTTON
        ).click()

        self.input_keypad_amount(amount)

        self.page.locator(QuickSaleLocator.ADD_DISCOUNT_BUTTON).click()

        self.page.wait_for_timeout(2000)  # Wait for the discount to be applied before proceeding.

    def add_tip(self, amount):
        self.page.wait_for_timeout(2000)

        self.page.get_by_role(
            "button",
            name=re.compile(r"Tips\s+\$?\d*", re.I)
        ).click()

        self.input_keypad_amount(amount)
        
        self.page.get_by_role(
            "button",
            name="Add"
        ).click()

        self.page.wait_for_timeout(2000)
        
        self.page.locator(
                QuickSaleLocator.TIPS_SAVE_BUTTON
            ).click(timeout=5000)

        self.page.wait_for_timeout(2000)

        self.page.get_by_text(
            "Tips Management"
        ).wait_for(state="hidden", timeout=10000)

        self.page.wait_for_timeout(2000)  # Wait for the tip to be applied before proceeding.

    def save_ticket(self):

        save_button = self.page.locator(
            QuickSaleLocator.SAVE_BUTTON
        )

        try:
            save_button.wait_for(state="visible", timeout=5000)
            save_button.click()
        except TimeoutError:
            # Auto-save can hide/disable this button after discount/tip changes.
            pass

    def payment_full_cash(self):

        self.page.locator(
            QuickSaleLocator.FULL_CASH_BUTTON
        ).click()

        charge_button = self.page.locator(
            QuickSaleLocator.CHARGE_BUTTON
        )

        charge_button.wait_for(state="visible")
        charge_button.click()

        receipt_title = self.page.locator(':text("Receipt"):visible').first
        expect(receipt_title).to_be_visible(timeout=10000)

    def close_bill(self):
        receipt_title = self.page.locator(':text("Receipt"):visible').first
        expect(receipt_title).to_be_visible(timeout=10000)

        close_bill_button = self.page.locator(
            QuickSaleLocator.CLOSE_BILL_BUTTON_AT_RECEPT
        )

        try:
            close_bill_button.wait_for(state="visible", timeout=5000)
        except TimeoutError:
            close_bill_button = self.page.get_by_text(
                re.compile("Close Bill", re.I)
            ).first
            close_bill_button.wait_for(state="visible", timeout=10000)

        self.page.wait_for_timeout(2000)

        close_bill_button.click(timeout=10000)

        self.page.wait_for_timeout(2000)
        # expect(
        #     self.page.get_by_text("Bill is closed")
        # ).to_be_visible(timeout=10000)
