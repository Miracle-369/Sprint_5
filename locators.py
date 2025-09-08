from selenium.webdriver.common.by import By

class Locators:

    #Главная страница
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    HEADER_BUTTON_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")
    LOGO_BUTTON = (By.XPATH, ".//a")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    #Страница регистрации
    NAME_INPUT_REGISTER = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT_REGISTER = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT_REGISTER = (By.XPATH, ".//input[@type='password']")
    BUTTON_REGISTER = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    LOGIN_LINK_REGISTER = (By.LINK_TEXT, "Войти")

    #Страница входа 
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RECOVERY_PASSWORD_LINK =(By.LINK_TEXT, "Восстановить пароль")

    #Страница востановления пароля 
    LOGIN_LINK_RECOVEY = (By.LINK_TEXT, "Войти")

    #Конструктор
    SAUCE_BUTTON = (By.XPATH, "//span[contains(text(), 'Соусы')]/..")
    ACTIVE_CONTAINER = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
    FILINGS_BUTTON = (By.XPATH, "//span[contains(text(), 'Начинки')]/..")
    BUNS_BUTTON = (By.XPATH, "//span[contains(text(), 'Булки')]/..")
