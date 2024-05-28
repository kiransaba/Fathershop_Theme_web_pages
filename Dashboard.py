import pytest
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

class Dashboard:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def expand_menu(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='cursor-pointer transform transition duration-300 ease-in-out rotate-0'])[1]"))).click()
        sleep(2)
        print("Menu expand")

        self.scroll_down()

    def scroll_down(self):
        # Using JavaScript to scroll down the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        print("Scrolled down the page")

    def open_inquiry_management(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'1:1문의관리')])[1]"))).click()
        sleep(3)
        print("1:1 inquiry Management screen is opened")
        self.scroll_down()

    def open_notice_management(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'공지사항관리')]"))).click()
        sleep(5)
        print("Notice Management screen is opened")
        self.scroll_down()

    def click_view_all(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='pb-[8px] text-admin-button-1'])[1]"))).click()
        sleep(5)
        print("View all screen is opened")

class TestIcarusAdmin:

    @pytest.fixture
    def setup(self):
        chrome_driver_path = '/Users/zain/Downloads/chromedriver'
        driver = webdriver.Chrome()
        driver.get('https://advertiser-admin.icarus.mufin.lol/login')
        driver.maximize_window()

        yield driver

        driver.quit()

    def test_login(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.login('admin_advertiser', 'Icarus@123')

    def test_dashboard_functions(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.login('admin_advertiser', 'Icarus@123')

        dashboard = Dashboard(driver)
        dashboard.expand_menu()
        dashboard.open_inquiry_management()
        dashboard.open_notice_management()
        dashboard.click_view_all()

if __name__ == "__main__":
    pytest.main()
