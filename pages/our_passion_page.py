from selenium.webdriver.common.by import By

from pages.page import Page


class OurPassionPage(Page):

    title_one_by = (By.CSS_SELECTOR, 'div.txt h1')
    title_two_by = (By.CSS_SELECTOR, 'div.txt h2.editor_h1')

    def __init__(self, driver):
        super().__init__(driver)

    def title_one(self):
        return self.driver.find_element(*self.title_one_by)

    def title_two(self):
        return self.driver.find_element(*self.title_two_by)
