from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class BasicSelectDropdownDemo:
    __dayListDropdown = (By.CSS_SELECTOR, "select#select-demo")
    __stateList = (By.CSS_SELECTOR, "select#multi-select")
    __california = (By.XPATH, "//select[@id='multi-select']//option[@value='California']")
    __florida = (By.XPATH, "//select[@id='multi-select']//option[@value='Florida']")
    __newJersey = (By.XPATH, "//select[@id='multi-select']//option[@value='New Jersey']")
    __newYork = (By.XPATH, "//select[@id='multi-select']//option[@value='New York']")
    __ohio = (By.XPATH, "//select[@id='multi-select']//option[@value='Ohio']")
    __texas = (By.XPATH, "//select[@id='multi-select']//option[@value='Texas']")
    __pennsylvania = (By.XPATH, "//select[@id='multi-select']//option[@value='Pennsylvania']")
    __washington = (By.XPATH, "//select[@id='multi-select']//option[@value='Washington']")
    __firstSelectedButton = (By.CSS_SELECTOR, "button#printMe")
    __allSelectedButton = (By.CSS_SELECTOR, "button#printAll")

    def __init__(self, driver):
        self.driver = driver

    def selectDayFromDropdown(self, day):
        menu = Select(self.driver.find_element(*self.__dayListDropdown))
        menu.select_by_value(value=day)
        return self

    def selectStateFromList(self, states):
        el = self.driver.find_element(By.CSS_SELECTOR, "select#multi-select")
        self.driver.execute_script("arguments[0].scrollIntoView();", el)

        california = self.driver.find_element(*self.__california)
        new_jersey = self.driver.find_element(*self.__newJersey)
        new_york = self.driver.find_element(*self.__newYork)
        ohio = self.driver.find_element(*self.__ohio)
        texas = self.driver.find_element(*self.__texas)
        florida = self.driver.find_element(*self.__florida)
        pennsylvania = self.driver.find_element(*self.__pennsylvania)
        washington = self.driver.find_element(*self.__washington)

        mapper = {'California': california, 'New Jersey': new_jersey, 'New York': new_york,
                  'Ohio': ohio, 'Texas': texas, 'Florida': florida, 'Pennsylvania': pennsylvania,
                  'Washington': washington}

        chain = ActionChains(self.driver).key_down(Keys.CONTROL)
        for s in states:
            chain.click(mapper[s])
        chain.key_up(Keys.CONTROL).perform()
        return self

    def clickFirstSelectedButton(self):
        e = self.driver.find_element(*self.__firstSelectedButton)
        self.driver.execute_script("arguments[0].scrollIntoView();", e)
        ActionChains(self.driver).move_to_element(e).click().pause(0.3).perform()
        return self

    def clickAllSelectedButton(self):
        e = self.driver.find_element(*self.__allSelectedButton)
        self.driver.execute_script("arguments[0].scrollIntoView();", e)
        ActionChains(self.driver).move_to_element(e).click().pause(0.3).perform()

        return self
