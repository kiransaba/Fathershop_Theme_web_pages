import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, time
import os

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        ID = self.wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        ID.send_keys(username)
        sleep(2)
        print('Username')
        Password = self.wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        Password.send_keys(password)
        sleep(2)
        print('Password')
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".flex.justify-center.gap-2")))
        login_button.click()
        sleep(5)
        print('Icarus Advertisement Admin Dashboard screen is opened successfully')

class History:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_history_management(self):
        dropdown = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="출금내역관리-tab"]')))
        dropdown.click()
        sleep(2)
        print("history_management Drop-down Menu is showing")

    def open_advertisment_verification(self):
        sel_adv = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="출금내역관리-tab-광고인증사진내역-subtab"]')))
        sel_adv.click()
        sleep(2)
        print("advertisment_verification screen is opened")

    def vehicle_menu(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'0원')])[1]"))).click()
        sleep(3)
        print("Number of vehicle screen is opened")

        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@fill-rule='evenodd'])[2]"))).click()
        sleep(3)
        print("Number of vehicle screen is closed")

@pytest.fixture
def driver_setup():
    chrome_driver_path = '/Users/zain/Downloads/chromedriver'
    driver = webdriver.Chrome()
    driver.get('https://advertiser-admin.icarus.mufin.lol/login')
    driver.maximize_window()
    yield driver
    driver.quit()

# Pytest function for testing login and member list page
def test_login_and_history_management(driver_setup):
    driver = driver_setup

    login_page = LoginPage(driver)
    login_page.login('admin_advertiser', 'Icarus@123')

    history = History(driver)
    history.open_history_management()
    history.open_advertisment_verification()
    history.vehicle_menu()

if __name__ == "__main__":
    pytest.main()
