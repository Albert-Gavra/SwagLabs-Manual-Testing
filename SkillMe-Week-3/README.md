# Week 3 - Automated UI Test Suite

## Project Overview

This project is part of the SkillMe Software Quality Virtual Internship - Week 3 assignment.

The objective is to build an automated UI test suite using **Playwright with Python and Pytest**, following the Page Object Model (POM) design pattern.

The test suite automates selected test scenarios from the Week 1 manual testing project on [SauceDemo](https://www.saucedemo.com/).

## Tools and Technologies

- Python 3.14
- Playwright 1.65.2
- Pytest 9.2.0
- pytest-html 4.2.0
- Visual Studio Code
- Chromium

## Project Structure

```text
SkillMe-Week-3/
├── tests/
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_login.py
│   └── test_product.py
├── pages/
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── checkout_info_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
├── reports/
│   └── report.html
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Automated Test Scenarios

The project contains 10 automated test executions covering the following scenarios:

| Test Scenario | Test Type |
|---|---|
| Successful Login | Positive |
| Login with Invalid Credentials | Negative |
| Login with Locked-Out Account | Negative |
| Verify Product List and Information | Positive |
| Add Multiple Products and Verify Cart Contents | Positive |
| Complete Checkout with Valid Information | Positive |
| Checkout with Empty First Name | Negative |
| Product Sorting Behavior | Edge Case |
| Verify User Can Log Out | Positive |
| Repeated Add and Remove Product Actions | Edge Case |

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Albert-Gavra/SwagLabs-Manual-Testing.git
cd SwagLabs-Manual-Testing/SkillMe-Week-3
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Install Playwright Browser

```bash
python -m playwright install chromium
```

## How to Run Tests

Run the complete test suite:

```bash
python -m pytest -v
```

Run a specific test file:

```bash
python -m pytest -v tests/test_login.py
```

## HTML Test Report

Generate a self-contained HTML report:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

After execution, open `reports/report.html` in a web browser to view the individual test results.

## Test Execution Result

Latest recorded execution:

- Total Tests: 10
- Passed: 10
- Failed: 0
- Skipped: 0

**Execution Status: All Tests Passed**

## Design and Implementation

This project applies the Page Object Model (POM) to separate page locators and interactions from test logic.

Reusable pytest fixtures are defined in `conftest.py` to handle common setup operations, including logging into the application.

Playwright's built-in auto-waiting and assertion mechanisms are used to improve test reliability without relying on fixed `time.sleep()` delays.

---

**Project:** SkillMe Software Quality Virtual Internship - Week 3  
**Application Under Test:** SauceDemo
