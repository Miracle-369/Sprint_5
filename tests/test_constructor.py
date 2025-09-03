from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConctructor:

    def test_transition_to_sauces(self,driver):

        #Кликаем по кнопке Соуса
        driver.find_element(By.XPATH, "//span[contains(text(), 'Соусы')]/..").click()

        WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]"), "Соусы"))

        active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        
        #Проверяем то что класс стал активным        
        assert "Соусы" in active_section.text

    def test_transition_to_fillings(self,driver):

        #Нажимаем по кнопке Начинки
        driver.find_element(By.XPATH, "//span[contains(text(), 'Начинки')]/..").click()

        WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]"), "Начинки"))

        active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

        #Проверяем класс что он стал активным 
        assert "Начинки" in active_section.text  

    def test_transition_to_buns(self,driver):

        #Кликаем по кнопке Соусы
        driver.find_element(By.XPATH, "//span[contains(text(), 'Соусы')]/..").click()
        
        #Кликаем по кнопке Булке
        driver.find_element(By.XPATH, "//span[contains(text(), 'Булки')]/..").click()

        #Находим класс который стал активным
        WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]"), "Булки")
        )

        active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

        #Проверяем класс то что он стал активным
        assert "Булки" in active_section.text