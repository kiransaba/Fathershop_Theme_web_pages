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

class AvdertisingListPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_advertisement_list_Inquiry(self):
        try:
            open_advertisement = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="광고관리-tab"]')))
            open_advertisement.click()
            sleep(2)
            print("Advertising Management Drop-down Menu is showing")
        except TimeoutException:
            print("Timed out waiting for advertisement list inquiry element to be present.")

    def select_advertisement_list(self):
        try:
            select_advertisement = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="광고관리-tab"]')))
            select_advertisement.click()
            sleep(2)
            print("Advertisement list inquiry is selected")
        except TimeoutException:
            print("Timed out waiting for select advertisement list element to be present.")

    def open_advertisement_detail(self):
        try:
            open_advertisement_detail = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Tes'])[1]")))
            open_advertisement_detail.click()
            sleep(2)
            print("Advertisement details screen is opened")
        except TimeoutException:
            print("Timed out waiting for open advertisement detail element to be present.")

    def scroll_down(self):
        try:
            # Using JavaScript to scroll down the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(5)
            print("Scrolled down")
        except Exception as e:
            print(f"An error occurred while scrolling down: {str(e)}")

    def excel_download(self):
        try:
            download_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span)[13]")))
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
            print("Timed out waiting for download button element to be present.")
        except Exception as e:
            print(f"An error occurred during excel download: {str(e)}")

    def save_drafts(self):
        try:
            drafts = self.wait.until(EC.presence_of_element_located((By.XPATH,"(//span)[12]")))
            drafts.click()
            sleep(2)
            print("draft open")

            close_drafts = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@fill-rule='evenodd'])[5]")))
            close_drafts.click()
            sleep(2)
            print("drafts closed")
        except TimeoutException:
            print("Timed out waiting for save drafts elements to be present.")
        except Exception as e:
            print(f"An error occurred during save drafts: {str(e)}")

    def edit_details(self):
        try:
                name = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[contains(@type,'text')])[1]")))
                name.send_keys("Fixed Promotion")
                sleep(2)
                print("name is edited")

                contact = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[contains(@class,'styles_input-body__5o5_t focus:border-0 w-[167px]')])[1]")))
                contact.send_keys("0331234567")
                sleep(2)
                print("Company number is edited")

                vehicle_no = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='3']")))
                vehicle_no.send_keys("4")
                sleep(2)
                print("Vehicle number is edited")

                change_status = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span)[34]")))
                change_status.click()
                sleep(2)
                print("change_status is edited")
                #self.scroll_down()

                sel_status = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span[contains(@class,'text-sm font-medium')])[5]")))
                sel_status.click()
                sleep(5)
                print("status is selected")

                save_status = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'flex justify-center gap-2')])[5]")))
                save_status.click()
                sleep(4)
                print("change_status is saved")


###########Adv_typpe element id not visble to selenium
                #adv_type = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[title='고정형']")))
                #adv_type.click()
                #sleep("3")
                #print("advertisement type is selected")

                #select_adv= self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='전국형']//div[@class='ant-select-item-option-content']")))
                #select_adv.click()
                #sleep(2)
                #print("adv type is saved")

                adv_area = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[contains(@type,'checkbox')])[5]")))
                adv_area.click()
                sleep(2)
                print("advertisement area is clicked")

                self.scroll_down()

                adv_content = self.wait.until(EC.presence_of_element_located((By.XPATH,"(//textarea[contains(@class,'pl-3 overflow-y-auto h-[170px] rounded border border-admin-stroke w-full styles_pre-wrap__r3a8D')])[1]")))
                adv_content.send_keys("Hello testing")
                sleep(2)
                print("change_status is saved")

                edit = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span)[107]")))
                edit.click()
                sleep(2)
                print("edit")

                Save_changes = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'flex justify-center gap-2')])[3]")))
                Save_changes.click()
                sleep(2)
                print("Saved")


        except TimeoutException:

            print("Timed out waiting for edit details elements to be present.")

        except Exception as e:

            print(f"An error occurred during edit details: {str(e)}")

@pytest.fixture
def driver_setup():
    chrome_driver_path = '/Users/zain/Downloads/chromedriver'
    driver = webdriver.Chrome()
    driver.get('https://advertiser-admin.icarus.mufin.lol/login')
    driver.maximize_window()
    yield driver
    driver.quit()

# Pytest function for testing login and member list page
def test_login_and_advertisinglist(driver_setup):
    driver = driver_setup

    login_page = LoginPage(driver)
    login_page.login('admin_advertiser', 'Icarus@123')

    adv_list_page = AvdertisingListPage(driver)
    adv_list_page.open_advertisement_list_Inquiry()
    adv_list_page.select_advertisement_list()
    adv_list_page.open_advertisement_detail()
    #adv_list_page.excel_download()
    #adv_list_page.save_drafts()
    adv_list_page.edit_details()


if __name__ == "__main__":
    pytest.main()
