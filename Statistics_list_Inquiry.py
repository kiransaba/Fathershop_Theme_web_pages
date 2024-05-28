import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, time

import os
from time import sleep, time
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
        sleep(10)
        print('Icarus Advertisement Admin Dashboard screen is opened successfully')

class StatisticsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def Open_Statistics_list_inquiry(self):
        # Define locators for Statistics dropdown and Statistics list
        statistics_dropdown_locator = (By.CSS_SELECTOR, '[data-testid="통계관리-tab"]')
        statistics_list_locator = (By.CSS_SELECTOR, '[data-testid="통계관리-tab-통계목록조회-subtab"]')

        try:
            # Click on Statistics dropdown
            statistics_dropdown = self.wait.until(EC.presence_of_element_located(statistics_dropdown_locator))
            statistics_dropdown.click()
            sleep(5)
            print("Statistics Management Drop-down Menu is showing")

            # Click on Statistics list
            statistics_list = self.wait.until(EC.element_to_be_clickable(statistics_list_locator))
            statistics_list.click()
            sleep(5)
            print("Statisticslist_Inquiry is selected")
        except Exception as e:
            print(f"Error: {e}")
            print("Error clicking on Statistics dropdown or Statistics list")

    def open_member_details(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//a[contains(text(),'usmanakram13@gmail.com')])[1]"))).click()
        sleep(2)
        print("Member details screen is opened")

    def excel_download(self):
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

    def edit_details(self):

        Company_number = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='company_phone_number'])[1]")))
        Company_number.click()
        sleep(2)
        print("Contact number is edited")

        Manager = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#manager")))
        Manager.send_keys("Hong@gmail.com")
        sleep(2)
        print("Manager email is edited")

        #position= self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='ant-select-item-option-content'])[8]")))
        #position.click()
        #sleep(2)
        #print("Contact Person Position dropdown is opened")
   ##Element_Ids not accessible by selenium
        #sel_position = self.wait.until(EC.presence_of_element_located((By.XPATH,"")))
        #sel_position.click()
        #sleep(2)
        #print("Contact Person Position  is selected")


  #you can remove comment when the phone number is not added
        #Mobile_no = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#contact_person_mobile_number")))
        #Mobile_no.send_keys("03316292999")
        #sleep(2)
        #print("Mobile number is edited")


    def view_business_certificate(self):
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

    def Customer_Memo_Screen(self):

        Customer_Memo = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='메모를 입력해주세요.']")))
        Customer_Memo.send_keys("Memo Testing Purpose")
        sleep(2)
        print("Customer Memo is edited ")

        self.scroll_down()


        Check_Memo_History= self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='flex justify-center gap-2'])[2]")))
        Check_Memo_History.click()
        sleep(5)
        print("Customer Memo History Screen is opened ")



    def close_Memo(self):
        close_memo_locator = (By.XPATH, "(//*[name()='svg'][@fill-rule='evenodd'])[1]")

        try:
            close_memo = self.wait.until(EC.presence_of_element_located(close_memo_locator))

            # Scroll into view using actions
            actions = ActionChains(self.driver)
            actions.move_to_element(close_memo).perform()

            # Click the button
            close_memo.click()

            sleep(5)
            print("Customer Memo History Screen is closed successfully")
        except Exception as e:
            print(f"Error: {e}")
            print("Close Memo button is not functional or clickable. Memo history screen not closed.")

    def Save_Member_details(self):
        save_details_locator = (By.XPATH, "(//div[@class='flex justify-center gap-2'])[3]")

        try:
            save_details = self.wait.until(EC.element_to_be_clickable(save_details_locator))
            save_details.click()
            sleep(5)
            print("Statistics Member details are Saved")
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
def test_login_and_statistcs_page(driver_setup):
    driver = driver_setup

    login_page = LoginPage(driver)
    login_page.login('admin_advertiser', 'Icarus@123')

    statisticspage = StatisticsPage(driver)
    statisticspage.Open_Statistics_list_inquiry()
    statisticspage.open_member_details()
    statisticspage.excel_download()
    statisticspage.edit_details()
    statisticspage.view_business_certificate()
    #statisticspage.Customer_Memo_Screen()
    #statisticspage.close_Memo() element Ids have some ssue first resolve that then remove both commmented
    statisticspage.Save_Member_details()




if __name__ == "__main__":
    pytest.main()
