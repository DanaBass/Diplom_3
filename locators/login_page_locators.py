from selenium.webdriver.common.by import By

class LoginPageLocators:
    FORGOT_PASSWORD_LINK = By.XPATH, "//a[@class='Auth_link__1fOlj' and contains(text(), 'Восстановить пароль')]"
    ACCOUNT_REGISTRATION_LOCATOR = By.XPATH, "//a[text()='Зарегистрироваться']"  # Кнопка "Зарегистрироваться"
    LOCATOR_AUTHORIZATION_EMAIL = By.NAME, 'name'  # Ввод email для входа.
    LOCATOR_AUTHORIZATION_PASSWORD = By.NAME, 'Пароль'  # Ввод пароля для входа.
    LOCATOR_LOGIN_BUTTON = By.XPATH, './/button[text()="Войти"]'  # Кнопка "Войти" после авторизации.

