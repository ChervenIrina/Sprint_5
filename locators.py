from selenium.webdriver.common.by import By


class Locators:
    # Локатор ссылки "Личный кабинет"
    PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")
    # Локатор ссылки "Зарегистрироваться"
    REG_LABEL = (By.LINK_TEXT, 'Зарегистрироваться')
    # Локатор кнопки "Зарегистрироваться"
    REG_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    # Локатор поля ввода имени
    NAME = (By.XPATH, ".//label[text()='Имя']/following-sibling::input[@type='text']")
    # Локатор поля ввода email
    EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']")
    # Локатор поля ввода пароля
    PASSWORD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@type='password']")
    # Локатор кнопки "Войти в аккаунт"
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    # Локатор кнопки "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    # Локатор ссылки "Войти"
    LOGIN_LABEL = (By.LINK_TEXT, 'Войти')
    # Локатор загрузки основной страницы
    MAIN_PAGE = (By.CLASS_NAME, "App_App__aOmNj")
    # Локатор ссылки "Восстановить пароль"
    PASSWORD_RECOVERY_LABEL = (By.LINK_TEXT, "Восстановить пароль")
    # Локатор блока профиля пользователя
    ACCOUNT_INFO = (By.CLASS_NAME, "Account_account__vgk_w")
    # Локатор ссылки "Конструктор"
    CONSTRUCTOR_LABEL = (By.LINK_TEXT, "Конструктор")
    # Локатор блока конструктор бургера
    CONSTRUCTOR_BURGER = (By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")
    # Локатор логотипа "stellar burgers"
    LOGO_BURGER = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    # Локатор кнопки "Выход"
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    # Локатор ссылки "Булки"
    ROLLS_LABEL = (By.XPATH, "//span[contains(text(), 'Булки')]")
    # Локатор фокуса "Булки"
    ROLLS_FOCUS = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[contains(text(), 'Булки')]")
    # Локатор ссылки "Соусы"
    SAUCES_LABEL = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    # Локатор фокуса "Соусы"
    SAUCES_FOCUS = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[contains(text(), 'Соусы')]")
    # Локатор ссылки "Начинки"
    FILLINGS_LABEL = (By.XPATH, "//span[contains(text(), 'Начинки')]")
    # Локатор фокуса "Начинки"
    FILLINGS_FOCUS = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[contains(text(), 'Начинки')]")

class Messages:
    # Локатор текста ошибки при регистрации, если пользователь уже такой есть
    USER_EXIST = (By.XPATH, ".//p[contains(text(), 'Такой пользователь уже существует')]")
    # Локатор текста ошибки при вводи некорректного пароля
    ERROR_PASSWORD = (By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]")
