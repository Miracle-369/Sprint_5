from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestConctructor:

    def test_transition_to_sauces(self,driver):

        #Кликаем по кнопке Соуса
        driver.find_element(*Locators.SAUCE_BUTTON).click()

        WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(Locators.ACTIVE_CONTAINER, "Соусы"))

        active_section = driver.find_element(*Locators.ACTIVE_CONTAINER)
        
        #Проверяем то что класс стал активным        
        assert "Соусы" in active_section.text

    def test_transition_to_fillings(self,driver):

        #Нажимаем по кнопке Начинки
        driver.find_element(*Locators.FILINGS_BUTTON).click()

        WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(Locators.ACTIVE_CONTAINER, "Начинки"))

        active_section = driver.find_element(*Locators.ACTIVE_CONTAINER)

        #Проверяем класс что он стал активным 
        assert "Начинки" in active_section.text  

    def test_transition_to_buns(self,driver):

        #Кликаем по кнопке Соусы
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        
        #Кликаем по кнопке Булке
        driver.find_element(*Locators.BUNS_BUTTON).click()

        #Находим класс который стал активным
        WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(Locators.ACTIVE_CONTAINER, "Булки")
        )

        active_section = driver.find_element(*Locators.ACTIVE_CONTAINER)

        #Проверяем класс то что он стал активным
        assert "Булки" in active_section.text