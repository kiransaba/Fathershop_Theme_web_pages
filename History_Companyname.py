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

    def company_name_menu(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//a[@class='pl-4 underline'])[2]"))).click()
        sleep(2)
        print("Member details screen is opened")

    def excel_download(self):
        download_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class='!bg-admin-light border !border-admin-stroke !text-admin-main-text'])[1]")))
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

    def scroll_down(self):
        # Using JavaScript to scroll down the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        print("Scrolled down")
    def view_business_certificate(self):
      try:
        start_time = time()  # Record the start time
        wait_time = 60  # Maximum wait time in seconds

        open_certificate = self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='flex justify-center gap-2'])[1]")))
        open_certificate.click()
        sleep(2)
        print("business_certificate is opened")

        # Check for both buttons (file download and close certificate)
        buttons_checked = 0
        max_checks = 10  # Maximum number of checks
        check_interval = 2  # Interval between checks in seconds

        while buttons_checked < 2:
            try:
                # Check for file download button
                file_download_button = self.driver.find_element(By.CSS_SELECTOR, ".ant-modal-wrap")
                file_download_button.click()
                sleep(2)
                print("File download button is functional")

                buttons_checked += 1  # Increment the counter

                # Check for close certificate button
                close_certificate = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".style_button__e50TK.styles_image-download-check__jlcKz")))
                close_certificate.click()
                sleep(2)
                print("business_certificate is closed")

                buttons_checked += 1  # Increment the counter

            except Exception as e:
                print(f"Error: {e}")
                print(f"Button check failed, retrying in {check_interval} seconds")
                sleep(check_interval)

            if buttons_checked >= 2 or (buttons_checked < 2 and (time() - start_time) > wait_time):
                break  # Exit the loop if both buttons are checked or time limit is reached

        if buttons_checked < 2:
            print("Error: Buttons not functional within the time limit")
        else:
            print("Both buttons are functional")

      except TimeoutException:
           print("Timed out waiting for advertisement list inquiry element to be present.")

    def customer_memo_screen(self):
        customer_memo = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//textarea[@placeholder='메모를 입력해주세요.'])[1]")))

        customer_memo.send_keys("Memo Testing Purpose")
        sleep(2)
        print("Customer Memo is edited ")



    def save_member_details(self):
        save_details_locator = (By.XPATH, "(//button[@class='style_button__e50TK styles_save-btn__kdqqe'])[1]")

        try:
            save_details = self.wait.until(EC.element_to_be_clickable(save_details_locator))

            # Move to the element before clicking
            ActionChains(self.driver).move_to_element(save_details).click().perform()

            sleep(2)
            print("History Comapny memeber_details are Saved")
        except Exception as e:
            print(f"Error: {e}")
            print("Save button is not functional or clickable. Details not saved.")


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
    history.company_name_menu()
    history.excel_download()
    history.view_business_certificate()
    history.customer_memo_screen()
    history.save_member_details()

if __name__ == "__main__":
    pytest.main()
