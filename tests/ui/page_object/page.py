from .locators import MainPageLocators, ResutlsPageLocators

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def is_title_matches(self):
        return "Demo" == self.driver.title

    def fill_data(self, m, n):
        element1 = self.driver.find_element(*MainPageLocators.TEXTAREAM)
        element2 = self.driver.find_element(*MainPageLocators.TEXTAREAN)
        element1.send_keys(m)
        element2.send_keys(n)

    def click_send_button(self):
        element = self.driver.find_element(*MainPageLocators.SEND_BUTTON)
        element.click()

class ResutlsPage(BasePage):
    def is_results_found(self):
        return "Bad Request" not in self.driver.page_source

    def get_result(self):
        result = self.driver.find_element(*ResutlsPageLocators.RESULT)
        return result.text

class ErrorPage(BasePage):
    def is_title_matches(self, title):
        return title == self.driver.title