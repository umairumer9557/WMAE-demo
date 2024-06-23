from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.forgetpasswordpage_locators import ForgetPasswordPageLocators

class ForgetPasswordPage(BasePage):
    def get_f_password_headline_text(self):
        return self.find_element(ForgetPasswordPageLocators.FORGET_PASSWORD_HEADLINE_TEXT).text

    def enter_email(self, email):
        self.find_element(ForgetPasswordPageLocators.EMAIL_FIELD).send_keys(email)

    def click_submit_button(self):
        self.find_element(ForgetPasswordPageLocators.SUBMIT_BUTTON).click()

    def return_enter_OTP_text(self):
        return self.find_element(ForgetPasswordPageLocators.ENTER_OTP_TEXT).text


