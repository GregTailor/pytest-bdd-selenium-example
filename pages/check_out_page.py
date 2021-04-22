from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.page import Page


class CheckOutPage(Page):

    form_locators = {
        "email": (By.ID, 'email'),
        "name": (By.ID, 'name'),
        "address": (By.ID, 'address'),
        "card_type_dropdown": (By.ID, 'card_type'),
        "card_number": (By.ID, 'card_number'),
        "cardholder_name": (By.ID, 'cardholder_name'),
        "verification_code": (By.ID, 'verification_code'),
    }
    error_message_by = (By.CSS_SELECTOR, ".form-error")

    def __init__(self, driver):
        super().__init__(driver)

    def __fill_form(self, field, content):
        self.driver.find_element(*self.form_locators[field]).send_keys(content)

    def fill_email(self, content):
        self.__fill_form('email', content)

    def fill_name(self, content):
        self.__fill_form('name', content)

    def fill_address(self, content):
        self.__fill_form('address', content)

    def fill_card_type_dropdown(self, content):
        self.__fill_form('card_type_dropdown', content)

    def fill_card_number(self, content):
        self.__fill_form('card_number', content)

    def fill_cardholder_name(self, content):
        self.__fill_form('cardholder_name', content)

    def fill_verification_code(self, content):
        self.__fill_form('verification_code', content)

    def select_card_type(self, card_type):
        try:
            select = Select(self.driver.find_element(*self.form_locators['card_type_dropdown']))
            select.select_by_visible_text(card_type)
        except NoSuchElementException:
            pass

    @property
    def form_error(self):
        return self.driver.find_element(*self.error_message_by).text
