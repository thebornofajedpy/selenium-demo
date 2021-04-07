from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class JqueryDropdownSearchDemo:
    __country = (By.CSS_SELECTOR, 'select#country')
    __searchBox = (By.CSS_SELECTOR, 'input.select2-search__field')
    __state = (By.CSS_SELECTOR, "input.select2-search__field")
    __territories = (By.CSS_SELECTOR, "select.js-example-disabled-results.select2-hidden-accessible")
    __file = (By.CSS_SELECTOR, "select#files")

    def __init__(self, driver):
        self.driver = driver

    def selectCountry(self, country='Australia', search=False):
        if search:
            ActionChains(self.driver).move_to_element(self.driver.find_element(*self.__country)) \
                .move_by_offset(2, 2).click().send_keys(country).send_keys(Keys.ENTER).pause(0.3).perform()
        else:
            s = Select(self.driver.find_element(*self.__country))
            try:
                s.select_by_visible_text(country)
            except Exception as e:
                print(e)
        return self

    def selectMultipleValues(self, states):
        try:
            for state in states:
                ActionChains(self.driver).move_to_element(self.driver.find_element(*self.__state)) \
                    .move_by_offset(2, 2).click().send_keys(state).send_keys(Keys.ENTER).pause(0.3).perform()
        except Exception as e:
            print(e)
        return self

    def selectTerritories(self, territory='Puerto Rico'):
        try:
            e = self.driver.find_element(*self.__territories)
            self.driver.execute_script("arguments[0].scrollIntoView();", e)
            ActionChains(self.driver).move_to_element(e) \
                .move_by_offset(2, 2).click().send_keys(territory).send_keys(Keys.ENTER).pause(0.3).perform()
        except Exception as e:
            print(e)
        return self

    def selectFile(self, file='Java'):
        try:
            e = self.driver.find_element(*self.__file)
            self.driver.execute_script("arguments[0].scrollIntoView();", e)
            ActionChains(self.driver).move_to_element(e) \
                .move_by_offset(2, 2).click().send_keys(file).send_keys(Keys.ENTER).pause(0.3).perform()
        except Exception as e:
            print(e)
        return self
