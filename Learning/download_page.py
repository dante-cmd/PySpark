from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time



driver_path = r'C:\dmozilla\geckodriver.exe'
ser = Service(driver_path)
opt = webdriver.FirefoxOptions()

# selenium without opening browser 
opt.add_argument('--headless')

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(service=ser, options=opt)

# Go to the home page
def get_page(url):
    init_time = time.time()
    driver.get(url)
    print("> ",round((time.time() -  init_time)),"Seconds")
    return driver.page_source

