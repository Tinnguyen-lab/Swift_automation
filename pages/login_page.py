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

        self.page.locator(
            LoginLocator.USERNAME_INPUT
        ).fill(USERNAME)

        self.page.locator(
            LoginLocator.PASSWORD_INPUT
        ).fill(PASSWORD)

        self.page.locator(
            LoginLocator.LOGIN_BUTTON
        ).click()

        self.page.wait_for_load_state("networkidle")