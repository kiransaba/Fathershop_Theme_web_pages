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
        sel_adv = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="출금내역관리-tab-광고인증사진내역-subtab"]')))
        sel_adv.click()
        sleep(2)
        print("advertisment_verification screen is opened")

    def open_member_details(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//a[@class='pl-4 underline'])[1]"))).click()
        sleep(2)
        print("Member details screen is opened")

    def excel_download(self):
        download_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span)[13]")))
        download_button.click()
        sleep(5)

        # Add code to verify whether the file is downloaded
        file_path = '/Users/zain/Downloads/UserDetail.xlsx'  # Change this to the actual path
        wait_time = 60  # Maximum wait time in seconds

        start_time = time()  # Use 'time()' directly, not 'self.time()'
        while not os.path.exists(file_path):
            if time() - start_time > wait_time:
                print("File download timed out")
                break
            sleep(1)

        if os.path.exists(file_path):
            print("Excel file is downloaded successfully")
        else:
            print("Excel file is not downloaded")

        self.scroll_down()

    def customer_memo_screen(self):
        customer_memo = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[class='pl-3 overflow-y-auto h-[170px] rounded border border-admin-stroke w-full styles_pre-wrap__r3a8D']")))
        customer_memo.send_keys("Memo Testing Purpose")
        sleep(2)
        print("Customer Memo is edited ")



    def save_member_details(self):
        save_details_locator = (By.XPATH, "(//div[@class='flex justify-center gap-2'])[3]")

        try:
            save_details = self.wait.until(EC.element_to_be_clickable(save_details_locator))

            # Move to the element before clicking
            ActionChains(self.driver).move_to_element(save_details).click().perform()

            sleep(2)
            print("History Mangement details are Saved")
        except Exception as e:
            print(f"Error: {e}")
            print("Save button is not functional or clickable. Details not saved.")

    def scroll_down(self):
        # Using JavaScript to scroll down the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        print("Scrolled down")


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
    history.open_member_details()
    history.excel_download()
    history.customer_memo_screen()
    history.save_member_details()
