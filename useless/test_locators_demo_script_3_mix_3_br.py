from datetime import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#class DemoFindElemenById():
def test_find_element_Id_milen():
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://demoqa.com/forms")
        # driver.find_element_by_xpath("//div[@id='section1Heading']").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Practice Form')]").click()
        te = driver.find_element(By.XPATH, "//span[contains(text(),'Practice Form')]").is_enabled()
        # te = driver.find_element(By.XPATH, "//span[contains(text(),'Practice Form')]").screenshot('C:\\Users\\mgeorgiev29\\PycharmProjects\\au\\useless\\f1.png')
        te = driver.find_element(By.XPATH, "//span[contains(text(),'Practice Form')]")
        driver.get_screenshot_as_file(('.\\f2.png'))
        # assert te == False
        # l = driver.find_elements(By.XPATH, "//div[@id='section1Heading']")
        # l = driver.find_elements(By.TAG_NAME, "div")
        t = driver.title
        assert "ToolsQA" == t
        print(t)
        print(te)
        # driver.get_full_page_screenshot_as_file('C:\\Users\\mgeorgiev29\\PycharmProjects\\au\\useless\\f1.png')

def test_test123():
    print("test test text")

url = 'https://demoqa.com/BookStore/v1/Books'

def test_get_employee_details_check_status_code_equals_200():
    response = requests.get(url)
    assert response.status_code == 200

#find = DemoFindElemenById()
#find.test_find_element_Id_milen()