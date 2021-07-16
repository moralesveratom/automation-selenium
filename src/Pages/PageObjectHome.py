"""
busca 'item'
"""

# Importaciones Modulos
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageObjectHome:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.click_search_bar = (By.ID, 'search_query_top')
        self.click_search_button = (By.NAME, 'submit_search')

    def search_item(self, item):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.click_search_bar)).click().send_keys(item)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.click_search_button)).click()
