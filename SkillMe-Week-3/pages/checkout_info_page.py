from playwright.sync_api import Page, expect


# Page Object Model for the Checkout Information page
class CheckoutInfoPage:
    def __init__(self, page: Page):
        # Store the browser page instance for interacting with the Checkout Information page
        self.page = page

        # Locators: Identify the form fields and elements on the Checkout Information page
        self.checkout_info_title = page.get_by_text(
            "Checkout: Your Information", exact=True
        )
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.get_by_role("button", name="Continue")
        self.cancel_button = page.get_by_role("button", name="Cancel")
        self.error_message = page.locator('[data-test="error"]')

    # Verify that the Checkout Information page is displayed
    def verify_checkout_info_page(self):
        expect(self.checkout_info_title).to_be_visible()

    # Fill in the required customer information fields
    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    # Verify that the expected validation error message is displayed
    def verify_error_message(self, expected_message: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(expected_message)

    # Continue to the Checkout Overview page
    def continue_to_checkout_overview(self):
        self.continue_button.click()

    # Cancel the checkout process and return to the previous page
    def cancel_checkout(self):
        self.cancel_button.click()
