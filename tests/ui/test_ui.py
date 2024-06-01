import page_object.page as page
from page_object.locators import MainPageLocators

class TestAppUI:
    def test_app_title_matches(self, browser):
        main_page = page.MainPage(browser)

        assert main_page.is_title_matches()

    def test_app_main_page_has_textaream(self, browser):
        main_page = page.MainPage(browser)

        assert main_page.driver.find_element(*MainPageLocators.TEXTAREAM)

    def test_app_main_page_has_textarean(self, browser):
        main_page = page.MainPage(browser)

        assert main_page.driver.find_element(*MainPageLocators.TEXTAREAN)

    def test_app_main_page_has_submit_button(self, browser):
        main_page = page.MainPage(browser)

        assert main_page.driver.find_element(*MainPageLocators.SEND_BUTTON)

    def test_app_result_is_not_empty_if_data(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data(4, 5)
        main_page.click_send_button()

        result_page = page.ResutlsPage(browser)
        assert result_page.is_results_found()


    def test_app_result_is_unique_paths(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data(4, 5)
        main_page.click_send_button()

        result_page = page.ResutlsPage(browser)

        result = result_page.get_result()

        assert result == '{\n  "result": 35\n}'

    def test_app_error_if_non_integer(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data('sdf', 'cx')
        main_page.click_send_button()
        error_page = page.ErrorPage(browser)

        assert error_page.is_title_matches("400 Bad Request")

    def test_app_error_if_big_answer(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data(80, 80)
        main_page.click_send_button()
        error_page = page.ErrorPage(browser)

        assert error_page.is_title_matches("400 Bad Request")

