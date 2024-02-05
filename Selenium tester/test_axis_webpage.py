"""
for i in range(10):
        for x in e:
            print(x.screenshot("C:/Users/SuvDul/Documents/Examensarbete/Selenium tester/screenshots/elementscsh.png"))'
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

AXIS_SITE = "https://www.axis.com/"
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome()

driver.implicitly_wait(5)

def test_axis_homepage():
    
    # Navigate to Axis homepage
    driver.get(AXIS_SITE)
    # Find popup
    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")
    # Click on popup
    popup.click()
    # Save homepage title in variabel titel
    title = driver.title
    time.sleep(3)
    # Verify that title contains the word Axis
    assert "Axis" in title
    
    driver.close()

def test_solutions_page_link():

    driver.get(AXIS_SITE)

    #ids = driver.find_elements(By.XPATH, ('//*[@id]'))

    #for ii in ids:
    #    print (ii.get_attribute('id'))

    # Find popup
    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")
    # Click on popup
    popup.click()

    #eee = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    driver.find_element(By.LINK_TEXT, "SOLUTIONS").click()

    solutions_header = driver.find_element(By.TAG_NAME, "h1").text

    #assert False, "Check print"

    assert solutions_header == "Solutions"

def test_products_page_link():

    driver.get(AXIS_SITE)

    # Find popup
    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")
    # Click on popup
    popup.click()

    driver.find_element(By.LINK_TEXT, "PRODUCTS").click()

    products_header = driver.find_element(By.TAG_NAME, "h1").text

    assert products_header == "Products"


    







