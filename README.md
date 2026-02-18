# Playwright Automation Framework

End-to-end test automation framework built with Playwright and Pytest.

This project follows clean architecture principles including:
- Page Object Model (POM)
- Centralized fixtures
- Indirect parametrization
- Custom pytest markers
- Scalable test structure

---

## 🛠 Tech Stack

- Python 3.x
- Pytest
- Playwright
- Page Object Model (POM)
- Git

---

## 📁 Project Structure

playwright_repogit/

├── yobingo_site_automations/      # Page Objects & automation logic  
├── yobingo_site_login_tests/      # Test suite  
│   ├── config/                    # Test data configuration  
│   ├── tests/                     # Test cases  
│   │   ├── conftest.py            # Fixtures & test setup  
│   │   └── test_login.py  
│   ├── pytest.ini                 # Pytest configuration & markers  
│  
├── requirements.txt  
├── .gitignore  

---

## 🚀 Installation

Clone the repository:

    git clone <repository-url>
    cd <repository-folder>

Create virtual environment:

    python -m venv venv
    source venv/bin/activate  # macOS/Linux

Install dependencies:

    pip install -r requirements.txt
    playwright install

---

## 🧪 Running Tests

Run all tests:

    pytest

Run specific marker:

## 🏷 Custom Markers

Markers are defined in `pytest.ini`.

Example:

    [pytest]
    markers =
        login: login-related tests
        regression: regression suite
        smoke: smoke tests

Execute by marker:

    pytest -m login

## 📌 Future Enhancements

- CI/CD integration (GitHub Actions)
- Environment configuration (QA / STG / PROD)
- Session-level authentication reuse
- Reporting integration (Allure)
