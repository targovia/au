import pytest
from pages.demoqa_index_page import DemoqaIndex


@pytest.mark.usefixtures("setup")
# @ddt
class TestSearchAndVerifyFilter():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.indexPage = DemoqaIndex(self.driver)

    def test_click_login_button(self):
        self.indexPage.clickLoginButton()

    def test_click_login_button(self):
        self.indexPage.ELEMENTS_MENU



