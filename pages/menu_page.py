from selenium.webdriver.common.by import By

from pages.page import Page


class MenuPage(Page):

    check_out_button_one_by = (By.ID, 'wsb-button-00000000-0000-0000-0000-000451955160')
    check_out_button_two_by = (By.ID, 'wsb-button-00000000-0000-0000-0000-000451959280')
    check_out_button_three_by = (By.ID, 'wsb-button-00000000-0000-0000-0000-000451961556')

    def __init__(self, driver):
        super().__init__(driver)

    def check_out_button_one(self):
        return self.driver.find_element(*self.check_out_button_one_by)

    def check_out_button_two(self):
        return self.driver.find_element(*self.check_out_button_two_by)

    def check_out_button_three(self):
        return self.driver.find_element(*self.check_out_button_three_by)
