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

class TestScenario1():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_Scenario1(self):
    self.driver.get("https://www.lambdatest.com/selenium-playground/")
    self.driver.set_window_size(814, 574)
    self.driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
    current_url = driver.current_url
    assert current_url == "https://www.lambdatest.com/selenium-playground/simple-form-demo", f"Expected URL: https://www.lambdatest.com/selenium-playground/simple-form-demo but got {current_url}"
    Welcome = "Welcome to LambdaTest"
    self.driver.find_element(By.ID, "user-message").send_keys(Welcome)
    self.driver.find_element(By.ID, "showInput").click()
    message = self.driver.find_element(By.XPATH, '//*[@id="message"]')
    assert message.text == Welcome
    self.driver.close()
  
