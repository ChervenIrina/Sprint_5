import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators, Messages
from faker import Faker

faker = Faker()


class TestRegistrationForm:

    # Тест на успешную регистрацию
    def test_registration_new_user(self, driver, form_registration):
        driver.find_element(*Locators.NAME).send_keys(faker.name())
        driver.find_element(*Locators.EMAIL).send_keys(faker.email())
        driver.find_element(*Locators.PASSWORD).send_keys(faker.password())
        driver.delete_all_cookies()
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(form_registration, 5).until(EC.visibility_of_element_located((Locators.LOGIN_BUTTON)))
        assert driver.current_url == Constants.URL_PAGE_LOGIN

    # Тест на проверку, что регистрация не будет пройдена, если поле Имя пустое
    def test_registration_name_none(self, driver, form_registration):
        driver.find_element(*Locators.EMAIL).send_keys(faker.email())
        driver.find_element(*Locators.PASSWORD).send_keys(faker.password())
        driver.find_element(*Locators.REG_BUTTON).click()
        assert driver.current_url == Constants.URL_PAGE_REG

    # Тест на проверку, что регистрация не будет пройдена, если Почта не соответствует маски логин@домен
    @pytest.mark.parametrize("email", ['123', '@ya.ru', '123ya.ru'])
    def test_registration_email_not_correct(self, driver, email, form_registration):
        driver.find_element(*Locators.NAME).send_keys(faker.name())
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(faker.password())
        driver.find_element(*Locators.REG_BUTTON).click()
        assert driver.current_url == Constants.URL_PAGE_REG

    # Тест на проверку вывода ошибки для некорректного пароля, если длина менее 6  символов
    @pytest.mark.parametrize("password", ['1', '12345'])
    def test_registration_pass_error_not_correct(self, driver, password, form_registration):
        driver.find_element(*Locators.NAME).send_keys(faker.name())
        driver.find_element(*Locators.EMAIL).send_keys(faker.email())
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        assert driver.find_element(*Messages.ERROR_PASSWORD).text == 'Некорректный пароль'
