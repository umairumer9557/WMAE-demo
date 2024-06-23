import time
import pytest

from pages.login_page import LoginPage

@pytest.mark.parametrize("email_for_login, password_for_login", [
    ("testing7676@yopmail.com", "12345678!Cipro"),
    # ("testing7777@yopmail.com", ")Ev%w}ifCK1s"),
    # ("testing7878@yopmail.com", "12345678!Cipro")
])

def test_valid_login(browser, email_for_login, password_for_login):
    login_page = LoginPage(browser)

    login_page.open("/login")
    login_page.enter_username(email_for_login)
    login_page.enter_password(password_for_login)
    login_page.click_login()
    time.sleep(5)
    account_button_text = login_page.get_button_text()
    assert account_button_text == "Account"


