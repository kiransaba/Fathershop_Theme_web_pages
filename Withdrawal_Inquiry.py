import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
            print('Password')
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


class WithdrawalPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_member_management_dropdown(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'회원관리')]"))).click()
        sleep(2)
        print("Membership Management Drop-down Menu is showing")

    def open_withdrawal_member_inquiry(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//a[contains(text(),'탈퇴회원조회')])[1]"))).click()
        sleep(2)
        print("Withdrawal_Member Inquiry screen is opened")

        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='underline text-[#1D2025]']"))).click()
        sleep(5)
        print("Withdrawal Member list screen is opened")

    def excel_download(self):
        download_button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[@class='!bg-admin-light border !border-admin-stroke !text-admin-main-text']")))
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

    def Customer_Memo_Screen(self):

        Customer_Memo = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='메모를 입력해주세요.']")))
        Customer_Memo.send_keys("Memo Testing Purpose")
        sleep(2)
        print("Customer Memo is edited ")

        self.scroll_down()

        Check_Memo_History = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='flex justify-center gap-2'])[1]")))
        Check_Memo_History.click()
        sleep(2)
        print("Customer Memo History Screen is opened ")

        close_memo = self.wait.until(EC.presence_of_element_located((By.XPATH,"(//*[name()='svg'][@fill-rule='evenodd'])[1]")))
        close_memo.click()
        sleep(3)
        print("Memo is closed")

    def scroll_down(self):
        # Using JavaScript to scroll down the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        print("Scrolled down the page")

    def save_withdrawal_details(self):
        save_details = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='flex justify-center gap-2'])[3]")))
        save_details.click()
        sleep(5)
        print("Withdrawal details are Saved ")


# Pytest fixture for setting up and tearing down the driver
@pytest.fixture
def driver_setup():
    chrome_driver_path = '/Users/zain/Downloads/chromedriver'
    driver = webdriver.Chrome()
    driver.get('https://advertiser-admin.icarus.mufin.lol/login')
    driver.maximize_window()
    yield driver
    driver.quit()


# Pytest function for testing login and withdrawal page
def test_login_and_withdrawal_page(driver_setup):
    driver = driver_setup

    login_page = LoginPage(driver)
    login_page.login('admin_advertiser', 'Icarus@123')

    withdrawal_page = WithdrawalPage(driver)
    withdrawal_page.open_member_management_dropdown()
    withdrawal_page.open_withdrawal_member_inquiry()
    withdrawal_page.excel_download()
    withdrawal_page.Customer_Memo_Screen()
    withdrawal_page.save_withdrawal_details()


if __name__ == "__main__":
    pytest.main()
