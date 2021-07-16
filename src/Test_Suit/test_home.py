"""
comentar que hace el test
"""

# Importaciones de Page
from src.Pages.PageObjectHome import PageObjectHome

# Importaciones Modulos
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import unittest
import json


class LoginCase(unittest.TestCase):
    def setUp(self):
        # Carga de JSONS
        with open(r"C:\Users\Administrator\Desktop\proyectos\automation-selenium\src\Datos\config.json") as driver:
            self.driver_locate = json.loads(driver.read())

        with open(r"C:\Users\Administrator\Desktop\proyectos\automation-selenium\src\Datos\config.json") as ambiente:
            self.ambiente_qa = json.loads(ambiente.read())

        # Config del driver
        options = Options()
        options.add_argument("--start-maximized")  # "--headless"
        self.driver = webdriver.Chrome(self.driver_locate["driver"], options=options)

        self.driver.get(self.ambiente_qa["ambiente"][0])
        self.driver.implicitly_wait(5)

        # Config de Pages
        self.page_home = PageObjectHome(self.driver)

    def test_busqueda_exitosa(self):
        self.page_home.search_item('dress')
        resultado_busqueda = self.driver.find_elements_by_class_name('product-count')
        self.assertEqual('Showing 1 - 7 of 7 items', resultado_busqueda.text)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
