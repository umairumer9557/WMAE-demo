from selenium.webdriver.common.by import By

class ForgetPasswordPageLocators:
    FORGET_PASSWORD_HEADLINE_TEXT = (By.XPATH, "/html/body/div[2]/div/form/h3[1]")
    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    SUBMIT_BUTTON = (By.XPATH, '//button[@data-variant="primary"]')
    ENTER_OTP_TEXTS = (By.XPATH, '//div[@class="text-left"]')



