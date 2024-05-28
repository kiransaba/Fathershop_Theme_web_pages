from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

class MemberDetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_member_list_inquiry(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'회원관리')]"))).click()
        sleep(2)
        print("Membership Management Drop-down Menu is showing")
    def open_member_details(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//a[normalize-space()='linen1@mufin.co.kr'])[1]"))).click()
        sleep(2)
        print("Member details screen is opened")
    def open_blacklist_registration(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_member-detail-header__msMMj']//button[1]"))).click()
        sleep(2)
        print("Blacklist Registration popup screen is opened")

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='광고의사 없는 반복 신청']"))).click()
        sleep(2)
        print("Checkbox is clicked")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='style_button__e50TK styles_model-table-cancel-btn__3vJWU']//div[@class='flex justify-center gap-2']"))).click()
        sleep(2)
        print("Blacklist Registration is cancelled")

def main():
    chrome_driver_path = '/Users/zain/Downloads/chromedriver'
    driver = webdriver.Chrome()
    driver.get('https://advertiser-admin.icarus.mufin.lol/login')
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login('admin_advertiser', 'Icarus@123')

    member_list_page = MemberDetailPage(driver)
    member_list_page.open_member_list_inquiry()
    member_list_page.open_member_details()
    member_list_page.open_blacklist_registration()

    driver.quit()

if __name__ == "__main__":
    main()
