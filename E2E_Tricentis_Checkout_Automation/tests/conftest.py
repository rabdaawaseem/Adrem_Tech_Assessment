# conftest.py (updated)
import json
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import allure
import os

@pytest.fixture(scope="session")
def test_data():
    with open("data/test_data.json") as f:
        return json.load(f)

@pytest.fixture(scope="class")
def driver():
    options = Options()
    #options.add_argument("--headless")  # UnComment for invisible browser (headless browser)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, driver):
    yield
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        try:
            project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
            screenshot_dir = os.path.join(project_root, 'reports', 'screenshots')
            os.makedirs(screenshot_dir, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}_{timestamp}.png")
            driver.save_screenshot(screenshot_path)
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot on failure", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            pass  # Silent fail if screenshot can't be taken