import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver


class Herokuapp(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators http://admin:admin@the-internet.herokuapp.com
    ABTESTING = "//a[contains(text(),'A/B Testing')]"
    ADDREMOVEEL = "//a[contains(text(),'Add/Remove Elements')]"
    BROKENIMG = "//a[contains(text(),'Broken Images')]"




    def clickABTestinglink(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ABTESTING).click()

    def clickADDREMOVElink(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ADDREMOVEEL)

    def clickBrokenImg(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BROKENIMG).click()

    # def clickLoginBtn(self):
    #     self.getLoginButton().click()
    #
    # def getElementsMenu(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.ELEMENTS_MENU)
    #
    # def clickElMnu(self):
    #     self.getElementsMenu().click()
    #
    # def getSearchClickIn(self):
    #     return self.driver.find_element(By.XPATH, self.SEARCH_INPUT)
    #
    # def sendTextSearchField(self, test_to_serach):
    #     self.getSearchClickIn().send_keys(test_to_serach)
    #
    # def sendingSearchClickIn(self, str_position):
    #     return self.driver.find_element(By.XPATH, self.SEARCH_INPUT).send_keys(str_position)


    # def clickSearchFlightsButton(self):
    #     self.getSearchButton().click()
    #     time.sleep(4)


    # def enterDepartFromLocation(self, departlocation):
    #     self.getDepartFromField().click()
    #     self.getDepartFromField().send_keys(departlocation)
    #     self.getDepartFromField().send_keys(Keys.ENTER)
    #
    # def enterGoingToLocation(self, goingtolocation):
    #     self.getGoingToField().click()
    #     self.log.info("Clicked on going to")
    #     time.sleep(2)
    #     self.getGoingToField().send_keys(goingtolocation)
    #     self.log.info("Typed text into going to field successfully")
    #     time.sleep(2)
    #     search_results = self.getGoingToResults()
    #     for results in search_results:
    #         if goingtolocation in results.text:
    #             results.click()
    #             break
    #
    # def enterDepartureDate(self, departuredate):
    #     self.getDepatureDateField().click()
    #     all_dates = self.getAllDatesField().find_elements(By.XPATH, self.ALL_DATES)
    #     for date in all_dates:
    #         if date.get_attribute("data-date") == departuredate:
    #             date.click()
    #             break
    #
    # def clickSearchFlightsButton(self):
    #     self.getSearchButton().click()
    #     time.sleep(4)