# -*- coding: latin5 -*-
from __future__ import unicode_literals
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IsbankLogin(unittest.TestCase):


    def setUp(self):
#        self.driver = webdriver.Chrome(executable_path=r'C:\Python27\selenium\drivers\geckodriver.exe')
        self.driver = webdriver.Remote(
        command_executor="http://192.168.1.23:4444/wd/hub",
        desired_capabilities={
        "browserName": "chrome",
        })
#        self.driver = webdriver.Chrome('C:\Python27\selenium\drivers\chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")

    def test_four(self):
        driver = self.driver
        driver.get("https://www.google.org")
        time.sleep(10)

    def test_five(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        time.sleep(10)

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
