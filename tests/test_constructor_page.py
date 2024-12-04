from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConstructorPage:

    # Тест на проверку входа в конструктор по кнопке "Конструктор" из Личного кабинета
    def test_click_on_constructor_label(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.CONSTRUCTOR_LABEL).click()
        WebDriverWait(login, 5).until(EC.visibility_of_element_located((Locators.CONSTRUCTOR_BURGER)))
        assert driver.find_element(*Locators.CONSTRUCTOR_BURGER).is_displayed()

    # Тест на проверку входа в конструктор по логотипу сайта из Личного кабинета
    def test_click_on_logo_burger(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.LOGO_BURGER).click()
        WebDriverWait(login, 5).until(EC.visibility_of_element_located((Locators.CONSTRUCTOR_BURGER)))
        assert driver.find_element(*Locators.CONSTRUCTOR_BURGER).is_displayed()

    # Тест на проверку выбора Булочек
    def test_click_rolls(self, driver, login):
        driver.find_element(*Locators.CONSTRUCTOR_LABEL).click()
        driver.find_element(*Locators.SAUCES_LABEL).click()
        driver.find_element(*Locators.ROLLS_LABEL).click()
        assert driver.find_element(*Locators.ROLLS_FOCUS)

    # Тест на проверку выбора Соуса
    def test_click_sauces(self, driver, login):
        driver.find_element(*Locators.CONSTRUCTOR_LABEL).click()
        driver.find_element(*Locators.SAUCES_LABEL).click()
        assert driver.find_element(*Locators.SAUCES_FOCUS)

    # Тест на проверку выбора Начинки
    def test_click_fillings(self, driver, login):
        driver.find_element(*Locators.CONSTRUCTOR_LABEL).click()
        driver.find_element(*Locators.FILLINGS_LABEL).click()
        assert driver.find_element(*Locators.FILLINGS_FOCUS)
