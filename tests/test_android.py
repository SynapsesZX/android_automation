import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.instagram_user_login import UserLogin
import time





class TestInstagram:
    @pytest.mark.log_in_regression
    @pytest.mark.parametrize("username, password", [
        ("fghjfgjhjj@gmail.com", "657865786595"),
        ("!@$%%^^&$^", "wrong_pass"),
        ("wrong_user", "%^^&%%^^"),
    ])
    def test_login_with_invalid_credentials(self,driver,username,password):
        user = UserLogin(driver)
        user.write_invalid_username(username)
        user.write_invalid_password(password)
        user.click_login_button()
        user.check_error_login_message()
        user.click_ok_button()
        user.log_in_message_disappeared()


