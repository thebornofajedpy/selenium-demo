from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class InputFormDemo:
    __firstName = (By.CSS_SELECTOR, "input[name=first_name]")
    __lastName = (By.CSS_SELECTOR, "input[name=last_name]")
    __email = (By.CSS_SELECTOR, "input[name=email]")
    __phone = (By.CSS_SELECTOR, "input[name=phone]")
    __address = (By.CSS_SELECTOR, "input[name=address]")
    __city = (By.CSS_SELECTOR, "input[name=city]")
    __state = (By.CSS_SELECTOR, "select[name=state]")
    __zipcode = (By.CSS_SELECTOR, "input[name=zip]")
    __website = (By.CSS_SELECTOR, "input[name=website]")
    __hostingYes = (By.CSS_SELECTOR, "input[value=yes]")
    __hostingNo = (By.CSS_SELECTOR, "input[value=no]")
    __comment = (By.CSS_SELECTOR, "textarea[name=comment]")
    __sendButton = (By.XPATH, "//button[contains(text(),'Send')]")

    def __init__(self, driver):
        self.driver = driver

    def addName(self, name=None):
        e = self.driver.find_element(*self.__firstName)
        # e = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__firstName))
        ActionChains(self.driver).move_to_element(e).move_by_offset(1, 1).click().send_keys(name).perform()
        return self

    def addLastName(self, last=None):
        e = self.driver.find_element(*self.__lastName)
        # e = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__lastName))
        ActionChains(self.driver).move_to_element(e).move_by_offset(1, 1).click().send_keys(last).perform()
        return self

    def addEmail(self, mail=None):
        self.driver.find_element(*self.__email).send_keys(mail)
        return self

    def addPhone(self, phone=None):
        self.driver.find_element(*self.__phone).send_keys(phone)
        return self

    def addAddress(self, address=None):
        self.driver.find_element(*self.__address).send_keys(address)
        return self

    def addCity(self, city=None):
        self.driver.find_element(*self.__city).send_keys(city)
        return self

    def addZipcode(self, zipcode=None):
        self.driver.find_element(*self.__zipcode).send_keys(zipcode)
        return self

    def addWebsite(self, web=None):
        self.driver.find_element(*self.__website).send_keys(web)
        return self

    def addComment(self, comment=None):
        self.driver.find_element(*self.__comment).send_keys(comment)
        return self

    def clickHostingYes(self):
        self.driver.find_element(*self.__hostingYes).click()
        return self

    def clickHostingNo(self):
        self.driver.find_element(*self.__hostingNo).click()
        return self

    def selectState(self):
        e = self.driver.find_element(*self.__state)
        self.driver.execute_script("arguments[0].scrollIntoView();", e)
        menu = Select(e)
        menu.select_by_visible_text("Alabama")
        return self

    def clickSend(self):
        e = self.driver.find_element(*self.__sendButton)
        ActionChains(self.driver).move_to_element(e).click().pause(0.3).perform()
        return self
