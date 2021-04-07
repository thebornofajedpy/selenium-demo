from selenium.webdriver.common.by import By
from pageObjects.datePickers.bootstrapDatePickerDemo import BootstrapDatePicker
from pageObjects.datePickers.jqueryDatePickerDemo import JqueryDatePicker
from pageObjects.inputForms.basicFirstFormDemo import BasicFirstFormDemo
from pageObjects.inputForms.basicCheckboxDemo import BasicCheckboxDemo
from pageObjects.inputForms.basicRadioButtonDemo import BasicRadioButtonDemo
from pageObjects.inputForms.basicSelectDropdownDemo import BasicSelectDropdownDemo
from pageObjects.inputForms.inputFormDemo import InputFormDemo
from pageObjects.inputForms.ajaxFormSubmitDemo import AjaxFormSubmitDemo
from pageObjects.inputForms.jqueryDropdownSearchDemo import JqueryDropdownSearchDemo
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def treeSelector(driver,locator):
    e = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
    driver.execute_script("arguments[0].scrollIntoView();", e)
    ActionChains(driver).move_to_element(e).click().perform()


class InputForms:
    imputForms = (By.XPATH, "//li[@class='tree-branch']/a[contains(text(),'Input Forms')]")
    simpleForm = (By.XPATH, "//li[@class='tree-branch']/ul/li/a[contains(text(),'Simple Form Demo')]")
    checkBox = (By.XPATH, "//li[@class='tree-branch']/ul/li/a[contains(text(),'Checkbox Demo')]")
    radioButtons = (By.XPATH, "//li[@class='tree-branch']/ul/li/a[contains(text(),'Radio Buttons Demo')]")
    selectDropdownList = (By.XPATH, "//li[@class='tree-branch']/ul/li/a[contains(text(),'Select Dropdown List')]")
    inputFormSubmit = (By.XPATH, "//li[@class='tree-branch']/ul/li/a[contains(text(),'Input Form Submit')]")
    ajaxFormSubmit = (By.XPATH, "//li[@class='tree-branch']/ul/li/a[contains(text(),'Ajax Form Submit')]")
    jquerySelectDropdown = (By.XPATH, "//li[@class='tree-branch']/ul/li/a[contains(text(),'JQuery Select dropdown')]")

    @classmethod
    def clickInputForms(cls, driver):
        treeSelector(driver,cls.imputForms)
        return cls

    @classmethod
    def clickSimpleFormDemo(cls, driver):
        treeSelector(driver, cls.simpleForm)
        return BasicFirstFormDemo(driver)

    @classmethod
    def clickCheckBoxDemo(cls, driver):
        treeSelector(driver,cls.checkBox)
        return BasicCheckboxDemo(driver)

    @classmethod
    def clickRadioButtonsDemo(cls, driver):
        treeSelector(driver,cls.radioButtons)
        return BasicRadioButtonDemo(driver)

    @classmethod
    def clickDropdownListDemo(cls, driver):
        treeSelector(driver,cls.selectDropdownList)
        return BasicSelectDropdownDemo(driver)

    @classmethod
    def clickInputFormSubmitDemo(cls, driver):
        treeSelector(driver,cls.inputFormSubmit)
        return InputFormDemo(driver)

    @classmethod
    def clickAjaxFormSubmitDemo(cls, driver):
        treeSelector(driver,cls.ajaxFormSubmit)
        return AjaxFormSubmitDemo(driver)

    @classmethod
    def clickJquerySelectDropdownDemo(cls, driver):
        treeSelector(driver,cls.jquerySelectDropdown)
        return JqueryDropdownSearchDemo(driver)


class DatePickers:
    datePicker = (By.XPATH, "//li[@class='tree-branch']/a[contains(text(),'Date pickers')]")
    bootstrapDate = (By.XPATH, "//li[@class='tree-branch']/ul/li/a[contains(text(),'Bootstrap Date Picker')]")
    jqueryDate = (By.XPATH, "//li[@class='tree-branch']/ul/li/a[contains(text(),'JQuery Date Picker')]")

    @classmethod
    def clickDatePickers(cls, driver):
        time.sleep(1)
        treeSelector(driver,cls.datePicker)
        return cls

    @classmethod
    def clickBootstrapDate(cls, driver):
        treeSelector(driver, cls.bootstrapDate)
        return BootstrapDatePicker(driver)

    @classmethod
    def clickJqueryDate(cls, driver):
        treeSelector(driver, cls.jqueryDate)
        return JqueryDatePicker(driver)



