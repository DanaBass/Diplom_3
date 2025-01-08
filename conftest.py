import pytest
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from api.methods.auth_methods import AuthMethods
from data.data import User
from data.urls import UrlsContainer
from helpers.user_data_generator import RandomRegistrationGenerator
from helpers.webdriver_factory import WebdriverFactory
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.feed_page import FeedPage
from pages.constructor_page import ConstructorPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """
    Базовый драйверп
    """
    driver =  WebdriverFactory.get_webdriver(request.param)
    yield driver
    driver.quit()

@pytest.fixture()
def main_page_driver(driver):
    driver.get(UrlsContainer.MAIN_PAGE_URL)
    return driver

@pytest.fixture()
def login_page_driver(driver):
    driver.get(UrlsContainer.LOGIN_PAGE_URL)
    return driver

@pytest.fixture()
def forgot_password_page_driver(driver):
    driver.get(UrlsContainer.FORGOT_PASSWORD_PAGE_URL)
    return driver

@pytest.fixture()
def random_user_data():
    name = RandomRegistrationGenerator.generate_random_name()
    email = RandomRegistrationGenerator.generate_random_email()
    password = RandomRegistrationGenerator.generate_password_random()
    user = User(email, password, name)

    AuthMethods.create_new_user(user) # По API создаём нового пользователя.
    yield user
    AuthMethods.delete_user(user) # После работы тестов через API удаляем созданного пользователя.

@pytest.fixture()
def main_page_with_logged_in_user(login_page_driver, random_user_data):
    main_page = ConstructorPage(login_page_driver)
    login_user(login_page_driver, random_user_data)

    return main_page

@pytest.fixture()
def feed_page_with_logged_in_user(login_page_driver, random_user_data):
    feed_page = FeedPage(login_page_driver)
    login_user(login_page_driver, random_user_data)
    feed_page.click_to_element(MainPageLocators.ORDER_FEED_LINK_ELEMENT)

    return feed_page

def login_user(login_page_driver, random_user_data):
    driver = login_page_driver

    personal_account = driver.find_element(*MainPageLocators.LOCATOR_PERSONAL_ACCOUNT)
    try:
        personal_account.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", personal_account)

    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable(LoginPageLocators.ACCOUNT_REGISTRATION_LOCATOR))

    driver.find_element(*LoginPageLocators.LOCATOR_AUTHORIZATION_EMAIL).send_keys(random_user_data.login)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOCATOR_AUTHORIZATION_PASSWORD))

    driver.find_element(*LoginPageLocators.LOCATOR_AUTHORIZATION_PASSWORD).send_keys(random_user_data.password)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LoginPageLocators.ACCOUNT_REGISTRATION_LOCATOR))

    driver.find_element(*LoginPageLocators.LOCATOR_LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(MainPageLocators.LOCATOR_PLACE_AN_ORDER))