from selenium.webdriver.common.by import By

class MainPageLocators(object):
    TEXTAREAM = (By.NAME, 'm')
    TEXTAREAN = (By.NAME, 'n')
    SEND_BUTTON = (By.ID, 'go')

class ResutlsPageLocators(object):
    RESULT = (By.TAG_NAME, 'pre')