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
        self.driver = webdriver.Chrome('C:\Python27\selenium\drivers\chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")



    def test_login_isbank_com_tr(self):
        driver = self.driver
        driver.get("http://www.isbank.com.tr/")
        self.assertIn("Türkiye İş Bankası A.Ş.", driver.title)
#        username = driver.find_element_by_id("login_login_username")
        internet_button = driver.find_element_by_xpath("//span[@class='box_font_big'][contains(text(),'Bireysel')]")
        internet_button.click()
        time.sleep(2)
        popuphandle = driver.window_handles[-1]
        driver.switch_to.window(popuphandle)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='_ctl0_MusNoText']"))
        )

        musno_text = driver.find_element_by_xpath("//input[@id='_ctl0_MusNoText']")
        # musno_text.click()
        musno_text.send_keys("183080379")
        time.sleep(10)
#        username.send_keys("student1")
#        password=driver.find_element_by_id("login_login_password")
#        password.send_keys("Testing1")
#        loginbutton=driver.find_element_by_id("login_submit")
#        loginbutton.click()
#       self.assertTrue(driver.find_element_by_link_text("Logout"),"Logout link")

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
