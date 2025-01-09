class UrlsContainer:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    LOGIN_PAGE_URL = f'{BASE_URL}login'
    FORGOT_PASSWORD_PAGE_URL = f'{BASE_URL}forgot-password'
    API_URL = f'{BASE_URL}api/'
    API_AUTH_URL = f'{API_URL}auth/'
    API_REGISTER_USER_URL = f'{API_AUTH_URL}register'
    API_USER_URL = f'{API_AUTH_URL}user'