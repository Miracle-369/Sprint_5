from selenium.webdriver.common.by import By
import random
import time

class TestRegistrationPage:

    def test_successful_registration(self, driver):

        #Кликаем по кнопке Личный Кабинет 
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        time.sleep(2)

        #Кликаем по ссылке Зарегистрироваться 
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        time.sleep(2)

        name = "Rostik Rost"
        email = f"vladislav_fedotov_29_{random.randint(000, 999)}@yndex.ru"
        password = "jobjob123"
        
        #Вводим валидные имя, email, пароль
        driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input").send_keys(name)
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)

        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        time.sleep(2)

        #Проверяем что нам перенесло на главную страницу
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

    def test_incorrect_password_error(self, driver):

        #Кликаем по кнопке Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        time.sleep(2)   

        #Кликаем по ссылке Зарегистрироваться
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        time.sleep(2)

        name = "Rostik Rost"
        email = f"vladislav_fedotov_29_{random.randint(000, 999)}@yndex.ru"
        password = "job33"
        
        #Вводим валидные имя, email
        driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input").send_keys(name)
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
        #Водим короткий пароль
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)

        #Кликаем по кнопке Зарегистрироваться
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        time.sleep(2)

        #Проверяем появления сообщения  Некорректный пароль
        assert "Некорректный пароль" in driver.page_source

        