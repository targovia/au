import pytest
import softest
from ddt import ddt, data,  unpack
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils()

    # @file_data("../testdata/testdata.json")
    # @file_data("../testdata/testyml.yaml")
    # @data(*Utils.read_data_from_excel("C:\\python-selenium\\TestFrameworkDemo\\testdata\\tdataexcel.xlsx", "Sheet1"))
    @data(*Utils.read_data_from_csv("C:\\Users\\mgeorgiev29\\PycharmProjects\\au\\testdata\\tdatacsv.csv"))
    @unpack
    def test_search_flights_1_stop(self, goingfrom, goingto, date, stops):
        search_flight_result = self.lp.searchFlights(goingfrom, goingto, date)
        self.lp.page_scroll()
        search_flight_result.filter_flights_by_stop(stops)
        allstops1 = search_flight_result.get_search_flight_results()
        self.log.info(len(allstops1))
        self.ut.assertListItemText(allstops1, stops)