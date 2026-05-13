from data.test_data import BASE_URL
from data.test_data import USERNAME
from data.test_data import PASSWORD

from locators.login_locator import LoginLocator


class LoginPage:

    def __init__(self, page):

        self.page = page

    def login(self):

        self.page.goto(
            BASE_URL,
            wait_until="networkidle"
        )

        username_input = self.page.locator(
            LoginLocator.USERNAME_INPUT
        )

        if not username_input.is_visible(timeout=5000):
            return

        username_input.fill(USERNAME)

        self.page.locator(
            LoginLocator.PASSWORD_INPUT
        ).fill(PASSWORD)

        self.page.locator(
            LoginLocator.LOGIN_BUTTON
        ).click()

        self.page.wait_for_load_state("networkidle")

        self.page.context.storage_state(path="user_data/storage_state.json")
