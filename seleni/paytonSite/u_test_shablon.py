from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time


class TestMainPage(unittest.TestCase):

    def setUp(self):#перед началом каждого теста
        self.driver = webdriver.Chrome()  # подключаем драйвер
        self.driver.get("https://www.python.org/")


    def test_search(self):
        driver = self.driver
        driver.find_element(By.ID, "id-search-field").click()
        driver.find_element(By.ID, "id-search-field").clear()
        driver.find_element(By.ID, "id-search-field").send_keys("pycon")
        driver.find_element(By.ID, "submit").click()
        time.sleep(3)


    def tearDowan(self):
        self.driver.close()#закрывает окно браузера #/quit -вкладку