from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


options = Options()
# options.headless = True
options.add_argument('start-maximized')
# options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)


def test_site():
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)

    driver.execute_script("window.scrollBy(0, 300);")
    first_name = wait.until(EC.presence_of_element_located((By.ID, 'firstName')))
    first_name.send_keys("Georgoian")
    last_name = wait.until(EC.presence_of_element_located((By.ID, 'lastName')))
    last_name.send_keys("Petrogian")
    user_email = wait.until(EC.presence_of_element_located((By.ID, 'userEmail')))
    user_email.send_keys("test@user.ru")
    gender_male = wait.until(EC.presence_of_element_located((By.ID, 'gender-radio-1')))
    gender_male.click()
    user_number = wait.until(EC.presence_of_element_located((By.ID, 'userNumber')))
    user_number.send_keys("8985566445")
    date_of_birht = wait.until(EC.presence_of_element_located((By.ID, 'dateOfBirthInput')))
    date_of_birht.click()
    month = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/select')))
    month.click()
    select_month = wait.until(EC.presence_of_element_located(
        (By.XPATH,
         '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/select/option[1]')
    ))
    select_month.click()
    year = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR,
         '.react-datepicker__year-dropdown-container.react-datepicker__year-dropdown-container--select > select')
    ))
    year.click()
    select_year = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/select/option[99]')
    ))
    select_year.click()
    day = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[4]')))
    day.click()
    subject = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="subjectsInput"]')))
    subject.click()
    subject.send_keys("c")
    sel_subject = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-select-2-option-0"]')))
    sel_subject.click()

    driver.find_element(By.ID, "hobbies-checkbox-1").click()
    cur_adress = wait.until(EC.presence_of_element_located((By.ID, 'currentAddress')))
    cur_adress.send_keys("MilkeyWay, Sun system")

    state = driver.find_element(By.ID, 'react-select-3-input')
    state.click()
    sel_state = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-option-0")))
    sel_state.click()

    driver.find_element(By.ID, "city").click()
    sel_city = wait.until(EC.visibility_of_element_located((By.ID, "react-select-4-option-0")))
    sel_city.click()

    wait.until(EC.presence_of_element_located((By.ID, "submit"))).click()

    print(wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".table.table-dark.table-striped.table-bordered.table-hover"))).text)


if __name__ == "__main__":
    test_site()
