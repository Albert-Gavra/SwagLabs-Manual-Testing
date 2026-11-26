from playwright.sync_api import Page, expect


# Page Object Model for the Products page
class ProductPage:
    def __init__(self, page: Page):
        # Store the browser page instance for interacting with the Products page
        self.page = page

        # Locators: Identify the page title, cart elements, and product actions
        self.product_title = page.get_by_text("Products", exact=True)
        self.cart_button = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.remove_from_cart_button = page.get_by_role("button", name="Remove")
        self.sorting_dropdown = page.get_by_role("combobox")

        # Locators: Identify the navigation menu and logout button
        self.burger_menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_button = page.get_by_role("button", name="Logout")

        # Locators: Identify product items and their displayed information
        self.products = page.locator(".inventory_item")
        self.product_names = page.locator(".inventory_item_name")
        self.product_desc = page.locator(".inventory_item_desc")
        self.prices = page.locator(".inventory_item_price")
        self.product_img = page.locator(".inventory_item_img img")

    # Verify that the Products page is displayed
    def verify_product_page(self):
        expect(self.product_title).to_be_visible()

    # Sort the displayed products using the selected sorting option
    def sort_products(self, sort_option: str):
        self.sorting_dropdown.select_option(sort_option)

    # Retrieve all displayed product names as a list
    def get_product_names(self):
        return self.product_names.all_text_contents()

    # Retrieve all displayed product prices and convert them into float values
    def get_product_prices(self):
        prices = self.prices.all_text_contents()
        return [float(price.replace("$", "")) for price in prices]

    # Add a specific product to the shopping cart using its name
    def add_product_to_cart(self, product_name: str):
        product = self.products.filter(has_text=product_name)
        product.get_by_role("button", name="Add to cart").click()

    # Remove a specific product from the shopping cart using its name
    def remove_product_from_cart(self, product_name: str):
        product = self.products.filter(has_text=product_name)
        product.get_by_role("button", name="Remove").click()

    # Navigate from the Products page to the Shopping Cart page
    def go_to_cart(self):
        self.cart_button.click()
