
import pytest
import os
import pytest_html
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config.settings import Settings
from datetime import datetime


# This belwow parser is used to add custom command line options. It is adding a new command line option --browser to the pytest command.
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser type (chrome, firefox, edge)")

@pytest.fixture
def browser(request):
    browser_type = request.config.getoption("--browser").lower()
    Settings.BROWSER = browser_type

    if browser_type == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_type == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_type == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Browser {browser_type} is not supported")

    driver.maximize_window()

    driver.implicitly_wait(Settings.TIMEOUT)
    yield driver
    driver.quit()

def pytest_html_report_title(report):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report.title = f"WMAE Automation Report - {now}"


# pytest hook to add env information to report
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"Browser: {Settings.BROWSER}", f"Environment: {Settings.ENVIRONMENT}"])

def pytest_html_results_table_header(cells):
    cells.insert(1, "Browser")
    cells.insert(2, "Environment")

def pytest_html_results_table_row(report, cells):
    cells.insert(1, Settings.BROWSER)
    cells.insert(2, Settings.ENVIRONMENT)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()




# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == "call" and report.failed:
#         try:
#             driver = item.funcargs['browser']
#             screenshot_path = f"reports/screenshots/{item.nodeid.replace('::', '_')}.png"
#             driver.get_screenshot_as_file(screenshot_path)
#             extra = getattr(report, 'extra', [])
#             extra.append(extras.image(screenshot_path))
#             report.extra = extra
#         except Exception as e:
#             print(f"Failed to take screenshot: {e}")

