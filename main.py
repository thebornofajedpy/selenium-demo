from pageObjects.menuList import InputForms
from pageObjects.menuList import DatePickers
from selenium.webdriver.common.by import By
from selenium import webdriver
from pathlib import Path
import time


def run():
    p = Path()
    currentPath = p.resolve().joinpath('chromedriver.exe')
    driver = webdriver.Chrome(currentPath)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.seleniumeasy.com/test/')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'a.at-cv-button.at-cv-lightbox-yesno.at-cm-no-button').click()
    time.sleep(2)

    DatePickers.clickDatePickers(driver)\
        .clickBootstrapDate(driver)\
        .today().clear().typeDate('23/3/2020')\
        .dateRange('1/1/2020','1/1/2021')

    DatePickers.clickDatePickers(driver)\
        .clickJqueryDate(driver)\
        .typeDatefrom("1/1/2020")\
        .typeDateTo("2/2/2021")

    InputForms.clickInputForms(driver) \
        .clickSimpleFormDemo(driver) \
        .setMessageAndClick("Hello World") \
        .setValuesAndClick(5, 5)

    InputForms.clickInputForms(driver) \
        .clickCheckBoxDemo(driver) \
        .clickSingleCheckBox() \
        .checkSingleMessage() \
        .clickOption('all') \
        .checkAllButton() \
        .uncheckAllButton()

    InputForms.clickInputForms(driver) \
        .clickRadioButtonsDemo(driver) \
        .clickMaleButton() \
        .clickCheckedValueButton() \
        .clickFemaleButton() \
        .clickCheckedValueButton() \
        .clickGroupMaleButton() \
        .clickGroupZeroFive() \
        .clickGroupValues()

    InputForms.clickInputForms(driver) \
        .clickDropdownListDemo(driver) \
        .selectDayFromDropdown("Friday") \
        .selectStateFromList(['Ohio', 'Florida', 'Texas', 'California']) \
        .clickAllSelectedButton() \
        .clickFirstSelectedButton()

    InputForms.clickInputForms(driver) \
        .clickInputFormSubmitDemo(driver) \
        .addName("Elon").addLastName("Musk") \
        .addEmail("model_3@tesla.com").addPhone('2000300400') \
        .addAddress("Mars sector 4 334567") \
        .addCity("Solar City").selectState().addZipcode("12345678") \
        .addWebsite("https://starlink.com").clickHostingYes() \
        .addComment("Hello world !!")

    InputForms.clickInputForms(driver) \
        .clickAjaxFormSubmitDemo(driver) \
        .addName("User") \
        .addComment("Hello World!!") \
        .clickSubmit()

    InputForms.clickInputForms(driver) \
        .clickJquerySelectDropdownDemo(driver) \
        .selectCountry('denmark', True).selectMultipleValues(['alabama', 'alaska', 'colorado']) \
        .selectTerritories('Virgin Islands').selectFile('C')

    driver.quit()


if __name__ == '__main__':
    run()
