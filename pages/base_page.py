import allure
from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from data import javascript_scripts
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Поиск элемента по локатору")
    def find_element_with_wait(self, locator, timeout: float = 10, need_visibility=True):
        try:
            if need_visibility:
                return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
            else:
                return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            return None

    @allure.step("Ожидание, пока элемент по переданному локатору не отобразится ")
    def wait_until_element_disappears(self, locator, timeout: float = 10):
        WebDriverWait(self.driver, timeout).until_not(ec.visibility_of_element_located(locator))

    @allure.step("Ожидание, пока элемент по переданному локатору не пропадёт ")
    def wait_until_element_appears(self, locator, timeout: float = 10):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    @allure.step("Ожидание, пока переданное условие не выполнится")
    def wait_until_condition(self, condition_lambda, timeout: float = 10):
        WebDriverWait(self.driver, timeout).until(condition_lambda)

    @allure.step("Поиск всех элементов по переданному локатору")
    def find_all_elements_with_wait(self, locator, timeout: float = 10, need_visibility=True):
        try:
            if need_visibility:
                return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))
            else:
                return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))
        except TimeoutException:
            return None

    @allure.step("Клик с ожиданием по элементу, подходящему переданному локатору")
    def click_to_element(self, locator, timeout: float = 10):
        element = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Добавление текста к элементу, связанному с переданным локатором")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получение текста из элемента, связанного с переданным локатором")
    def get_text_from_element(self, locator, timeout: float = 10):
        element = WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        return element.text

    @allure.step("Переход на ленту заказов")
    def go_to_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_LINK_ELEMENT)

    @allure.step("Переход на конструктор")
    def go_to_constructor(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_LINK_ELEMENT)

    @allure.step("Перенос элемента")
    def drag_and_drop_element(self, source_element, target_element):
        self.driver.execute_script(javascript_scripts.DRAG_AND_DROP_SCRIPT, source_element, target_element)

    @allure.step("Открытие новой вкладки")
    def open_new_tab(self, url: str):
        self.driver.execute_script("window.open();")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(url)

    @staticmethod
    @allure.step("Поиск дочернего элемента в родительском по переданному локатору")
    def find_child_element_by_xpath(parent: WebElement, locator):
        if parent is None:
            return None

        try:
            return parent.find_element(By.XPATH, locator)
        except:
            return None