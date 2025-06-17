import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

class TestOrangeHRMLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        s = Service(executable_path="D:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        yield
        self.driver.quit()

    def test_login_valid_user(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        sleep(5)  # Chờ trang dashboard load
        assert "dashboard" in self.driver.current_url.lower()
        print("Login successful!")

        self.driver.back()
        sleep(2)  # Quay lại trang login

        self.driver.forward()
        sleep(2)  # Quay lại trang dashboard