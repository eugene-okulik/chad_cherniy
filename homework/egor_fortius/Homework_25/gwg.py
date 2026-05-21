from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
#options.headless = True
options.add_argument('start-maximized')
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

def test_site():
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    st_city_name = wait.until(EC.presence_of_element_located((By.ID, 'stateCity-label')))
    # sleep(3)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", st_city_name)

    state = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'css-13cymwt-control')))
    state.click()
    sel_state = wait.until(EC.visibility_of_element_located((By.ID, "react-select-3-option-1")))
    sel_state.click()

    city_container = driver.find_element(By.XPATH, "//div[text()='City']//parent::div")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", city_container)

    city_control = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#city input")))
    city_control.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#city-menu")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='city-menu']//div[text()='Agra']"))).click()