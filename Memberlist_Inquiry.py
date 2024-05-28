import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

from time import sleep, time

import os
from time import sleep, time
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
class MemberListPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_member_list_inquiry(self):
      try:
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'회원관리')]"))).click()
        sleep(2)
        print("Membership Management Drop-down Menu is showing")
      except TimeoutException:
            print("Timed out waiting for advertisement list inquiry element to be present.")

    def open_member_details(self):
      try:
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='krnsaba@gmail.com']"))).click()
        sleep(2)
        print("Member details screen is opened")

      except TimeoutException:
        print("Timed out waiting for advertisement list inquiry element to be present.")

    def excel_download(self):
      try:
        download_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='!bg-admin-light border !border-admin-stroke !text-admin-main-text']")))
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

      except TimeoutException:
          print("Timed out waiting for advertisement list inquiry element to be present.")

    def edit_details(self):

        Company_number = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#company_phone_number")))
        Company_number.send_keys("03335963657")
        sleep(2)
        print("Contact number is edited")

        Manager = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#manager")))
        Manager.send_keys("Hong Gil Dong")
        sleep(2)
        print("Manager name is edited")

        print("Before waiting for Mobile_no element")

        #Mobile_no = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#contact_person_mobile_number")))
        #Mobile_no.send_keys("03316292999")
        #sleep(2)
        #print("After waiting for Mobile_no element")
        #print("Mobile number is edited")


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

    def Customer_Memo_Screen(self):

        Customer_Memo = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='메모를 입력해주세요.']")))
        Customer_Memo.send_keys("Memo Testing Purpose")
        sleep(2)
        print("Customer Memo is edited ")

        self.scroll_down()


        Check_Memo_History= self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='flex justify-center gap-2'])[2]")))
        Check_Memo_History.click()
        sleep(2)
        print("Customer Memo History Screen is opened ")



    def close_Memo(self):

        try:
            close_memo_locator = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@fill-rule='evenodd'])[1]"))
            )

            close_memo_locator.click()

            sleep(3)
            print("Customer Memo History Screen is closed successfully")
        except Exception as e:
            print(f"Error: {e}")
            print("Close Memo button is not functional or clickable. Memo history screen not closed.")

    def Save_Member_details(self):
        save_details_locator = (By.XPATH, "(//div[@class='flex justify-center gap-2'])[3]")

        try:
            save_details = self.wait.until(EC.element_to_be_clickable(save_details_locator))

            # Move to the element before clicking
            ActionChains(self.driver).move_to_element(save_details).click().perform()

            sleep(2)
            print("Blacklist details are Saved")
        except Exception as e:
            print(f"Error: {e}")
            print("Save button is not functional or clickable. Details not saved.")

    def scroll_down(self):
            # Using JavaScript to scroll down the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(5)
            print("Scrolled down")


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
    member_list_page.excel_download()
    member_list_page.edit_details()
    member_list_page.view_business_certificate()
    member_list_page.Customer_Memo_Screen()
    member_list_page.close_Memo()
    member_list_page.Save_Member_details()




if __name__ == "__main__":
    pytest.main()
