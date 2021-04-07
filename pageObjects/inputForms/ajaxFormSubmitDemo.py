from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class AjaxFormSubmitDemo:
    __name = (By.CSS_SELECTOR, "input#title")
    __comment = (By.CSS_SELECTOR, "textarea#description")
    __submitButton = (By.CSS_SELECTOR, "input#btn-submit")

    def __init__(self, driver):
        self.driver = driver

    def addName(self, name=None):
        e = self.driver.find_element(*self.__name)
        ActionChains(self.driver).move_to_element(e).move_by_offset(2, 2).click().send_keys(name).pause(0.3).perform()
        return self

    def addComment(self, comment=None):
        e = self.driver.find_element(*self.__comment)
        ActionChains(self.driver).move_to_element(e).click().send_keys(comment).pause(0.3).perform()
        return self

    def clickSubmit(self):
        e = self.driver.find_element(*self.__submitButton)
        ActionChains(self.driver).move_to_element(e).click().pause(0.3).perform()
        return self
