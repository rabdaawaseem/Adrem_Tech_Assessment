<!-- Banner -->
<p align="center">
  <img src="https://via.placeholder.com/1200x250.png?text=🚀+E-Commerce+Checkout+Automation+Framework" alt="E-Commerce Checkout Automation Banner"/>
</p>

<!-- Badges -->
<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white" alt="Python"/></a>
  <a href="https://www.selenium.dev/"><img src="https://img.shields.io/badge/Selenium-4.x-brightgreen?logo=selenium&logoColor=white" alt="Selenium"/></a>
  <a href="https://docs.pytest.org/"><img src="https://img.shields.io/badge/Pytest-Framework-orange?logo=pytest" alt="Pytest"/></a>
  <a href="https://docs.qameta.io/allure/"><img src="https://img.shields.io/badge/Allure-Reports-purple?logo=allure&logoColor=white" alt="Allure"/></a>
  <a href="https://github.com/features/actions"><img src="https://img.shields.io/badge/GitHub-Actions-black?logo=githubactions&logoColor=white" alt="GitHub Actions"/></a>
</p>

---

#  E-Commerce Checkout Automation Framework  
🛒 **End-to-End Test Automation for Tricentis Demo Web Shop**

This project implements a robust, maintainable, and highly readable **end-to-end test automation solution** for the **Tricentis Demo Web Shop checkout process**.

---

## 🛠 Tech Stack

- **Language:** Python 3.9+  
- **Automation:** Selenium WebDriver 4.x  
- **Framework:** Pytest  
- **Reporting:** Allure Reports  
- **Driver:** ChromeDriver (latest compatible)  

---

## 📊 Quality & Reporting

- ✅ Allure HTML Reports with Screenshots  
- ✅ Python Logging for detailed execution traces  
- ✅ Assertions for critical checkpoints  

---

## ✨ Project Overview & Architecture

This framework is built on the **Page Object Model (POM)** design pattern, ensuring **maintainability, readability, and reusability**.  

**Key Features:**
- 🏗️ **Page Object Model (POM):** All web interactions encapsulated in `/pages`  
- 🔄 **Robust Synchronization:** Explicit waits handle dynamic elements  
- 🔒 **Data Management:** Test data managed in `test_data.json` via `JsonReader`  
- 📢 **Observability:** Comprehensive Python logging  
- 📸 **Error Handling:** Automatic screenshots on failure attached to Allure  
- ✅ **Assertions:** Built-in test validation points  

---

## 🎯 Objective: The E2E Checkout Flow

### Test Scenario (`tests/main.py`):
1. **Login** – Authenticate with newly created credentials drom external json file source 
2. **Homepage Addition** – Add a product from main page  
3. **Search & Add** – Add multiple products from `test_data.json`  
4. **Cart Validation** – Validate items + total price  
5. **Checkout Initiation** – Start checkout after ToS agreement  
6. **Address & Methods** – Fill in billing, shipping, and payment  
7. **Order Submission** – Confirm and submit order  
8. **Confirmation** – Asserts Order Confirmation Success Message  

---

## 🛠️ Tools & Dependencies

| Component            | Role                   | Version       |
|----------------------|------------------------|---------------|
| **Python**           | Core Language          | 3.10+          |
| **Selenium WebDriver** | Browser Automation     | 4.x           |
| **Pytest**           | Test Framework         | Latest        |
| **Allure**           | HTML Test Reporting    | Latest        |
| **ChromeDriver**     | Browser Driver         | Latest        |

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- Install Python **3.10+**  
- Install Google Chrome  

### 2. Clone Repository
```bash
git clone <repository_url>
cd End_to_End_Checkout_Automation
