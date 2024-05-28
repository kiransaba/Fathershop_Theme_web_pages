from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest


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
        self.wait = WebDriverWait(self.driver, 10)

    def open_member_list_inquiry(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'회원관리')]"))).click()
        sleep(2)
        print("Membership Management Drop-down Menu is showing")
    def open_member_details(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//a[normalize-space()='linen@mufin.co.kr'])[1]"))).click()
        sleep(2)
        print("Member details screen is opened")
class BlackListRegistration:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)


    def open_blacklist_registration(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_member-detail-header__msMMj']//button[1]"))).click()
        sleep(2)
        print("Blacklist Registration popup screen is opened")
    def checkbox_selected(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='기타(직접입력)(0/100)']"))).click()
        sleep(2)
        print("Checkbox is clicked")
    def blacklist_reason(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='사유입력']"))).send_keys("Testing")
        sleep(5)
        print("Reason for Blacklist is entered")
    def save_blacklist_info(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/button[2]/div[1]"))).click()
        sleep(10)
        print("Blacklist Registration is saved")
    def reopen_blacklist_registration(self):
        #self.wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='ant-modal-wrap']")))
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//button)[2]"))).click()
        sleep(5)
        print("General Registration popup screen is opened")
    def close_general_regstration(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='flex justify-center gap-2'])[7]"))).click()

        sleep(2)
        print("General Registration screen is closed")

@pytest.fixture
def driver_setup():
    chrome_driver_path = '/Users/zain/Downloads/chromedriver'
    driver = webdriver.Chrome()
    driver.get('https://advertiser-admin.icarus.mufin.lol/login')
    driver.maximize_window()
    yield driver
    driver.quit()

def main():
    chrome_driver_path = '/Users/zain/Downloads/chromedriver'
    driver = webdriver.Chrome()
    driver.get('https://advertiser-admin.icarus.mufin.lol/login')
    driver.maximize_window()

def test_login_and_member_list(driver_setup):
    driver = driver_setup

    login_page = LoginPage(driver)
    login_page.login('admin_advertiser', 'Icarus@123')

    member_list_page = MemberListPage(driver)
    member_list_page.open_member_list_inquiry()
    member_list_page.open_member_details()

    blacklistregitration = BlackListRegistration(driver)
    blacklistregitration.open_blacklist_registration()
    blacklistregitration.checkbox_selected()
    blacklistregitration.blacklist_reason()
    blacklistregitration.save_blacklist_info()
    #blacklistregitration.reopen_blacklist_registration()
    #blacklistregitration.close_general_regstration()


    driver.quit()

if __name__ == "__main__":
    pytest.main()