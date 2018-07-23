from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest, os
from datetime import datetime

driver = webdriver.Chrome('C:\Python27\selenium\drivers\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")

def findElement(self, webDriver, windowId, frameId, selectorType, selectorText):
    if windowId != self.currentWindowId:
        windows = webDriver.get_window_handles()
        webDriver.switch_to.window(windows[windowId - 1])
        self.currentWindowId = self.windowId

    if frameId == -1:
        webDriver.switch_to.default_content()
        self.currentFrameId = -1
    elif self.currentFrameId != frameId:
        webDriver.switch_to.frame(frameId)
        self.currentFrameId = frameId

    if selectorType == 'css':
        return WebDriverWait(webDriver, self.timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selectorText)))
    elif selectorType == 'id':
        return WebDriverWait(webDriver, self.timeout).until(EC.presence_of_element_located((By.ID, selectorText)))
    elif selectorType == 'name':
        return WebDriverWait(webDriver, self.timeout).until(EC.presence_of_element_located((By.NAME, selectorText)))
    elif selectorType == 'class':
        return WebDriverWait(webDriver, self.timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, selectorText)))
    elif selectorType == 'link':
        return WebDriverWait(webDriver, self.timeout).until(
            EC.presence_of_element_located((By.LINK_TEXT, selectorText)))
    elif selectorType == 'tag':
        return WebDriverWait(webDriver, self.timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, selectorText)))
    elif selectorType == 'xpath':
        return WebDriverWait(webDriver, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, selectorText)))

    return None

def setAttribute(self, webDriver, element, attribute, value):
    webDriver.execute_script('arguments[0].setAttribute(arguments[1], arguments[2])', element, attribute, value)

def selectFromDropDownByIndex(self, element, index):
    if element.get_attribute('multiple') != None:
        optionElements = element.find_elements(By.TAG_NAME, 'option')
        if len(optionElements) > 0:
            optionElements[index].click()
        else:
            Select(element).select_by_index(index)
    else:
        Select(element).select_by_index(index)


    try:

        self.webDriver.get('http://www.isbank.com.tr')

        self.findElement(self.webDriver, 1, -1, 'css',
                             '#IbInterActive > DIV:nth-child(3) > A:nth-child(1) > SPAN:nth-child(1)').click()

        self.webDriver.execute_script('arguments[0].blur();', self.findElement(self.webDriver, 2, -1, 'css',
                                                                                   'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(3) > DIV:nth-child(2) > DIV:nth-child(2) > DIV:nth-child(2) > INPUT:nth-child(1)'))

        self.webDriver.execute_script('arguments[0].focus();', self.findElement(self.webDriver, 2, -1, 'css',
                                                                                    'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(3) > DIV:nth-child(2) > DIV:nth-child(2) > DIV:nth-child(2) > INPUT:nth-child(1)'))

        self.webDriver.execute_script('arguments[0].focus();',
                                          self.findElement(self.webDriver, 2, -1, 'id', '_ctl0_MusNoText'))

        self.webDriver.execute_script('arguments[0].blur();', self.findElement(self.webDriver, 2, -1, 'css',
                                                                                   'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(3) > DIV:nth-child(2) > DIV:nth-child(2) > DIV:nth-child(2) > INPUT:nth-child(1)'))

        self.webDriver.execute_script('arguments[0].blur();',
                                          self.findElement(self.webDriver, 2, -1, 'id', '_ctl0_MusNoText'))

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > DIV:nth-child(50) > DIV:nth-child(1) > DIV:nth-child(3) > A:nth-child(2) > P:nth-child(1)').click()

        self.webDriver.execute_script('arguments[0].blur();',
                                          self.findElement(self.webDriver, 2, -1, 'id', '_ctl0_MusNoText'))

        self.webDriver.execute_script('arguments[0].focus();', self.findElement(self.webDriver, 2, -1, 'css',
                                                                                    'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(3) > DIV:nth-child(2) > DIV:nth-child(2) > DIV:nth-child(2) > INPUT:nth-child(1)'))

        assert len(self.webDriver.find_elements_by_css_selector('#_ctl0_MusNoText')) > 0

        self.webDriver.execute_script('arguments[0].blur();', self.findElement(self.webDriver, 2, -1, 'css',
                                                                                   'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(3) > DIV:nth-child(2) > DIV:nth-child(2) > DIV:nth-child(2) > INPUT:nth-child(1)'))

        self.webDriver.execute_script('arguments[0].blur();',
                                          self.findElement(self.webDriver, 2, -1, 'id', '_ctl0_MusNoText'))

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(4) > BUTTON:nth-child(1)').click()

        self.findElement(self.webDriver, 2, -1, 'id', '_ctl0_SubeLogin01_btnGiris').click()

        self.webDriver.execute_script('arguments[0].focus();', self.findElement(self.webDriver, 2, -1, 'css',
                                                                                    'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)'))

        self.webDriver.execute_script('arguments[0].focus();',
                                          self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText'))

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '+')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('+')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('0')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '0')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '!')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('!')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('|')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '|')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('%')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '/')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('/')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '#')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('}')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys(';')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                ':')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys(',')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '1')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('0')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('0')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '=')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys(']')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '4')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('/')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '{')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '0')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('0')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '5')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('5')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '`')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('`')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '@')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('@')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '3')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('3')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(''')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys(''')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys(';')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                ';')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '!')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('!')

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)').send_keys(
                '{')

        self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText').send_keys('$')

        self.webDriver.execute_script('arguments[0].blur();',
                                          self.findElement(self.webDriver, 2, -1, 'id', 'ParolaText'))

        self.webDriver.execute_script('arguments[0].blur();', self.findElement(self.webDriver, 2, -1, 'css',
                                                                                   'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(2) > INPUT:nth-child(1)'))

        self.findElement(self.webDriver, 2, -1, 'id', '_ctl0_SubeLogin01_btnGiris').click()

        self.findElement(self.webDriver, 2, -1, 'css',
                             'HTML > BODY:nth-child(2) > FORM:nth-child(44) > DIV:nth-child(14) > DIV:nth-child(4) > DIV:nth-child(2) > DIV:nth-child(1) > SPAN:nth-child(1) > DIV:nth-child(14) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(1) > DIV:nth-child(4) > DIV:nth-child(4) > BUTTON:nth-child(1)').click()

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('#')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('-')

        self.webDriver.execute_script('arguments[0].blur();',
                                          self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar'))

        assert len(self.webDriver.find_elements_by_css_selector('#oneTimePasswordCepAnahtar')) > 0

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('6')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('!')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('2')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('4')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('/')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('=')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('\\')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('(')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('7')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('$')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('"')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('2')

        self.webDriver.execute_script('arguments[0].blur();',
                                          self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar'))

        self.webDriver.execute_script('arguments[0].focus();',
                                          self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar'))

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys(')')

        self.findElement(self.webDriver, 3, -1, 'id', 'oneTimePasswordCepAnahtar').send_keys('%')

        self.webDriver.quit()
