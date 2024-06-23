from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".md\\3Atext-sm")
    ACCOUNT_BUTTON_TEXT = (By.XPATH, "//button[@id='headlessui-menu-button-:r0:']")
    GOOGLE_IMAGE = (By.XPATH, "//img[@alt='google image']")
    FORGET_PASSWORD_BUTTON = (By.XPATH, "//a[@href='/forget-password']")


