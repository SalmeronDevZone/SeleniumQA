import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TestGoogleSearch(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()


    def test_google_search(self):

        driver = self.driver
        driver.get("https://www.google.es")
        self.assertIn("Google", driver.title)  # Corregido: "google" -> "Google"
        search_box = driver.find_element_by_name("q")  # Corregido: elem -> search_box
        search_box.send_keys("selenium")
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)  # Corregido: 10 -> 5
        assert "No se encontró el elemento" not in driver.page_source  # Corregido: "No se encontro el elemento" -> "No se encontró el elemento"


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
