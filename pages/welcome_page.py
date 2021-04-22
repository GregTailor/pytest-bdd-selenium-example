from selenium.webdriver.common.by import By

from pages.page import Page


class WelcomePage(Page):

    url = "http://www.practiceselenium.com/"

    big_logo_by = (By.XPATH, '//*[@id="wsb-element-00000000-0000-0000-0000-000450914885"]/div/div/img')
    title_by = (By.CSS_SELECTOR, 'div.txt h1')
    description_by = (By.CSS_SELECTOR, 'div.txt p span')
    see_collection_one_by = (By.ID, 'wsb-button-00000000-0000-0000-0000-000450914890')
    see_collection_two_by = (By.ID, 'wsb-button-00000000-0000-0000-0000-000450914897')
    see_collection_three_by = (By.ID, 'wsb-button-00000000-0000-0000-0000-000450914899')

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(self.url)

    def big_logo(self):
        return self.driver.find_element(*self.big_logo_by)

    def title(self):
        return self.driver.find_element(*self.title_by)

    def desciption(self):
        return self.driver.find_element(*self.description_by)

    def see_collection(self, position):
        if position == 1:
            return self.driver.find_element(*self.see_collection_one_by)
        if position == 2:
            return self.driver.find_element(*self.see_collection_two_by)
        if position == 3:
            return self.driver.find_element(*self.see_collection_three_by)
