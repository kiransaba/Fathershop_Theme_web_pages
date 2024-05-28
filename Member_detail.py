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

    def excel_download(self):
        self.scroll_down()
        self.wait.until( EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[1]/div[2]/main[1]/div[1]/table[1]/tr[16]/td[2]/button[1]/div[1]"))).click()
        sleep(2)
        print("yes")

    def excel_download(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ""))).click()
        sleep(2)
        print("")

    def select_person_position(self):
        self.wait.until(EC.presence_of_element_located(By.XPATH, "")).click()
        sleep(2)
        print("Contact Person Dropdown is opened")
        self.wait.until(EC.presence_of_element_located(By.XPATH, "")).click()
        sleep(2)
        print("Option from Dropdown is selected")
    def view_business_certificate(self):
        self.wait.until(EC.presence_of_element_located(By.XPATH, "")).click()
        sleep(2)
        print("Contact Person Dropdown is opened")

    def scroll_down(self):
        # Using JavaScript to scroll down the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        print("Scrolled down the page")





def main():
    chrome_driver_path = '/Users/zain/Downloads/chromedriver'
    driver = webdriver.Chrome()
    driver.get('https://advertiser-admin.icarus.mufin.lol/login')
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login('admin_advertiser', 'Icarus@123')

    member_list_page = MemberListPage(driver)
    member_list_page.open_member_list_inquiry()
    member_list_page.open_member_details()
    member_list_page.excel_download()




    driver.quit()

if __name__ == "__main__":
    main()
