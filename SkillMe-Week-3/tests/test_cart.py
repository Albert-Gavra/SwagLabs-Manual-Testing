from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.product_page import ProductPage


# TC003: Verify that the cart displays the correct products and prices
# Test Type: Positive / Happy Path
def test_verify_cart_contents(logged_in_page: Page):
    # Arrange: Initialize the Product Page Object
    product_page = ProductPage(logged_in_page)
    product_page.verify_product_page()

    # Act: Add three selected products to the shopping cart
    product_page.add_product_to_cart("Sauce Labs Backpack")
    product_page.add_product_to_cart("Sauce Labs Bike Light")
    product_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")

    # Assert: Verify that the cart badge displays the correct product count
    expect(product_page.cart_badge).to_have_text("3")

    # Act: Navigate to the Cart page
    product_page.go_to_cart()

    # Arrange: Initialize the Cart Page Object
    cart_page = CartPage(logged_in_page)
    cart_page.verify_cart_page()

    # Define the expected product names and prices
    expected_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
    ]
    expected_prices = ["$29.99", "$9.99", "$15.99"]

    # Assert: Verify the cart product count, names, and prices
    cart_page.verify_cart_product_count(3)
    cart_page.verify_cart_product_names(expected_names)
    cart_page.verify_cart_product_prices(expected_prices)
