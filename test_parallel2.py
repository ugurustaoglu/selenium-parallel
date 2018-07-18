import unittest
import wd.parallel
from time import sleep
from selenium import webdriver
import copy


class TestParallel(unittest.TestCase):

    def setUp(self):
        desired_capabilities = [
            webdriver.DesiredCapabilities.FIREFOX,
            webdriver.DesiredCapabilities.FIREFOX,
            webdriver.DesiredCapabilities.CHROME
        ]

        self.drivers = wd.parallel.Remote(
            desired_capabilities=desired_capabilities
        )
        self.drivers.load_config_file("/root/PycharmProjects/paralleltests/venv/config.json")
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub"
        )

    @wd.parallel.multiply
    def test_sauce(self):
        self.driver.get('http://saucelabs.com/test/guinea-pig')
        self.assertTrue("I am a page title - Sauce Labs" in self.driver.title)
        self.driver.find_element_by_id('comments').send_keys(
            'Hello! I am some example comments. I should appear in the page after you submit the form')
        self.driver.find_element_by_id('submit').click()

        comments = self.driver.find_element_by_id('your_comments')
        self.assertTrue(
            'Your comments: Hello! I am some example comments. I should appear in the page after you submit the form' in comments.text)
        body = self.driver.find_element_by_xpath('//body')
        self.assertFalse('I am some other page content' in body.text)
        self.driver.find_elements_by_link_text('i am a link')[0].click()
        body = self.driver.find_element_by_xpath('//body')
        self.assertTrue('I am some other page content' in body.text)

    @wd.parallel.multiply
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
