from selenium.webdriver.common.by import By


class Testlogin:

    def test_login_button_on_the_main_page(self,driver):
        #Кликаем по кнопке Войти в аккаунт
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        email = "vladislav_fedotov_29_333@yandex.ru"
        password = "qwerty333"

        #Вводим валидный email
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
        #Вводим валидный пароль       
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)

        #Кликаем по кнопке Войти
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        #Проверяем что URL Изменился на Основной адрес приложения 
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

    def test_login_button_personal_account(self,driver):
        
        #Кликаем по кнопке Личный кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()

        #Валидный Email
        email = "vladislav_fedotov_29_333@yandex.ru"
        #Валидный Пароль
        password = "qwerty333"

        #Вводим валидный email
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
        #Вводим валидный пароль       
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)

        #Кликаем по кнопке Войти
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        #Проверяем что нас перенесло на главную страницу после входа
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

    def test_login_button_in_the_registration_form(self,driver):  
        
        #Кликаем по кнопке Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        
        #Кликаем по ссылке Зарегистрироваться
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

        #Кликаем по ссылке Войти
        driver.find_element(By.LINK_TEXT, "Войти").click()

        #Валидный Email
        email = "vladislav_fedotov_29_333@yandex.ru"
        #Валидный Пароль
        password = "qwerty333"

        #Вводим валидный email
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
        #Вводим валидный пароль       
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)

        #Кликаем по кнопке Войти
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        #Проверяем что нас перенесло на главную страницу после входа
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

    def test_login_button_in_the_password_recovery_form(self,driver):

        #Кликаем по кнопке Личный Кабинет
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()

        #Кликаем по ссылке Восстановить пароль
        driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
        
        #Кликаем по ссылке Войти
        driver.find_element(By.LINK_TEXT, "Войти").click()

         #Валидный Email
        email = "vladislav_fedotov_29_333@yandex.ru"
        #Валидный Пароль
        password = "qwerty333"

        #Вводим валидный email
        driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
        #Вводим валидный пароль       
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)

        #Кликаем по кнопке Войти
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        #Проверяем что нас перенесло на главную страницу после входа
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

