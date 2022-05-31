from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElemenById():
    def find_element_Id_milen(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://demoqa.com/accordian")
        # driver.find_element_by_xpath("//div[@id='section1Heading']").click()
        # driver.find_element(By.XPATH, "//div[@id='section1Heading']").click()
        # l = driver.find_elements(By.XPATH, "//div[@id='section1Heading']")
        l = driver.find_elements(By.TAG_NAME, "div")
        print(len(l))
        assert len(l) == 79
        print(type(l))
        for i in l:
            print(i.text)
        print(driver.title)
        assert "ToolsQA" in driver.title
        # time.sleep(20)
        # assert "Nema" in driver.page_source

find = DemoFindElemenById()
find.find_element_Id_milen()