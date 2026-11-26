from playwright.sync_api import Page, expect


# Page Object Model for the Checkout Overview page
class CheckoutOverviewPage:
    def __init__(self, page: Page):
        # Store the browser page instance for interacting with the Checkout Overview page
        self.page = page

        # Locators: Identify the page title and checkout action buttons
        self.checkout_overview_title = page.get_by_text(
            "Checkout: Overview", exact=True
        )
        self.finish_button = page.get_by_role("button", name="Finish")
        self.cancel_button = page.get_by_role("button", name="Cancel")

        # Locators: Identify product information displayed in the order overview
        self.product_names = page.locator(".inventory_item_name")
        self.product_desc = page.locator(".inventory_item_desc")
        self.product_prices = page.locator(".inventory_item_price")

        # Locators: Identify the order price summary
        self.summary_subtotal = page.locator(".summary_subtotal_label")
        self.summary_tax = page.locator(".summary_tax_label")
        self.summary_total = page.locator(".summary_total_label")

    # Verify that the Checkout Overview page is displayed
    def verify_checkout_overview_page(self):
        expect(self.checkout_overview_title).to_be_visible()

    # Verify that the expected number of products and their information are displayed
    def verify_products_count(self, expected_count: int):
        expect(self.product_names).to_have_count(expected_count)
        expect(self.product_desc).to_have_count(expected_count)
        expect(self.product_prices).to_have_count(expected_count)

    # Verify that the displayed product names match the expected values
    def verify_products(self, expected_names: list[str]):
        expect(self.product_names).to_have_text(expected_names)

    # Verify that the order subtotal, tax, and total match the expected values
    def verify_order_summary(
        self, expected_subtotal: str, expected_tax: str, expected_total: str
    ):
        expect(self.summary_subtotal).to_contain_text(expected_subtotal)
        expect(self.summary_tax).to_contain_text(expected_tax)
        expect(self.summary_total).to_contain_text(expected_total)

    # Verify that the displayed product prices match the expected values
    def verify_product_prices(self, expected_prices: list[str]):
        expect(self.product_prices).to_have_text(expected_prices)

    # Complete the checkout process by clicking the Finish button
    def finish_checkout(self):
        self.finish_button.click()

    # Cancel the checkout process and return to the previous page
    def cancel_checkout(self):
        self.cancel_button.click()
