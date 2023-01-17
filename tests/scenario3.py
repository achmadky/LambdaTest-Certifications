import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestScenario3():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_scenario3(self):
    self.driver.get("https://www.lambdatest.com/selenium-playground/")
    self.driver.set_window_size(814, 574)
    self.driver.execute_script("window.scrollTo(0,451)")
    self.driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
    self.driver.execute_script("window.scrollTo(0,300)")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Test")
    self.driver.find_element(By.ID, "inputEmail4").click()
    self.driver.find_element(By.ID, "inputEmail4").send_keys("test@gmail.com")
    self.driver.find_element(By.ID, "inputPassword4").click()
    self.driver.find_element(By.ID, "inputPassword4").send_keys("12345678")
    self.driver.find_element(By.ID, "company").click()
    self.driver.find_element(By.ID, "company").send_keys("test")
    self.driver.find_element(By.ID, "websitename").click()
    self.driver.find_element(By.ID, "websitename").send_keys("test.com")
    self.driver.find_element(By.NAME, "country").click()
    dropdown = self.driver.find_element(By.NAME, "country")
    dropdown.find_element(By.XPATH, "//option[. = 'United States']").click()
    self.driver.find_element(By.ID, "inputCity").send_keys("test")
    self.driver.find_element(By.ID, "inputAddress1").click()
    self.driver.find_element(By.ID, "inputAddress1").send_keys("tes")
    self.driver.find_element(By.ID, "inputAddress2").click()
    self.driver.find_element(By.ID, "inputAddress2").send_keys("tes")
    self.driver.find_element(By.ID, "inputState").click()
    self.driver.find_element(By.ID, "inputState").send_keys("tes")
    self.driver.find_element(By.ID, "inputZip").click()
    self.driver.find_element(By.ID, "inputZip").send_keys("tes")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".success-msg")
    assert len(elements) > 0
    self.driver.close()
  
