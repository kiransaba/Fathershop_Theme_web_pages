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

    def open_payment_list(self):
        sel_adv = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="출금내역관리-tab-지급목록조회-subtab"]')))
        sel_adv.click()
        sleep(2)
        print("payment list inqury screen is opened")

    def open_payment_info(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'보기')])[1]"))).click()
        sleep(3)
        print("Payment Information screen is opened")

    def excel_download(self):
        download_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span)[12]")))
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


    def scroll_down(self):
        # Using JavaScript to scroll down the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        print("Scrolled down")



    def payment_status(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='flex justify-center gap-2'])[1]"))).click()
        sleep(3)
        print("Change Payment Status dropdown is opened")

        sel_status=self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='completed'])[1]")))
        sel_status.click()
        sleep(3)
        print("Paymebt status changes to approved")

        save_status = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='flex justify-center gap-2'])[5]")))
        save_status.click()
        sleep(3)
        print("Paymebt status is saved")

    def click_import(self):
        try:
            import_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'가져오기')])[1]")))
            import_button.click()
            sleep(3)
            print("Payment Information screen is opened")
        except Exception as e:
            print(f"Error: {e}")
            print("Failed to click the '가져오기' button. Button may not be functional.")

    def Customer_Memo_Screen(self):

        Customer_Memo = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='특이사항 없이 지급 완료']:first-child")))

        Customer_Memo.send_keys("Memo Testing Purpose")
        sleep(2)
        print("Customer Memo is edited ")

        self.scroll_down()
        Check_Memo_History = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='flex justify-center gap-2'])[2]")))
        Check_Memo_History.click()
        sleep(2)
        print("Customer Memo History Screen is opened ")

        close_memo = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@fill-rule='evenodd'])[3]")))
        close_memo.click()
        sleep(3)
        print("Customer Memo History Screen is closed successfully")

    def save_payment_information(self):
        save_details_locator = (By.XPATH, "(//button[@class='style_button__e50TK styles_save-button__BOfyF'])[1]")

        try:
            save_details = self.wait.until(EC.element_to_be_clickable(save_details_locator))

            # Move to the element before clicking
            ActionChains(self.driver).move_to_element(save_details).click().perform()

            sleep(5)
            print("Payment information details are Saved")
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
    history.open_payment_list()
    history.open_payment_info()
    history.excel_download()
    history.payment_status()
    history.click_import()
    history.Customer_Memo_Screen()
    history.save_payment_information()

if __name__ == "__main__":
    pytest.main()
