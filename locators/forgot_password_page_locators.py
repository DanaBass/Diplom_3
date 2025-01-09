from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    RECOVER_PASSWORD_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Восстановить']"
    EMAIL_PLACEHOLDER = By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']"