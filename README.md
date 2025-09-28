<!-- Banner -->
<p align="center">
  <img src="E2E_Tricentis_Checkout_Automation/banner.png" alt="E-Commerce Checkout Automation Banner" width="100%" />
</p>

<!-- Badges -->
<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white" alt="Python"/></a>
  <a href="https://www.selenium.dev/"><img src="https://img.shields.io/badge/Selenium-4.24.0-brightgreen?logo=selenium&logoColor=white" alt="Selenium"/></a>
  <a href="https://docs.pytest.org/"><img src="https://img.shields.io/badge/Pytest-Framework-orange?logo=pytest" alt="Pytest"/></a>
  <a href="https://docs.qameta.io/allure/"><img src="https://img.shields.io/badge/Allure-Reports-purple?logo=allure&logoColor=white" alt="Allure"/></a>
  <a href="https://github.com/features/actions"><img src="https://img.shields.io/badge/GitHub-Actions-black?logo=githubactions&logoColor=white" alt="GitHub Actions"/></a>
</p>

---

#  End-to-End E-Commerce Checkout Automation Framework  
🛒 **End-to-End Checkout Automation for Tricentis Demo Web Shop**

This project implements a robust, maintainable and highly readable **end-to-end test checkout automation solution** for the **Tricentis Demo Web Shop checkout process** using **Selenium WebDriver** with **Python**.

It follows **Page Object Model (POM)** design pattern for maintainibility and reusibility, incorporates **explicit waits** for dynamic elements and includes  **logging, assertions** and **error handling** fo robust execution.

---

## 🛠 Tech Stack

- **Language:** Python 3.11+  
- **Automation:** Selenium WebDriver 4.24.0  
- **Framework:** Pytest  
- **Reporting:** Allure Reports  
- **Driver:** ChromeDriver (latest compatible)  

---

## 📊 Quality & Reporting

- Allure HTML Reports with Screenshots  
- Python Logging for detailed execution traces  
- Assertions for critical checkpoints  

---

## ✨ Project Overview & Architecture

This framework is built on the **Page Object Model (POM)** design pattern, ensuring **maintainability, readability and reusability**.  

**Key Features:**
- 🏗️ **Page Object Model (POM):** All web interactions encapsulated in `/pages`  
- 🔄 **Robust Synchronization:** Explicit waits handle dynamic elements  
- 🔒 **Data Management:** Test data managed in `test_data.json` via `JsonReader`  
- 📢 **Observability:** Comprehensive Python logging  
- 📸 **Error Handling:** Automatic screenshots on failure attached to Allure  
- ✅ **Assertions:** Built-in test validation points  

---

## 🎯 Objective: The End-to-End Checkout Flow

### Test Scenario (`tests/main.py`):
1. **Login** – Authenticate with newly created credentials from external json file source 
2. **Choose Product from Homepage** – Add a product from main page  
3. **Search & Add Product** – Add multiple products from `test_data.json`  
4. **Cart Validation** – Validate items + total price  
5. **Checkout Initiation** – Start checkout after ToS agreement  
6. **Address & Methods** – Fill in billing, shipping and payment  
7. **Order Submission** – Confirm and submit order  
8. **Confirmation** – Asserts Order Confirmation Success Message  

---

## 🛠️ Tools & Dependencies

| Component            | Role                   | Version       |
|----------------------|------------------------|---------------|
| **Python**           | Core Language          | 3.11+          |
| **Selenium WebDriver** | Browser Automation     | 4.24.0           |
| **Pytest**           | Test Framework         | Latest        |
| **Allure**           | HTML Test Reporting    | Latest        |
| **ChromeDriver**     | Browser Driver         | Latest        |
| **Logger**           |  Debugging CLI         | Latest        |

---

## 🖥 System Under Test (SUT)
- **Website:** [Demo Web Shop](https://demowebshop.tricentis.com/)
- **Credentials:** A new test user account should be created manually.
- **Browser:** Chrome (ChromeDriver required)

---
## ⚙️ Setup & Installation

### 1. Prerequisites
- Install Python **3.11+** from https://python.org 
- Install Google Chrome 
- Download and Extract Allure from https://github.com/allure-framework/allure2/releases **Add to PATH in Windows**

### 2. Clone Repository
```bash
git clone <repository_url>
``` 

### 3. Create and Activate Virtual Environment 
It is best practice to isolate project dependencies 
```bash 
# Create Environment 
python -m venv venv 

# Activate environment (Windows) [Gitbash]: 
source venv/Scripts/activate 

# Activate environment (MacOS / Linux): 
source venv/bin/activate 
``` 
### 4. Install Dependencies 
All required Python libraries are listed in `requirements.txt`.
```bash 
pip install -r requirements.txt 
```
## ▶️ Execution 
### Run the Test 
Execute the main checkout flow using Pytest, generating Allure report, HTML report and Logs files in the process : 

```bash 
# Change Directory to Desired Folder 
cd E2E_Tricentis_Checkout_Automation 

# Run Tests 
pytest tests/main.py 
```
## 📊 Test Reporting 
After execution, serve the generated report files to view the interactive dashboard. 
```bash 
# Serve Allure Report locally in your browser 
allure serve reports/allure-results
```
--- 
## 📂 Project Structure 
```plaintext
ADREM_TECH_ASSESSMENT/
├── E2E_Tricentis_Checkout_Automation/
│   ├── pages/ 
│   │   ├── __init__.py
│   │   ├── tricentis_cart_summary_page.py
│   │   ├── tricentis_checkout_page.py
│   │   ├── tricentis_home_page.py
│   │   ├── tricentis_login_page.py
│   │   ├── tricentis_order_completion_page.py
│   │   ├── tricentis_search_add_multiple_products_page.py
│   │   ├── tricentis_shipping_billing_address_page.py
│   │   ├── tricentis_submit_order_page.py
│   ├── reports/
│   │   ├── allure/
│   │   ├── assets/
│   │   ├── pytest_logs.txt
│   │   ├── report.html
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── main.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── driver_factory.py
│   │   ├── json_reader.py
│   ├── order_confirmation.png
│   ├── test_data.json
├── __init__.py
├── .gitignore
├── pytest.ini
├── README.md
├── requirements.txt
```
## 📌 Assumptions & Considerations 
- **Credentials :** Assumes the user in `test_data.json` is **already registered** with newly created credentials on Demo Web Shop manually.
- **Data Integrity :** Assumes product names and associated IDs/XPaths in `test_data.json` are current and accurate for SUT. 


