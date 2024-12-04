import pytest
from selenium import webdriver

from constants import Constants
from locators import Locators

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser
    browser.quit()

@pytest.fixture
def form_registration(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.REG_LABEL).click()
    return driver

@pytest.fixture()
def form_password_recovery(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.PASSWORD_RECOVERY_LABEL).click()
    return driver

@pytest.fixture()
def login(driver):
    driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return driver
