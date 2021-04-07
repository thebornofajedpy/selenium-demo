from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BootstrapDatePicker:
    __date = (By.CSS_SELECTOR, 'div.input-group.date > input.form-control')
    __today = (By.CSS_SELECTOR, 'div.datepicker-days > table.table-condensed > tfoot >tr > th.today')
    __clear = (By.CSS_SELECTOR, "div.datepicker-days > table.table-condensed > tfoot >tr > th.clear")
    __startDate = (By.CSS_SELECTOR, "div#datepicker > input[placeholder='Start date']")
    __endDate = (By.CSS_SELECTOR, "div#datepicker > input[placeholder='End date']")

    def __init__(self, driver):
        self.driver = driver

    def typeDate(self,date):
        e = self.driver.find_element(*self.__date)
        ActionChains(self.driver).move_to_element(e).move_by_offset(2,2).click().pause(0.3)\
            .send_keys(date).pause(0.3).perform()
        return self

    def today(self):
        e = self.driver.find_element(*self.__date)
        ActionChains(self.driver).move_to_element(e).move_by_offset(2, 2).click().perform()
        t = self.driver.find_element(*self.__today)
        ActionChains(self.driver).move_to_element(t).click().pause(0.3).perform()
        return self

    def clear(self):
        e = self.driver.find_element(*self.__date)
        ActionChains(self.driver).move_to_element(e).move_by_offset(2, 2).click().perform()
        c = self.driver.find_element(*self.__clear)
        ActionChains(self.driver).move_to_element(c).click().pause(0.3).perform()
        return self

    def dateRange(self,start,end):
        s = self.driver.find_element(*self.__startDate)
        ActionChains(self.driver).move_to_element(s).move_by_offset(2, 2).click().send_keys(start).perform()
        e = self.driver.find_element(*self.__endDate)
        ActionChains(self.driver).move_to_element(e).click().send_keys(end).pause(0.3).perform()
        return self
