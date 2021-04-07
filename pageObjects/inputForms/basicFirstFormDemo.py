from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasicFirstFormDemo:
    __enterMessageInput = (By.CSS_SELECTOR, "input#user-message")
    __showMessageButton = (By.XPATH, "//button[contains(text(),'Show Message')]")
    __enterValueA = (By.CSS_SELECTOR, "input#sum1")
    __enterValueB = (By.CSS_SELECTOR, "input#sum2")
    __totalButton = (By.XPATH, "//button[contains(text(),'Get Total')]")

    def __init__(self, driver):
        self.driver = driver

    def setMessageAndClick(self, message):
        e = self.driver.find_element(*self.__enterMessageInput)
        b = self.driver.find_element(*self.__showMessageButton)
        ActionChains(self.driver).move_to_element(e).click().send_keys(message).pause(1).perform()
        ActionChains(self.driver).move_to_element(b).click().pause(1).perform()

        return self

    def setValuesAndClick(self, val1, val2):
        e = self.driver.find_element(*self.__enterValueA)
        v = self.driver.find_element(*self.__enterValueB)
        b = self.driver.find_element(*self.__totalButton)
        self.driver.execute_script("arguments[0].scrollIntoView();", e)
        ActionChains(self.driver).move_to_element(e).click().send_keys(val1).pause(0.3).perform()
        ActionChains(self.driver).move_to_element(v).click().send_keys(val2).pause(0.3).perform()
        ActionChains(self.driver).move_to_element(b).click().pause(0.3).perform()
        return self
