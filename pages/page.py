from selenium.webdriver.common.by import By


class Page:

    welcome_page_by = (By.CSS_SELECTOR, 'a[data-title="Welcome"]')
    our_passion_page_by = (By.CSS_SELECTOR, 'a[data-title="Our Passion"]')
    menu_page_by = (By.CSS_SELECTOR, 'a[data-title="Menu"]')
    lets_talk_tea_page_by = (By.CSS_SELECTOR, 'a[data-title="Let\'s Talk Tea"]')
    check_out_page_by = (By.CSS_SELECTOR, 'a[data-title="Check Out"]')

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_welcome_page(self):
        self.driver.find_element(*self.welcome_page_by).click()

    def navigate_to_our_passion_page(self):
        self.driver.find_element(*self.our_passion_page_by).click()

    def navigate_to_menu_page(self):
        self.driver.find_element(*self.menu_page_by).click()

    def navigate_to_lets_talk_tea_page(self):
        self.driver.find_element(*self.lets_talk_tea_page_by).click()

    def navigate_to_check_out_page(self):
        self.driver.find_element(*self.check_out_page_by).click()
