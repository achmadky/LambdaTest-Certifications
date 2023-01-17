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

class TestScenario2():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_scenario2(self):
    self.driver.get("https://www.lambdatest.com/selenium-playground/input-form-demo")
    self.driver.set_window_size(814, 574)
    self.driver.find_element(By.CSS_SELECTOR, ".mb-10:nth-child(4) .sp__arrow").click()
    self.driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sp__range-success > .sp__range").send_keys("95")
    self.driver.find_element(By.CSS_SELECTOR, ".sp__range-success > .sp__range").click()
    value = self.driver.find_element(By.ID, "rangeSuccess").get_attribute("value")
    assert value == "95"
    self.driver.close()
  
