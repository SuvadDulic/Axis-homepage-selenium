import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
#class TestAxisWebpage:


def test_axis_homepage(driver):

    # Verify that title contains the word Axis
    assert "Axis" in driver.title

def test_solutions_page_link(driver):

    # Find popup
    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")
    # Click on popup
    popup.click()
    # Find link to Solutions page and Click it
    driver.find_element(By.LINK_TEXT, "SOLUTIONS").click()
    # Find the page header and save the text
    solutions_header = driver.find_element(By.TAG_NAME, "h1").text
    # Verify that page header referes to right page
    assert solutions_header == "Solutions"

def test_products_page_link(driver):

    # Find popup
    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")
    # Click on popup
    popup.click()

    driver.find_element(By.LINK_TEXT, "PRODUCTS").click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert page_header == "Products"

def test_learning_page_link(driver):

    # Find popup
    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")
    # Click on popup
    popup.click()

    driver.find_element(By.LINK_TEXT, "LEARNING").click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert page_header == "Learning"

def test_support_page_link(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    driver.find_element(By.LINK_TEXT, "SUPPORT").click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert "support" in page_header

def test_partner_page_link(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    driver.find_element(By.LINK_TEXT, "PARTNER").click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert "partner" in page_header

def test_wheretobuy_page_link(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    driver.find_element(By.LINK_TEXT, "WHERE TO BUY").click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert page_header == "Where to buy"

def test_newsroom_page_link(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    actions = ActionChains(driver)

    actions.move_to_element(driver.find_element(By.CLASS_NAME, "home-page__trends-insights-newsroom-link")).perform()

    driver.find_element(By.CLASS_NAME, "home-page__trends-insights-newsroom-link").click()

    page_header = driver.find_element(By.CLASS_NAME, "acn-header__title").text

    assert page_header == "Newsroom"

def test_contact_page_link(driver):

   popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

   popup.click()

   driver.find_element(By.CSS_SELECTOR, "a[aria-label='contact us']").click()
   
   page_header = driver.find_element(By.TAG_NAME, "h1").text

   assert page_header == "Contact us"

def test_login_page_link(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    driver.find_element(By.CSS_SELECTOR, "a[aria-label='log in']").click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert page_header == "Sign in"

def test_login_register_page_link(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    driver.find_element(By.CSS_SELECTOR, "a[aria-label='log in']").click()

    driver.find_element(By.ID, "reg-link").click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert page_header == "Create Account"

def test_login_forgot_password_page_link(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    driver.find_element(By.CSS_SELECTOR, "a[aria-label='log in']").click()

    driver.find_element(By.ID, "forgot-link").click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert page_header == "Reset password"

def test_axis_homepage_search_bar(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    searchbar = driver.find_element(By.NAME, "search")

    searchbar.send_keys("camera")

    driver.find_element(By.CLASS_NAME, "gsc-search-button-v2").click()

    elem = driver.find_elements(By.CLASS_NAME, "gs-title")

    elem[1].click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert "cameras" in page_header

def test_customerstory_page_link(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    actions = ActionChains(driver)

    actions.move_to_element(driver.find_element(By.LINK_TEXT, "About us")).perform()

    driver.find_element(By.LINK_TEXT, "VIEW ALL CUSTOMER STORIES").click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert page_header == "Customer stories"

def test_corpgover_page_link(driver):
    
    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    actions = ActionChains(driver)

    actions.move_to_element(driver.find_element(By.LINK_TEXT, "Quality")).perform()

    driver.find_element(By.LINK_TEXT, "Corporate governance").click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert page_header == "Corporate governance"

def test_sustainabilitiy_page_link(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    actions = ActionChains(driver)

    actions.move_to_element(driver.find_element(By.LINK_TEXT, "Quality")).perform()

    driver.find_element(By.LINK_TEXT, "Sustainability").click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert page_header == "Sustainability at Axis"

def test_experience_center_page_link(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    actions = ActionChains(driver)

    actions.move_to_element(driver.find_element(By.LINK_TEXT, "Quality")).perform()

    driver.find_element(By.LINK_TEXT, "Experience Center").click()

    page_header = driver.find_element(By.TAG_NAME, "h1").text

    assert "Experience Center" in page_header

def test_cookies_settings_popup(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    WebDriverWait(driver, 5).until_not(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Only Necessary')]"))
    )

    cookie_settings_present = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]").is_displayed()

    if cookie_settings_present:

        assert False, "Cookie settings popup still present"

    actions = ActionChains(driver)

    actions.move_to_element(driver.find_element(By.LINK_TEXT, "Cookie settings")).perform()

    driver.find_element(By.LINK_TEXT, "Cookie settings").click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Only Necessary')]"))
    )

    cookie_settings_present = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]").is_displayed()

    if cookie_settings_present:

        assert True, "Cookie settings popup is present"

    elif cookie_settings_present == False:

        assert False, "Cookie settings did not appear"

def test_change_language_swedish(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    english_header = driver.find_element(By.XPATH, "//*[contains(text(), 'Discover smart solutions')]").text
    
    assert "Discover" in english_header

    actions = ActionChains(driver)

    actions.move_to_element(driver.find_element(By.LINK_TEXT, "Cookie settings")).perform()

    driver.find_element(By.CLASS_NAME, "languageswitcher__toggle").click()

    actions.move_to_element(driver.find_element(By.LINK_TEXT, "Europe")).perform()

    driver.find_element(By.LINK_TEXT, "Europe").click()

    driver.find_element(By.LINK_TEXT, "Svenska").click()

    swedish_header = driver.find_element(By.XPATH, "//*[contains(text(), 'Upptäck smarta lösningar')]").text

    assert "Upptäck" in swedish_header

def test_country_contact_info(driver):

    popup = driver.find_element(By.XPATH, "//*[contains(text(), 'Only Necessary')]")

    popup.click()

    actions = ActionChains(driver)

    driver.find_element(By.CSS_SELECTOR, "a[aria-label='contact us']").click()

    h2_elem = driver.find_element(By.XPATH, "//*[contains(text(), 'Get in touch')]")

    actions.move_to_element(h2_elem).perform()

    country_dropdown = driver.find_element(By.NAME, "field_country_region_target_id")

    select = Select(country_dropdown)

    select.select_by_visible_text('Sweden')

    country_info = driver.find_elements(By.CLASS_NAME, "field-content")

    country_info_sweden = country_info[0]

    assert "Sweden, Lund" in country_info_sweden.text