import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


# TC001: Verify successful login with valid credentials
# Test Type: Positive / Happy Path
def test_valid_login(page: Page):
    # Arrange: Initialize the Login Page Object
    login_page = LoginPage(page)

    # Act: Open the application and log in using valid credentials
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Assert: Verify that the user is redirected to the Products page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products", exact=True)).to_be_visible()


# TC012: Verify login rejection with an invalid username
# TC016: Verify login rejection when using a locked-out account
# Test Type: Negative
@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        (
            "invalid_user",
            "secret_sauce",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "locked_out_user",
            "secret_sauce",
            "Epic sadface: Sorry, this user has been locked out.",
        ),
    ],
    ids=["TC012-invalid-credentials", "TC016-locked-out-account"],
)
def test_invalid_login(
    page: Page,
    username: str,
    password: str,
    expected_message: str,
):
    # Arrange: Initialize the Login Page Object
    login_page = LoginPage(page)

    # Act: Open the application and attempt to log in with the provided credentials
    login_page.navigate()
    login_page.login(username, password)

    # Assert: Verify that the expected login error message is displayed
    login_page.verify_login_error(expected_message)
