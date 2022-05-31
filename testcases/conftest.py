import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = None

@pytest.fixture(autouse=True)
def setup(request, browser, url):
    global driver
    if browser == "chrome":
        #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser == "edge":
        #driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")
    parser.addoption("--headless", action="store", default="false", help="Run browser tests in headless mode. Default: false") #https://github.com/arkturix/internet-heroku-aut/blob/master/tests/conftest.py


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="class", autouse=True)
def headless(request):
    if request.config.getoption("--headless") == "false":
        return False
    else:
        return True

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("http://www.rcvacademy.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             file_name = str(int(round(time.time() * 1000))) + ".png"
#             # file_name = report.nodeid.replace("::", "_") + ".png"
#             destinationFile = os.path.join(report_directory, file_name)
#             driver.save_screenshot(destinationFile)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>'%file_name
#             extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
# def pytest_html_report_title(report):
#     report.title = "RCV Academy Automation Report"