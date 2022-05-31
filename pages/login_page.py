import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver


class LoginPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators https://demoqa.com/login
    LOGIN_BTN_INSIDE = "//button[@id='login']"
    NEW_USER_BTN = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]"
    USER_INPUT = "//input[@id='userName']"
    PASSWORD_INPUT = "//input[@id='userName']"
    ERR_MSG_FIELD = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[5]/div[1]/p[1]"



    def getLoginButtonInside(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LOGIN_BTN_INSIDE)

    def clickLoginBtn(self):
        self.getLoginButtonInside().click()

    def getUserInput(self):
        return self.driver.find_element(By.XPATH, self.USER_INPUT)

    def sendDummyUserName(self, dummy_user):
        self.getUserInput().send_keys(dummy_user)

    def getPassInput(self):
        return self.driver.find_element(By.XPATH, self.PASSWORD_INPUT)

    def sendDummyPass(self, dummy_pass_string):
        self.getPassInput().send_keys(dummy_pass_string)

    def getErrMsgField(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ERR_MSG_FIELD).to_text()






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
    #
    # def searchFlights(self, departlocation, goingtolocation, departuredate):
    #     self.enterDepartFromLocation(departlocation)
    #     self.enterGoingToLocation(goingtolocation)
    #     self.enterDepartureDate(departuredate)
    #     self.clickSearchFlightsButton()
    #     search_flights_result = SearchFlightResults(self.driver)
    #     return search_flights_result


    #####################################################################################################

    # Locators
    # DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    # GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    # GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    # SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    # ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    # SEARCH_BUTTON = "//input[@value='Search Flights']"
    #
    # def getDepartFromField(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)
    #
    # def getGoingToField(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)
    #
    # def getGoingToResults(self):
    #     return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)
    #
    # def getDepatureDateField(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)
    #
    # def getAllDatesField(self):
    #     return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)
    #
    # def getSearchButton(self):
    #     return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)
    #
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
    #
    # def searchFlights(self, departlocation, goingtolocation, departuredate):
    #     self.enterDepartFromLocation(departlocation)
    #     self.enterGoingToLocation(goingtolocation)
    #     self.enterDepartureDate(departuredate)
    #     self.clickSearchFlightsButton()
    #     search_flights_result = SearchFlightResults(self.driver)
    #     return search_flights_result
