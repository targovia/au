import pytest
from pages.demoqa_index_page import DemoqaIndex
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
# @ddt
class TestLogin():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.indexPage = DemoqaIndex(self.driver)

    def test_click_login_button(self):
        self.indexPage.clickLoginBtn()

    def test_click_el_menu(self):
        self.indexPage.clickElMnu()





