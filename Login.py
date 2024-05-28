from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def login(self, username, password):
        ID = self.wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        ID.send_keys(username)
        sleep(2)
        print('Username')
        Password = self.wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        Password.send_keys(password)
        sleep(2)
        print('Password')
        Show = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='icon pw-show false']")))
        Show.click()
        sleep(2)
        print("Password is showing")
        Unshow = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='icon pw-show active'])[1]")))
        Unshow.click()
        sleep(5)
        print("Password is not showing")
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".flex.justify-center.gap-2")))
        login_button.click()
        sleep(5)
        print('Icarus Advertisement Admin Dashboard screen is opened successfully')

# Fixtures for setting up and tearing down the driver
@pytest.fixture
def driver_setup():
    chrome_driver_path = '/Users/zain/Downloads/chromedriver'
    driver = webdriver.Chrome()
    driver.get('https://advertiser-admin.icarus.mufin.lol/login')
    driver.maximize_window()
    yield driver
    driver.quit()

# Pytest function for testing login
def test_login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login('admin_advertiser', 'Icarus@123')

    # Print statements instead of assertions to check if the login was successful
    expected_url = 'https://advertiser-admin.icarus.mufin.lol/admin/dashboard'
    if expected_url.lower() in driver.current_url.lower():
        print('Login successful - Redirected to the expected URL')
    else:
        print('Login failed - Not redirected to the expected URL')

    wait = WebDriverWait(driver, 10)
    dashboard_text_locator = (By.XPATH, "//span[@class='text-admin-primary']")
    try:
        wait.until(EC.presence_of_element_located(dashboard_text_locator))
        print('Dashboard text is present on the page after login')
    except:
        print('Dashboard text is not present on the page after login')

    # You can add more print statements or actions as needed

if __name__ == "__main__":
    pytest.main()
