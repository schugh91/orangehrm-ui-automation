# OrangeHRM UI Automation Framework

This project is a UI automation framework for the OrangeHRM demo application using **Python, Playwright, and Pytest**.

The framework follows the **Page Object Model (POM)** design pattern and includes reusable fixtures, test data, and utility methods.

## Application Under Test

OrangeHRM Demo Site:

```text
https://opensource-demo.orangehrmlive.com/
```

## Tech Stack

* Python
* Playwright
* Pytest
* Pytest fixtures
* Pytest parametrization
* Page Object Model
* Environment variables
* Git and GitHub

## Test Coverage

The project currently covers the following scenarios:

* Valid login
* Invalid login
* Logout
* Navigate to PIM page
* Add new employee
* Search employee
* Delete employee

## Project Structure

```text
orangehrm-ui-automation/
│
├── pages/
│   ├── orangehrm_login_page.py
│   ├── orangehrm_dashboard_page.py
│   └── orangehrm_pim_page.py
│
├── test_data/
│   ├── invalid_credentials.py
│   ├── names_data.py

├── tests/
│   ├── test_login.py
│   ├── test_invalid_login.py
│   ├── test_logout.py
│   ├── test_navigate_to_pim_page.py
│   ├── test_add_new_employee.py
│   ├── test_search_an_employee.py
│   └── test_delete_employee.py
│
├── utils/
│   ├── config.py
│   ├── data_generator.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Key Features

### Page Object Model

The framework separates page locators and actions from test logic.

Example:

```python
pim_page.click_add_button()
pim_page.add_employee(firstname, lastname, emp_id)
```

This makes the tests cleaner and easier to maintain.

### Fixtures

A `logged_in_user` fixture is used for tests that require the user to already be logged in.

This avoids repeating login steps in every test.

### Parametrization

Test data is stored separately and used with `pytest.mark.parametrize`.

This allows the same test to run with multiple sets of data.

### Unique Employee ID

Employee IDs are generated uniquely during test execution to avoid duplicate data issues.

This makes add, search, and delete employee tests more stable.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/schugh91/orangehrm-ui-automation.git
cd orangehrm-ui-automation
```

### 2. Create and activate virtual environment

For Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install
```

## Environment Variables

Create a `.env` file in the project root.

Example:

```text
URL=https://opensource-demo.orangehrmlive.com/
USERNAME=Admin
PASSWORD=admin123
```

The `.env` file should not be pushed to GitHub.

## How to Run Tests

Run all tests:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -v
```

Run tests in headed mode:

```bash
pytest --headed -v
```

By default, Playwright runs tests in headless mode, so no extra `--headless` option is needed.

## Run a Specific Test File

```bash
pytest tests/test_login.py -v
```

Example:

```bash
pytest tests/test_add_new_employee.py -v
```

## Test Design Notes

Each test is designed to be independent.

For example, the delete employee test creates its own employee, searches for the same employee, deletes it, and then verifies deletion.

This avoids dependency on another test having already created data.

## Future Improvements

Planned improvements for this framework:

* Add HTML test reports
* Add GitHub Actions CI workflow
* Add screenshot capture on failure
* Improve employee data generation utility
* Add edit employee test
* Add more PIM module validations

## Author

Surabhi Chugh
