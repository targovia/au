import pytest
from pages.demoqa_index_page import DemoqaIndex
from pages.login_page import LoginPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
# @ddt
class TestSearchAndVerifyFilter():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.indexPage = DemoqaIndex(self.driver)
        self.loginPage = LoginPage(self.driver)

    # @unpack
    # def test_search_flights_1_stop(self, goingfrom, goingto, date, stops):
    #     search_flight_result = self.lp.searchFlights(goingfrom, goingto, date)
    #     self.lp.page_scroll()
    #     search_flight_result.filter_flights_by_stop(stops)
    #     allstops1 = search_flight_result.get_search_flight_results()
    #     self.log.info(len(allstops1))
    #     self.ut.assertListItemText(allstops1, stops)
    def test_click_login_button(self):
        self.indexPage.clickLoginBtn()

    def test_click_login_buttons_repeat(self):
        self.indexPage.getSearchClickIn()

    def test_send_text_to_input_search(self):
        self.indexPage.sendTextSearchField("6666666666666666666666666")

    def test_test_test(self):
        self.indexPage.sendTextSearchField("pasta za zabi")

    def test_random_login_procedure(self):
        self.indexPage.getElementsMenu()
        self.indexPage.clickElMnu()

    def test_integaration_books_login(self):
        self.indexPage.clickLoginBtn()
        self.loginPage.clickLoginBtn()
        self.loginPage.sendDummyUserName("pastir")
        self.loginPage.getPassInput().click()
        self.loginPage.sendDummyPass("past244")
        self.loginPage.clickLoginBtn()
        # assert self.loginPage.getErrMsgField() == "Invalid username or password!"

    def test_sending_direct(self):
        self.indexPage.sendingSearchClickIn(123)

    def test_PrintErr(self):
        print("MISSSSSSSSSSKA - Print from Print function inside the test")
        # self.printError()
        ut = Utils()
        ut.printError()
