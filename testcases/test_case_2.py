import pytest
from pages.demoqa_index_page import DemoqaIndex


@pytest.mark.usefixtures("setup")
# @ddt
class TestSearchAndVerifyFilter():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.indexPage = DemoqaIndex(self.driver)

    # @unpack
    # def test_search_flights_1_stop(self, goingfrom, goingto, date, stops):
    #     search_flight_result = self.lp.searchFlights(goingfrom, goingto, date)
    #     self.lp.page_scroll()
    #     search_flight_result.filter_flights_by_stop(stops)
    #     allstops1 = search_flight_result.get_search_flight_results()
    #     self.log.info(len(allstops1))
    #     self.ut.assertListItemText(allstops1, stops)
    def test_click_login_button(self):
        self.indexPage.clickLoginButton()

    def test_click_element_menu(self):
        self.indexPage.clickElementsMenu()


