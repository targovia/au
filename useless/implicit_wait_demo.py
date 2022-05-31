from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Demo():
    def test_login(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://login.salesforce.com/")
        # driver.implicitly_wait(10)
        driver.implicitly_wait()
        driver.find_element(By.XPATH, "//input[@id='username22']").send_keys("babangida")

iml = Demo()
iml.test_login()