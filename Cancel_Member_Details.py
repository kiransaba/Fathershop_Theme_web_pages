import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, time

import os
from time import sleep, time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    class LoginPage:
        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 20)

        def login(self, username, password):
            try:
                ID = self.wait.until(EC.presence_of_element_located((By.NAME, 'username')))
                ID.send_keys(username)
                sleep(2)
                print('Username')
            except TimeoutException:
                print("Timed out waiting for username element to be present.")
                return False

            try:
                Password = self.wait.until(EC.presence_of_element_located((By.NAME, 'password')))
                Password.send_keys(password)
                sleep(2)
                print('Password')
            except TimeoutException:
                print("Timed out waiting for password element to be present.")
                return False

            try:
                login_button = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".flex.justify-center.gap-2")))
                login_button.click()
                sleep(3)
                print('Icarus Advertisement Admin Dashboard screen is opened successfully')
            except TimeoutException:
                print("Timed out waiting for login button to be clickable.")
                return False

            return True

class MemberListPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_member_list_inquiry(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'회원관리')]"))).click()
        sleep(2)
        print("Membership Management Drop-down Menu is showing")

    def open_member_details(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='krnsaba@gmail.com']"))).click()
        sleep(2)
        print("Member details screen is opened")

        self.scroll_down()

    def scroll_down(self):
        # Using JavaScript to scroll down the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        print("Scrolled down the page")

    def Cancel_Member_details(self):
        cancel_details_locator = (By.XPATH, "(//button[@class='style_button__e50TK styles_cancel-btn__8lQtL'])[1]")

        try:
            save_details = self.wait.until(EC.visibility_of_element_located(cancel_details_locator))
            save_details = self.wait.until(EC.element_to_be_clickable(cancel_details_locator))
            save_details.click()
            sleep(5)
            print("Member details page is cancelled")
        except Exception as e:
            print(f"Error: {e}")
            print("Cancel button is not functional or clickable. Details not cancelled.")

# Pytest fixture for setting up and tearing down the driver
@pytest.fixture
def driver_setup():
    chrome_driver_path = '/Users/zain/Downloads/chromedriver'
    driver = webdriver.Chrome()
    driver.get('https://advertiser-admin.icarus.mufin.lol/login')
    driver.maximize_window()
    yield driver
    driver.quit()

# Pytest function for testing login and member list page
def test_login_and_member_list(driver_setup):
    driver = driver_setup

    login_page = LoginPage(driver)
    login_page.login('admin_advertiser', 'Icarus@123')

    member_list_page = MemberListPage(driver)
    member_list_page.open_member_list_inquiry()
    member_list_page.open_member_details()

    member_list_page.Cancel_Member_details()

if __name__ == "__main__":
    pytest.main()
