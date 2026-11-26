import re

from playwright.sync_api import Page, expect

from pages.product_page import ProductPage


# TC002: Verify that all product information and elements are displayed correctly
# Test Type: Positive / Happy Path
def test_inventory_products_elements(logged_in_page: Page):
    # Arrange: Initialize the Product Page Object
    product_page = ProductPage(logged_in_page)
    product_page.verify_product_page()

    # Assert: Verify that all six products and their main elements are present
    expect(product_page.products).to_have_count(6)
    expect(product_page.product_names).to_have_count(6)
    expect(product_page.product_desc).to_have_count(6)
    expect(product_page.prices).to_have_count(6)
    expect(product_page.product_img).to_have_count(6)
    expect(product_page.add_to_cart_button).to_have_count(6)

    # Assert: Verify that each product name is visible and not empty
    for product_name in product_page.product_names.all():
        expect(product_name).to_be_visible()
        expect(product_name).not_to_be_empty()

    # Assert: Verify that each product description is visible and not empty
    for product_desc in product_page.product_desc.all():
        expect(product_desc).to_be_visible()
        expect(product_desc).not_to_be_empty()

    # Assert: Verify that each product price is visible and not empty
    for price in product_page.prices.all():
        expect(price).to_be_visible()
        expect(price).not_to_be_empty()

    # Assert: Verify that each product image is visible and has a non-empty src attribute
    for img in product_page.product_img.all():
        expect(img).to_be_visible()
        expect(img).to_have_attribute("src", re.compile(r".+"))

    # Assert: Verify that all Add to Cart buttons are visible and correctly labeled
    for add_to_cart_button in product_page.add_to_cart_button.all():
        expect(add_to_cart_button).to_be_visible()
        expect(add_to_cart_button).to_have_text("Add to cart")


# TC006: Verify product sorting behavior when switching between sorting options
# Test Type: Edge Case
def test_product_sorting(logged_in_page: Page):
    # Arrange: Initialize the Product Page Object and retrieve the original product data
    product_page = ProductPage(logged_in_page)
    product_page.verify_product_page()

    original_names = product_page.get_product_names()
    original_prices = product_page.get_product_prices()

    # Act & Assert: Sort products by name in ascending order (A to Z)
    product_page.sort_products("Name (A to Z)")
    expected_names_az = sorted(original_names)
    expect(product_page.product_names).to_have_text(expected_names_az)

    # Act & Assert: Sort products by name in descending order (Z to A)
    product_page.sort_products("Name (Z to A)")
    expected_names_za = sorted(original_names, reverse=True)
    expect(product_page.product_names).to_have_text(expected_names_za)

    # Act & Assert: Sort products by price in ascending order (low to high)
    product_page.sort_products("Price (low to high)")
    expected_prices_low = sorted(original_prices)
    assert product_page.get_product_prices() == expected_prices_low

    # Act & Assert: Sort products by price in descending order (high to low)
    product_page.sort_products("Price (high to low)")
    expected_prices_high = sorted(original_prices, reverse=True)
    assert product_page.get_product_prices() == expected_prices_high


# TC005: Verify that a user can successfully log out from the Products page
# Test Type: Positive / Happy Path
def test_logout_from_product_page(logged_in_page: Page):
    # Arrange: Initialize the Product Page Object
    product_page = ProductPage(logged_in_page)
    product_page.verify_product_page()

    # Act: Open the navigation menu and select Logout
    product_page.burger_menu_button.click()
    product_page.logout_button.click()

    # Assert: Verify that the user is redirected to the Login page
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/")
    expect(logged_in_page.get_by_placeholder("Username")).to_be_visible()


# TC007: Verify that a product can be repeatedly added to and removed from the cart
# Test Type: Edge Case
def test_repeated_add_remove_product(logged_in_page: Page):
    # Arrange: Initialize the Product Page Object and locate the Sauce Labs Backpack
    product_page = ProductPage(logged_in_page)
    product_page.verify_product_page()

    backpack = product_page.products.filter(has_text="Sauce Labs Backpack")

    # Act & Assert: Repeat the add and remove actions three times
    for _ in range(3):
        # Act: Add the product to the cart
        product_page.add_product_to_cart("Sauce Labs Backpack")

        # Assert: Verify that the button changes to Remove and the cart badge shows 1
        expect(backpack.get_by_role("button", name="Remove")).to_be_visible()
        expect(product_page.cart_badge).to_have_text("1")

        # Act: Remove the product from the cart
        product_page.remove_product_from_cart("Sauce Labs Backpack")

        # Assert: Verify that the button returns to Add to cart and the cart badge disappears
        expect(backpack.get_by_role("button", name="Add to cart")).to_be_visible()
        expect(product_page.cart_badge).to_have_count(0)
