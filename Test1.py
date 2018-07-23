from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Ie('C:\Python27\selenium\drivers\IEDriverServer.exe')
#driver = webdriver.Edge('C:\Python27\selenium\drivers\MicrosoftWebDriver.exe')


driver = webdriver.Chrome('C:\Python27\selenium\drivers\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")

#driver = webdriver.Firefox(executable_path=r'C:\Python27\selenium\drivers\geckodriver.exe')
#driver.set_page_load_timeout(30)

driver.get("http://www.isbank.com.tr")
internet_button = driver.find_element_by_xpath("//span[@class='box_font_big'][contains(text(),'Bireysel')]")
internet_button.click()
time.sleep(10)

popuphandle = driver.window_handles[-1]
driver.switch_to.window(popuphandle)
#WindowHandlerID = iterator.next()
#driver.switch_to.window(WindowHandlerID)
#alert = driver.switch_to.alert()
#alert.accept()



#wait = WebDriverWait(driver, 100)
#wait.until(lambda driver: driver.current_url != "http://www.isbank.com.tr/Internet")

#wait.until(EC.new_window_is_opened)

#driver.switch_to.active_element
#driver.switch_to.window("http://www.isbank.com.tr/Internet")


#window_before = driver.window_handles[0]

#time.sleep(10)
#windows = driver.window_handles
#print(windows.count())
#for ewindow in windows:
#    print(ewindow.__getattribute__("name"))
#driver.switch_to.frame("")



#window_after = driver.window_handles[1]
#driver.switch_to.window(window_after)
#wait = WebDriverWait(driver, 100)

#wait.until(EC.frame_to_be_available_and_switch_to_it)
#ait.until(EC.presence_of_element_located((By.XPATH, "*")))

#for elm in driver.find_elements_by_class_name("loginInputContainer"):
#    print(elm.get_attribute('id'))


#driver.switch_to.window(window_after)
musno_text = driver.find_element_by_xpath("//input[@id='_ctl0_MusNoText']")
#musno_text.click()
musno_text.send_keys("183080379")
time.sleep(10)
driver.quit()