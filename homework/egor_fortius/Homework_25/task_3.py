from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


options = Options()
# options.headless = True
options.add_argument('start-maximized')
# options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)


def test_site_1():
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    driver.maximize_window()
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)

    select = Select(driver.find_element(By.NAME, "choose_language"))
    select.select_by_value("1")
    sleep(0.5)
    sel_text = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'form-select'))).text
    sleep(0.5)
    submit = wait.until(EC.presence_of_element_located((By.ID, "submit-id-submit")))
    submit.click()
    sleep(0.5)
    res_text = wait.until(EC.visibility_of_element_located((By.ID, "result-text"))).text

    return res_text == sel_text


def test_site_2():
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.maximize_window()
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)

    start = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#start > button")))
    start.click()
    check_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]/h4')))

    return check_text.text == "Hello World!"
