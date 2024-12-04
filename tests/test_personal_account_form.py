from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestPersonalAccountForm:

    # Тест на проверку входа в Личный кабинет
    def test_click_on_personal_account(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(login, 5).until(EC.visibility_of_element_located((Locators.ACCOUNT_INFO)))
        assert driver.find_element(*Locators.ACCOUNT_INFO).is_displayed()

    # Тест на проверку выхода из аккаунта
    def test_click_exit_button(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(login, 5).until(EC.visibility_of_element_located((Locators.EXIT_BUTTON)))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(login, 5).until(EC.visibility_of_element_located((Locators.LOGIN_BUTTON)))
        assert driver.find_element(*Locators.LOGIN_BUTTON).is_displayed()




