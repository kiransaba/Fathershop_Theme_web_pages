import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from time import sleep, time
import os


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
            print('Password is saved ')
        except TimeoutException:
            print("Timed out waiting for password element to be present.")
            return False

        try:
            login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".flex.justify-center.gap-2")))
            login_button.click()
            sleep(3)
            print('Icarus Advertisement Admin Dashboard screen is opened successfully')
        except TimeoutException:
            print("Timed out waiting for login button to be clickable.")
            return False

        return True


class AvdertisingListPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_advertisement_list_Inquiry(self):
        try:
            open_advertisement = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="광고관리-tab"]')))
            open_advertisement.click()
            sleep(5)
            print("Advertising Management Drop-down Menu is showing")
        except TimeoutException:
            print("Timed out waiting for advertisement list inquiry element to be present.")

    def select_advertisement_list(self):
        try:
            select_advertisement = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="광고관리-tab"]')))
            select_advertisement.click()
            sleep(5)
            print("Advertisement list inquiry is selected")
        except TimeoutException:
            print("Timed out waiting for select advertisement list element to be present.")

    def select_advertisemt_order(self):
        # Increase the timeout to 20 seconds
        try:
            advertisement_order_dropdown = self.wait.until( EC.presence_of_element_located((By.XPATH, "//input[@id='rc_select_1']")), timeout=20)
            advertisement_order_dropdown.click()
            sleep(10)
            print("Opened")
        except TimeoutException:
            print("Timed out waiting for select advertisement list element to be present.")

    def change_advertisemnt_status(self):
        try:
            select_adv = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[12]")))
            select_adv.click()
            sleep(2)
            print("Advertisement checkmark is selected")

            change_adv_status = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='flex justify-center gap-2'])[4]")))
            change_adv_status.click()
            sleep(2)
            print("change_adv_status drop-down is selected")

            select_adv_status_option = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='recruiting_cargo_owners']")))
            select_adv_status_option.click()
            sleep(2)
            print("change_adv_status option is selected")

            save_adv_status_option = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='flex justify-center gap-2'])[6]")))
            save_adv_status_option.click()
            sleep(5)
            print("change_adv_status option is saved")


        except TimeoutException:
            print("Timed out waiting for select advertisement list element to be present.")

            self.scroll_down()

    def scroll_down(self):
            # Using JavaScript to scroll down the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(5)
            print("Scrolled down")




@pytest.fixture
def driver_setup():
    chrome_driver_path = '/Users/zain/Downloads/chromedriver' #(gve your chrome_driver path)
    driver = webdriver.Chrome()
    driver.get('https://advertiser-admin.icarus.mufin.lol/login')
    driver.maximize_window()
    yield driver
    driver.quit()


# Pytest function for testing login and withdrawal page
def test_login_and_advertising_management(driver_setup):
    driver = driver_setup

    login_page = LoginPage(driver)
    login_page.login('admin_advertiser', 'Icarus@123')

    advertising = AvdertisingListPage(driver)
    advertising.open_advertisement_list_Inquiry()
    advertising.select_advertisement_list()
    #advertising.excel_download()
    #advertising.select_advertisemt_order()
    advertising.change_advertisemnt_status()


if __name__ == "__main__":
    pytest.main()
