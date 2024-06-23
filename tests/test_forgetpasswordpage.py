import time
import pytest
from pages.login_page import LoginPage
from pages.forgetpassword_page import ForgetPasswordPage

def test_submit_email_for_forget_password(browser):
    login_page = LoginPage(browser)
    forget_password_page = ForgetPasswordPage(browser)

    login_page.open("/login")
    login_page.click_forget_password_button()
    time.sleep(2)
    forget_password_headline_text = forget_password_page.get_f_password_headline_text()
    assert forget_password_headline_text == "Forgot password"
    forget_password_page.enter_email("testing7878@yopmail.com")
    forget_password_page.click_submit_button()
    enter_otp_text = forget_password_page.return_enter_OTP_text()
    assert enter_otp_text == "Please enter OTP here"


