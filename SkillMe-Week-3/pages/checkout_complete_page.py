from playwright.sync_api import Page, expect


# Page Object Model for the Checkout Complete page
class CheckoutCompletePage:
    def __init__(self, page: Page):
        # Store the browser page instance for interacting with the Checkout Complete page
        self.page = page

        # Locators: Identify the elements displayed after a successful checkout
        self.checkout_complete_title = page.get_by_text(
            "Checkout: Complete!", exact=True
        )
        self.checkout_complete_message = page.get_by_text(
            "Thank you for your order!", exact=True
        )
        self.checkout_complete_desc = page.get_by_text(
            "Your order has been dispatched, and will arrive just as fast as the pony can get there!",
            exact=True,
        )
        self.back_home_button = page.get_by_role("button", name="Back Home")

    # Verify that the checkout confirmation page and its messages are displayed
    def verify_checkout_complete_page(self):
        expect(self.checkout_complete_title).to_be_visible()
        expect(self.checkout_complete_message).to_be_visible()
        expect(self.checkout_complete_desc).to_be_visible()

    # Return to the Products page after completing the checkout
    def back_to_home(self):
        self.back_home_button.click()
