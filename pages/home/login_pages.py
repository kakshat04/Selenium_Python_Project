from time import sleep
from base.selenium_driver import SeleniumDriver as SD


class LoginPage(SD):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.sd = SD(self.driver)

    # locators
    _login_link = "Login"
    _email_field_id = "user_email"
    _password_field_id = "user_password"
    _login_button_name = "commit"
    _login_success_field_id = "search-courses"
    _login_failed_class_name = "alert alert-danger"

    # def get_login_link(self):
    #     return self.driver.find_element(By.PARTIAL_LINK_TEXT, self._login_link)
    #
    # def get_email_field(self):
    #     return self.driver.find_element(By.ID, self._email_field_id)
    #
    # def get_password_field(self):
    #     return self.driver.find_element(By.ID, self._password_field_id)
    #
    # def get_login_button(self):
    #     return self.driver.find_element(By.NAME, self._login_button_name)

    def click_login_link(self):
        # self.sd.element_click(self._login_link, 'link') # When done without Inheritance
        self.element_click(self._login_link, 'link')

    def enter_email(self, email):
        # self.sd.enter_keys(self._email_field_id, 'id', email) # When done without Inheritance
        self.clear_text(self._email_field_id, 'id')
        self.enter_keys(self._email_field_id, 'id', email)

    def enter_password(self, pwd):
        # self.sd.enter_keys(self._password_field_id, 'id', pwd) # When done without Inheritance
        self.clear_text(self._password_field_id, 'id')
        self.enter_keys(self._password_field_id, 'id', pwd)

    def click_login_button(self):
        # self.sd.element_click(self._login_button_name, 'name') # When done without Inheritance
        self.element_click(self._login_button_name, 'name')

    def login_page(self, email='', password=''):
        self.click_login_link()
        sleep(2)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        is_login_success = self.is_element_present(self._login_success_field_id, 'id')
        if is_login_success:
            return True
        else:
            return False

    def verify_login_failed(self):
        is_login_fail = self.is_element_present("//div[contains(text(),'Invalid email or password')]", 'xpath')
        if is_login_fail:
            return True
        else:
            return False



