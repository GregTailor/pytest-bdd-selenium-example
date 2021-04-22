from selenium.webdriver.common.by import By

from pages.page import Page


class LetsTalkTeaPage(Page):

    form_locators = {
        "name": (By.CSS_SELECTOR, '[name=name]'),
        "email": (By.CSS_SELECTOR, '[name=email]'),
        "subject": (By.CSS_SELECTOR, '[name=subject]'),
        "message": (By.CSS_SELECTOR, '[name=message]'),
        "submit": (By.CSS_SELECTOR, '[type=submit]')
    }
    email_is_sent_message_by = (By.CSS_SELECTOR, "h3.response")
    error_message_by = (By.CSS_SELECTOR, ".form-error")

    def __init__(self, driver):
        super().__init__(driver)

    def __fill_form(self, field, content):
        self.driver.find_element(*self.form_locators[field]).send_keys(content)

    def fill_name(self, content):
        self.__fill_form('name', content)

    def fill_email(self, content):
        self.__fill_form('email', content)

    def fill_subject(self, content):
        self.__fill_form('subject', content)

    def fill_message(self, content):
        self.__fill_form('message', content)

    def click_submit(self):
        self.driver.find_element(*self.form_locators['submit']).click()

    @property
    def email_is_sent_message(self):
        return self.driver.find_element(*self.email_is_sent_message_by).text

    @property
    def form_error(self):
        return self.driver.find_element(*self.error_message_by).text
