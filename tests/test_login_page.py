import pytest
from constants import Constants
from locators import Locators


class TestLoginPage:

    # Тест на проверку входа через кнопку "Войти в аккаунт"
    def test_login_button_login_to_account(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        user_authorization(driver)
        assert driver.find_element(*Locators.MAIN_PAGE).is_displayed()

    # Тест на проверку входа через кнопку "Личный кабинет"
    def test_login_button_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        user_authorization(driver)
        assert driver.find_element(*Locators.MAIN_PAGE).is_displayed()

    # Тест на проверку входа через форму Регистрации
    def test_login_in_reg_form(self, driver, form_registration):
        driver.find_element(*Locators.LOGIN_LABEL).click()
        user_authorization(driver)
        assert driver.find_element(*Locators.MAIN_PAGE).is_displayed()

    # Тест на проверку входа через форму восстановления пароля
    def test_login_in_pass_recovery(self, driver, form_password_recovery):
        driver.find_element(*Locators.LOGIN_LABEL).click()
        user_authorization(driver)
        assert driver.find_element(*Locators.MAIN_PAGE).is_displayed()

# Ввода данных пользователя
def user_authorization(driver):
    driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return driver
