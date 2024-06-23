from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.loginpage_locators import LoginPageLocators

class LoginPage(BasePage):
    def enter_username(self, username):
        self.find_element(LoginPageLocators.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_button_text(self):
        return self.find_element(LoginPageLocators.ACCOUNT_BUTTON_TEXT).text

    def click_forget_password_button(self):
        self.find_element(LoginPageLocators.FORGET_PASSWORD_BUTTON).click()

