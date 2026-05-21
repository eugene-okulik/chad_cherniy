from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)

def test_site():
    driver.get("https://www.qa-practice.com/elements/input/simple")
    driver.maximize_window()
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)

    vvod_text = wait.until(EC.presence_of_element_located((By.NAME, "text_string")))
    vvod_text.send_keys("reegte46")
    vvod_text.submit()

    get_text = driver.find_element(By.ID, 'result-text')
    print(f"\n{get_text.text}")
