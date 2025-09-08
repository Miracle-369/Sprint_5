from selenium.webdriver.common.by import By
from locators import Locators
from urls import Urls

class Testlogin:

    def test_login_button_on_the_main_page(self,driver):
        #Кликаем по кнопке Войти в аккаунт
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()

        email = "vladislav_fedotov_29_333@yandex.ru"
        password = "qwerty333"

        #Вводим валидный email
        driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email)
        #Вводим валидный пароль       
        driver.find_element(*Locators.PASSWORD_INPUT_REGISTER).send_keys(password)

        #Кликаем по кнопке Войти
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        #Проверяем что URL Изменился на Основной адрес приложения 
        assert Urls.MAIN_PAGE in driver.current_url

    def test_login_button_personal_account(self,driver):
        
        #Кликаем по кнопке Личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        #Валидный Email
        email = "vladislav_fedotov_29_333@yandex.ru"
        #Валидный Пароль
        password = "qwerty333"

        #Вводим валидный email
        driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email)
        #Вводим валидный пароль       
        driver.find_element(*Locators.PASSWORD_INPUT_REGISTER).send_keys(password)

        #Кликаем по кнопке Войти
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        #Проверяем что нас перенесло на главную страницу после входа
        assert Urls.MAIN_PAGE in driver.current_url

    def test_login_button_in_the_registration_form(self,driver):  
        
        #Кликаем по кнопке Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        #Кликаем по ссылке Зарегистрироваться
        driver.find_element(*Locators.REGISTER_LINK).click()

        #Кликаем по ссылке Войти
        driver.find_element(*Locators.LOGIN_LINK_REGISTER).click()

        #Валидный Email
        email = "vladislav_fedotov_29_333@yandex.ru"
        #Валидный Пароль
        password = "qwerty333"

        #Вводим валидный email
        driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email)
        #Вводим валидный пароль       
        driver.find_element(*Locators.PASSWORD_INPUT_REGISTER).send_keys(password)

        #Кликаем по кнопке Войти
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        #Проверяем что нас перенесло на главную страницу после входа
        assert Urls.MAIN_PAGE in driver.current_url

    def test_login_button_in_the_password_recovery_form(self,driver):

        #Кликаем по кнопке Личный Кабинет
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()

        #Кликаем по ссылке Восстановить пароль
        driver.find_element(*Locators.RECOVERY_PASSWORD_LINK).click()
        
        #Кликаем по ссылке Войти
        driver.find_element(*Locators.LOGIN_LINK_RECOVEY).click()

         #Валидный Email
        email = "vladislav_fedotov_29_333@yandex.ru"
        #Валидный Пароль
        password = "qwerty333"

        #Вводим валидный email
        driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email)
        #Вводим валидный пароль       
        driver.find_element(*Locators.PASSWORD_INPUT_REGISTER).send_keys(password)

        #Кликаем по кнопке Войти
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        #Проверяем что нас перенесло на главную страницу после входа
        assert Urls.MAIN_PAGE in driver.current_url

