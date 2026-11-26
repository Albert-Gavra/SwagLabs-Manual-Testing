from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.product_page import ProductPage


# TC004: Verify that a user can complete the checkout process with valid information
# Test Type: Positive / Happy Path
def test_complete_checkout_process(logged_in_page: Page):
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

    # Act: Proceed to the Checkout Information page
    cart_page.proceed_to_checkout()

    # Arrange: Initialize the Checkout Information Page Object
    checkout_info_page = CheckoutInfoPage(logged_in_page)
    checkout_info_page.verify_checkout_info_page()

    # Act: Fill in the required customer information
    checkout_info_page.fill_checkout_info(
        first_name="John", last_name="Doe", postal_code="12345"
    )

    # Act: Submit the customer information
    checkout_info_page.continue_to_checkout_overview()

    # Arrange: Initialize the Checkout Overview Page Object
    checkout_overview_page = CheckoutOverviewPage(logged_in_page)
    checkout_overview_page.verify_checkout_overview_page()

    # Define the expected product names and prices
    expected_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
    ]
    expected_prices = ["$29.99", "$9.99", "$15.99"]

    # Assert: Verify the product count, names, and prices
    checkout_overview_page.verify_products_count(3)
    checkout_overview_page.verify_products(expected_names)
    checkout_overview_page.verify_product_prices(expected_prices)

    # Assert: Verify the order subtotal, tax, and final total
    checkout_overview_page.verify_order_summary(
        expected_subtotal="$55.97",
        expected_tax="$4.48",
        expected_total="$60.45",
    )

    # Act: Finish the checkout process and submit the order
    checkout_overview_page.finish_checkout()

    # Arrange: Initialize the Checkout Complete Page Object
    checkout_complete_page = CheckoutCompletePage(logged_in_page)

    # Assert: Verify that the checkout confirmation page is displayed
    checkout_complete_page.verify_checkout_complete_page()

    # Act: Return to the Products page
    checkout_complete_page.back_to_home()

    # Assert: Verify that the user is redirected to the Products page
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(logged_in_page.get_by_text("Products", exact=True)).to_be_visible()


# TC009: Verify that checkout is rejected when the First Name field is empty
# Test Type: Negative / Edge Case
def test_checkout_empty_first_name(logged_in_page: Page):
    # Arrange: Initialize the Product Page Object
    product_page = ProductPage(logged_in_page)
    product_page.verify_product_page()

    # Act: Add a product to the shopping cart
    product_page.add_product_to_cart("Sauce Labs Backpack")

    # Assert: Verify that the cart badge displays 1
    expect(product_page.cart_badge).to_have_text("1")

    # Act: Navigate to the Cart page
    product_page.go_to_cart()

    # Arrange: Initialize the Cart Page Object
    cart_page = CartPage(logged_in_page)
    cart_page.verify_cart_page()

    # Act: Proceed to the Checkout Information page
    cart_page.proceed_to_checkout()

    # Arrange: Initialize the Checkout Information Page Object
    checkout_info_page = CheckoutInfoPage(logged_in_page)
    checkout_info_page.verify_checkout_info_page()

    # Act: Leave First Name empty while filling in the other required fields
    checkout_info_page.fill_checkout_info(
        first_name="", last_name="Doe", postal_code="12345"
    )

    # Act: Submit the checkout information
    checkout_info_page.continue_to_checkout_overview()

    # Assert: Verify that the user remains on the Checkout Information page
    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )

    # Assert: Verify that the expected validation error message is displayed
    expected_error_message = "Error: First Name is required"
    checkout_info_page.verify_error_message(expected_error_message)
