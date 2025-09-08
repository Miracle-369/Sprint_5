from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import Urls

class TestButton:

    def test_click_to_go_to_your_personal_account(self,driver):
        #Кликаем по кнопке Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        email = "vladislav_fedotov_29_333@yandex.ru"
        password = "qwerty333"

        #Вводим валидные email и password
        driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_REGISTER).send_keys(password)
        
        #Кликаем по кнопке Войти
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        #Кликаем по кнопке Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        
        #Проверяем что мы в Личном аккаунте
        assert Urls.PERSONAL_ACOUNT_PAGE in driver.current_url

    def test_click_to_go_to_the_constructor(self, driver):
        
        #Кликаем по кнопке Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        email = "vladislav_fedotov_29_333@yandex.ru"
        password = "qwerty333"

        #Вводим валидные email и password
        driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_REGISTER).send_keys(password)
        
        #Кликаем по кнопке Войти
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        
        #Кликаем по кнопке Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        #Кликаем по кнопке Конструктор
        driver.find_element(*Locators.HEADER_BUTTON_CONSTRUCTOR).click()

        #Проверяем что нас перенесло на главную страницу
        assert Urls.MAIN_PAGE in driver.current_url

    def test_transition_by_clicking_on_the_logo(self,driver):
        
        #Кликаем по кнопке Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        email = "vladislav_fedotov_29_333@yandex.ru"
        password = "qwerty333"

        #Вводим валидные email и password
        driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_REGISTER).send_keys(password)

        #Кликаем по кнопке Войти
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        #Кликаем по кнопке Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        #Кликаем по Логотипу
        driver.find_element(*Locators.LOGO_BUTTON).click()


        #Проверяем что нас перенесло на главную страницу
        assert Urls.MAIN_PAGE in driver.current_url

    def test_Logout(self,driver):
        
        #Кликаем по кнопке Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        email = "vladislav_fedotov_29_333@yandex.ru"
        password = "qwerty333"

        #Вводим валидные email и password
        driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_REGISTER).send_keys(password)

        #Кликаем по кнопке Войти
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        #Кликаем по кнопке Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        #Кликаем по кнопке Выход
        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        #Проверяем что нас перенесло на страницу Входа
        assert Urls.LOGIN_PAGE in driver.current_url
        
