from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class JqueryDatePicker:
    __from = (By.CSS_SELECTOR, 'input#from')
    __to = (By.CSS_SELECTOR, 'input#to')

    def __init__(self, driver):
        self.driver = driver

    def typeDatefrom(self, date):
        e = self.driver.find_element(*self.__from)
        ActionChains(self.driver).move_to_element(e).move_by_offset(2, 2).click().pause(0.3) \
            .send_keys(date).pause(0.3).perform()
        return self

    def typeDateTo(self, date):
        e = self.driver.find_element(*self.__to)
        ActionChains(self.driver).move_to_element(e).move_by_offset(2, 2).click().send_keys(date).pause(0.3).perform()
        return self
