from selenium.webdriver.common.by import By
from locators import Locators
from urls import Urls
import random


class TestRegistrationPage:

    def test_successful_registration(self, driver):

        #Кликаем по кнопке Личный Кабинет 
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        #Кликаем по ссылке Зарегистрироваться 
        driver.find_element(*Locators.REGISTER_LINK).click()

        name = "Rostik Rost"
        email = f"vladislav_fedotov_29_{random.randint(000, 999)}@yndex.ru"
        password = "jobjob123"
        
        #Вводим валидные имя, email, пароль
        driver.find_element(*Locators.NAME_INPUT_REGISTER).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_REGISTER).send_keys(password)

        driver.find_element(*Locators.BUTTON_REGISTER).click()

        #Проверяем что нам перенесло на главную страницу
        assert Urls.MAIN_PAGE in driver.current_url

    def test_incorrect_password_error(self, driver):

        #Кликаем по кнопке Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
           

        #Кликаем по ссылке Зарегистрироваться
        driver.find_element(*Locators.REGISTER_LINK).click()
    

        name = "Rostik Rost"
        email = f"vladislav_fedotov_29_{random.randint(000, 999)}@yndex.ru"
        password = "job33"
        
        #Вводим валидные имя, email
        driver.find_element(*Locators.NAME_INPUT_REGISTER).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email)
        #Водим короткий пароль
        driver.find_element(*Locators.PASSWORD_INPUT_REGISTER).send_keys(password)

        #Кликаем по кнопке Зарегистрироваться
        driver.find_element(*Locators.BUTTON_REGISTER).click()

        #Проверяем появления сообщения  Некорректный пароль
        assert "Некорректный пароль" in driver.page_source

        