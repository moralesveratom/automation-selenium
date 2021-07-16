"""
comentar que hace el test
"""

# Importaciones de Page

# Importaciones Modulos
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import unittest
import json


class LoginCase(unittest.TestCase):
    def setUp(self):
        # Carga de JSONS
        with open(r"C:\Program Files\automation-selenium\Datos\config.json") as driver:
            self.driver_locate = json.loads(driver.read())

        with open(r"C:\Program Files\automation-selenium\Datos\config.json") as ambiente:
            self.ambiente_qa = json.loads(ambiente.read())

        with open(r"C:\Program Files\automation-selenium\Datos\usuarios.json") as usuario:
            self.diccionario_usuario = json.loads(usuario.read())

        # Config del driver
        options = Options()
        options.add_argument("--start-maximized")  # "--headless"
        self.driver = webdriver.Chrome(self.driver_locate["driver"], options=options)

        self.driver.get(self.ambiente_qa["ambiente"])
        self.driver.implicitly_wait(5)

        # Config de Pages

    def test_ejemplo(self):
        self.assertNotEqual(True, False)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
