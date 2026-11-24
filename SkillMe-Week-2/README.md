# Week 2 – Bug Reports and Regression Tracking

## Project Overview

This project is part of the SkillMe QuestGuard Software Quality Virtual Internship – Week 2.

The objective of this activity is to document previously identified issues in the SauceDemo application, create structured bug reports, and perform regression testing to evaluate the application's existing functionality.

**Application Under Test:** [SauceDemo](https://www.saucedemo.com/)

**Testing Type:** Manual Testing, Bug Reporting, and Regression Testing

**Testing Environment:**
- Operating System: Windows 11
- Browser: Google Chrome

## Project Objectives

- Convert previously identified issues into structured bug reports.
- Assign severity and priority levels based on their impact and urgency.
- Provide evidence for each reported bug.
- Create minimal reproduction steps for the three highest-priority bugs.
- Develop a regression checklist covering reported bugs and core application functionality.
- Retest the application and document the results.

## Bug Reports Summary

A total of six bugs were documented during this activity.

| Bug ID | Bug Title | Severity | Priority | Status |
|---|---|---|---|---|
| BUG-001 | Add to Cart Button Not Clickable | High | High | New |
| BUG-002 | Remove Button Not Clickable | High | High | New |
| BUG-003 | Sort Feature Does Not Update Product Order Correctly | Medium | Medium | New |
| BUG-004 | Product Prices Displayed Incorrectly | High | High | New |
| BUG-005 | Finish Button Not Clickable | Critical | High | New |
| BUG-006 | Application Allows Checkout with an Empty Cart | High | High | New |

## Minimal Reproduction Steps

Minimal reproduction steps were prepared for the three highest-priority bugs:

- BUG-005 – Finish Button Not Clickable
- BUG-001 – Add to Cart Button Not Clickable
- BUG-002 – Remove Button Not Clickable

These steps provide a concise way to reproduce the reported issues.

## Regression Testing

A regression checklist containing 10 test scenarios was created to cover the core application flow and all six reported bugs.

### Test Execution Summary

| Result | Count |
|---|---:|
| Passed | 4 |
| Failed | 6 |
| Total | 10 |

**Pass Rate: 40%**

All 10 test scenarios were executed again. The results remained unchanged, and all six previously reported bugs were still reproducible.

## Retesting Conclusion

The retesting confirmed that the previously identified issues remain present in the current SauceDemo demo application.

No source code modifications or actual bug fixes were performed during this activity. Therefore, the results represent a retest of the existing application rather than verification of deployed fixes.

## Project Files

| File / Folder | Description |
|---|---|
| `Bug-Tracker-and-Regression.xlsx` | Contains the Bug Tracker, Bug Report Details, Regression Checklist, and Minimal Reproduction Steps sheets. |
| `Week-2_Regression-Testing-Summary.docx` | Documents the regression testing execution results and conclusion. |
| `Evidence/` | Contains screenshots and video recordings supporting the reported bugs. |

## Notes

This project was conducted as a manual software testing exercise using the publicly accessible SauceDemo demo application.

All reported issues are documented based on the observed application behavior during testing.
