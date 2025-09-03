from selenium.webdriver.common.by import By
import time

class TestButton:

    def test_click_to_go_to_your_personal_account(self,driver):
        #Кликаем по кнопке Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()

        email = "vladislav_fedotov_29_333@yandex.ru"
        password = "qwerty333"

        #Вводим валидные email и password
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)
        
        #Кликаем по кнопке Войти
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        #Кликаем по кнопке Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        time.sleep(2)
        
        #Проверяем что мы в Личном аккаунте
        assert "https://stellarburgers.nomoreparties.site/account/profile" in driver.current_url 

    def test_click_to_go_to_the_constructor(self, driver):
        
        #Кликаем по кнопке Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()

        email = "vladislav_fedotov_29_333@yandex.ru"
        password = "qwerty333"

        #Вводим валидные email и password
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)
        
        #Кликаем по кнопке Войти
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        #Кликаем по кнопке Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        
        #Кликаем по кнопке Конструктор
        driver.find_element(By.LINK_TEXT, "Конструктор").click()

        #Проверяем что нас перенесло на главную страницу
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

    def test_transition_by_clicking_on_the_logo(self,driver):
        
        #Кликаем по кнопке Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()

        email = "vladislav_fedotov_29_333@yandex.ru"
        password = "qwerty333"

        #Вводим валидные email и password
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)

        #Кликаем по кнопке Войти
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        #Кликаем по кнопке Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        
        #Кликаем по Логотипу
        driver.find_element(By.XPATH, ".//a").click()


        #Проверяем что нас перенесло на главную страницу
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

    def test_Logout(self,driver):
        
        #Кликаем по кнопке Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()

        email = "vladislav_fedotov_29_333@yandex.ru"
        password = "qwerty333"

        #Вводим валидные email и password
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)

        #Кликаем по кнопке Войти
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        #Кликаем по кнопке Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        
        #Кликаем по кнопке Выход
        driver.find_element(By.XPATH, "//button[contains(text(), 'Выход')]").click()
        time.sleep(2)

        #Проверяем что нас перенесло на страницу Входа
        assert "https://stellarburgers.nomoreparties.site/login" in driver.current_url
        
