from playwright.sync_api import Page, expect


# Page Object Model for the Shopping Cart page
class CartPage:
    def __init__(self, page: Page):
        # Store the browser page instance for interacting with the Cart page
        self.page = page

        # Locators: Identify the elements available on the Cart page
        self.cart_title = page.get_by_text("Your Cart", exact=True)

        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.continue_shopping_button = page.get_by_role(
            "button", name="Continue Shopping"
        )

        # Locators: Identify cart items and their product information
        self.cart_items = page.locator(".cart_item")
        self.cart_item_names = page.locator(".inventory_item_name")
        self.cart_item_desc = page.locator(".inventory_item_desc")
        self.cart_item_prices = page.locator(".inventory_item_price")

    # Verify that the Cart page is displayed
    def verify_cart_page(self):
        expect(self.cart_title).to_be_visible()

    # Verify that the cart contains the expected number of products
    def verify_cart_product_count(self, expected_count: int):
        expect(self.cart_items).to_have_count(expected_count)

    # Verify that the product names in the cart match the expected values
    def verify_cart_product_names(self, expected_names: list[str]):
        expect(self.cart_item_names).to_have_text(expected_names)

    # Verify that the product prices in the cart match the expected values
    def verify_cart_product_prices(self, expected_prices: list[str]):
        expect(self.cart_item_prices).to_have_text(expected_prices)

    # Remove a specific product from the cart using its name
    def remove_product_from_cart(self, product_name: str):
        product = self.cart_items.filter(has_text=product_name)
        product.get_by_role("button", name="Remove").click()

    # Return to the Products page without proceeding to checkout
    def continue_shopping(self):
        self.continue_shopping_button.click()

    # Proceed from the Cart page to the Checkout Information page
    def proceed_to_checkout(self):
        self.checkout_button.click()
