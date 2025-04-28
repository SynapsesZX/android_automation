from page_object.base_page import BasePage
import locators.instagram


class UserLogin(BasePage):

    def click_instagram_icon(self):
        self.wait_and_click(locators.instagram.instagram_icon)

    def click_username_input_field(self):
        self.wait_and_click(locators.instagram.username_input_field)

    def write_invalid_username(self,username):
        self.send_keys(locators.instagram.username_input_field, value=username)

    def write_invalid_password(self,password):
        self.send_keys(locators.instagram.password_input_field, value=password)

    def click_login_button(self):
        self.wait_and_click(locators.instagram.login_button)

    def check_error_login_message(self):
        self.check_element_text(locators.instagram.log_in_error_message, text="Unable to log in")
        self.check_element_attribute(locators.instagram.log_in_error_description,attribute='text',attribute_value='An unexpected error occurred. Please try logging in again.')

    def click_ok_button(self):
        self.wait_and_click(locators.instagram.log_in_error_ok_button)

    def log_in_message_disappeared(self):
        self.check_if_element_is_not_displayed(locators.instagram.log_in_error_ok_button)


