from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasicCheckboxDemo:
    __singleCheckBox = (By.CSS_SELECTOR, "input#isAgeSelected")
    __singleCheckBoxMessage = (By.CSS_SELECTOR, "div#txtAge")
    __options = (By.CSS_SELECTOR, "input.cb1-element")
    __checkButton = (By.CSS_SELECTOR, "input#check1")

    def __init__(self, driver):
        self.driver = driver

    def clickSingleCheckBox(self):
        e = self.driver.find_element(*self.__singleCheckBox)
        ActionChains(self.driver).move_to_element(e).move_by_offset(1,1).click().pause(0.3).perform()
        return self

    def checkSingleMessage(self):
        e = self.driver.find_element(*self.__singleCheckBoxMessage)
        if e.is_displayed():
            print(e.text)
        else:
            print("Not checked")
        return self

    def clickOption(self, option=0):
        el = self.driver.find_elements(*self.__options)
        self.driver.execute_script("arguments[0].scrollIntoView();", el[0])
        if option == 'all':
            for e in el:
                WebDriverWait(self.driver,10).until(EC.visibility_of(e))
                ActionChains(self.driver).move_to_element(e).click().perform()
        else:
            el[option].click()
        return self

    def checkAllButton(self):
        e = self.driver.find_element(*self.__checkButton)
        if e.get_attribute("value") == 'Check All':
            ActionChains(self.driver).move_to_element(e).click().pause(0.3).perform()
        return self

    def uncheckAllButton(self):
        e = self.driver.find_element(*self.__checkButton)
        if e.get_attribute("value") == 'Uncheck All':
            ActionChains(self.driver).move_to_element(e).click().pause(0.3).perform()
        return self
