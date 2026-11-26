from playwright.sync_api import Page, expect


# Page Object Model for the Login page
class LoginPage:
    def __init__(self, page: Page):
        # Store the browser page instance for interacting with the Login page
        self.page = page

        # Locators: Identify the login form elements and error message
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator('[data-test="error"]')

    # Navigate to the SauceDemo Login page
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    # Enter the username and password, then submit the login form
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    # Verify that the expected login error message is displayed
    def verify_login_error(self, expected_message: str):
        expect(self.error_message).to_have_text(expected_message)
