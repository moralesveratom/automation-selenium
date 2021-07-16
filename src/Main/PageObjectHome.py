"""
comentar que hace el page
"""

# Importaciones Modulos
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageObject:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.element_box = (By.ID, '')
        self.submit_box = (By.ID, '')

    def click_submit(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.submit_box)).click()

    def send(self, element):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.element_box)).send_keys(element)