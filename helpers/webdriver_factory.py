from selenium import webdriver

class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name: str):
        if browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            return webdriver.Firefox(options)
        elif browser_name == 'chrome':
            return webdriver.Chrome()

        raise NotImplementedError(f'Нет реализованного драйвера для браузера с названием {browser_name}!')
