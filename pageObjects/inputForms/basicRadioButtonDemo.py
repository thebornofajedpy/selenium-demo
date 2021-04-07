from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasicRadioButtonDemo:
    __maleButton = (By.CSS_SELECTOR, "input[name='optradio'][value='Male']")
    __femaleButton = (By.CSS_SELECTOR, "input[name='optradio'][value='Female']")
    __checkedValue = (By.CSS_SELECTOR, "button#buttoncheck")
    __groupMaleButton = (By.CSS_SELECTOR, "input[name='gender'][value='Male']")
    __groupFemaleButton = (By.CSS_SELECTOR, "input[name='gender'][value='Female']")
    __groupZeroFive = (By.CSS_SELECTOR, "input[name='ageGroup'][value='0 - 5']")
    __groupFiveFifteen = (By.CSS_SELECTOR, "input[name='ageGroup'][value='5 - 15']")
    __groupFifteenFifty = (By.CSS_SELECTOR, "input[name='ageGroup'][value='15 - 50']")
    __groupValues = (By.XPATH, "//button[contains(text(),'Get values')]")

    def __init__(self, driver):
        self.driver = driver

    def clickMaleButton(self):
        e = self.driver.find_element(*self.__maleButton)
        ActionChains(self.driver).move_to_element(e).pause(1).click().perform()
        return self

    def clickFemaleButton(self):
        e = self.driver.find_element(*self.__femaleButton)
        ActionChains(self.driver).move_to_element(e).pause(1).click().perform()
        return self

    def clickCheckedValueButton(self):
        e = self.driver.find_element(*self.__checkedValue)
        ActionChains(self.driver).move_to_element(e).pause(1).click().perform()
        return self

    def clickGroupMaleButton(self):
        e = self.driver.find_element(*self.__groupMaleButton)
        ActionChains(self.driver).move_to_element(e).pause(1).click().perform()
        return self

    def clickGroupFemaleButton(self):
        e = self.driver.find_element(*self.__groupFemaleButton)
        self.driver.execute_script("arguments[0].scrollIntoView();", e)
        e.click()
        return self

    def clickGroupZeroFive(self):
        self.driver.find_element(*self.__groupZeroFive).click()
        return self

    def clickGroupFiveFifteen(self):
        self.driver.find_element(*self.__groupFiveFifteen).click()
        return self

    def clickGroupFifteenFifty(self):
        self.driver.find_element(*self.__groupFifteenFifty).click()
        return self

    def clickGroupValues(self):
        e = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.__groupValues))
        self.driver.execute_script("arguments[0].scrollIntoView();", e)
        ActionChains(self.driver).move_to_element(e).pause(1).click().pause(1).perform()
        return self
