from selenium.webdriver.common.by import By

class ResetPasswordPageLocators:
    PASSWORD_PLACEHOLDER = By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Введите новый пароль' and @type='password']"
    SHOW_PASSWORD_ELEMENT = By.XPATH, "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]"
    PASSWORD_ACTIVE_STATUS_ELEMENT = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']"