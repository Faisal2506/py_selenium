from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import config


URL = config.URL
driver = webdriver.Chrome()
driver.get(URL)

wait = WebDriverWait(driver, 10)

accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]")))
accept_button.click()

# time.sleep(3)

terms_button = wait.until(EC.element_to_be_clickable((By.ID, 'agreeToTerms')))
terms_button.click()

USERNAME = config.USERNAME
userName = driver.find_element(By.ID,"email")
userName.clear()
userName.send_keys(USERNAME)


signInPassword = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In with Password')]")))
signInPassword.click()


PASSWORD = config.PASSWORD
password = driver.find_element(By.ID,"password")
password.clear()
password.send_keys(PASSWORD)
signInPassword = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In with Password')]")))
signInPassword.click()


time.sleep(3)

contract_button = wait.until(EC.element_to_be_clickable((By.ID, 'create-contract')))
contract_button.click()

time.sleep(2)

TITLE = config.TITLE
contractTitle = driver.find_element(By.ID,"title")
contractTitle.clear()
contractTitle.send_keys(TITLE)

PROMISOR = config.PROMISOR
promisor = driver.find_element(By.NAME,"promisor")
promisor.clear()
promisor.send_keys(PROMISOR)

PROMISEE = config.PROMISEE
promisee = driver.find_element(By.NAME,"promisee")
promisee.clear()
promisee.send_keys(PROMISEE)

country_dropdown_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@role='combobox' and .//span[contains(text(), 'Country')]]")
    ))
country_dropdown_button.click()

india_option = driver.find_element(By.XPATH, "//span[text()='India']")
india_option.click()

state_dropdown_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox' and .//span[contains(text(), 'State')]]")))
state_dropdown_button.click()

bihar_option = driver.find_element(By.XPATH, "//span[text()='Bihar']")
bihar_option.click()

city = driver.find_element(By.ID,"city")
city.clear()
city.send_keys("Mumbai")

contractValue = driver.find_element(By.ID,"contractValue")
contractValue.clear()
contractValue.send_keys("1000")

status_dropdown_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@role='combobox' and .//span[contains(text(), 'status')]]")
    ))
status_dropdown_button.click()

pending_option = driver.find_element(By.XPATH, "//span[text()='Pending']")
pending_option.click()

duration = driver.find_element(By.ID,"contractDuration")
duration.clear()
duration.send_keys("6")

contractType = driver.find_element(By.ID,"contractType")
contractType.clear()
contractType.send_keys("Legal")

contractDescription = driver.find_element(By.ID,"contractDescription")
contractDescription.clear()
contractDescription.send_keys("If I let Rishabh kill me everytime in valorant on sunday, then he will give me job")


date_value = config.CONTRACT_DATE  # Example: "2024-12-01"
parsed_date = datetime.strptime(date_value, "%Y-%m-%d")
desired_year = parsed_date.year
desired_month = parsed_date.strftime("%B") 
desired_day = parsed_date.day

date_picker_elements = driver.find_element(By.CSS_SELECTOR, "svg.lucide-calendar")
date_picker_elements.click()
    
time.sleep(1)

day_button = WebDriverWait(driver, 1).until(
    EC.presence_of_element_located((By.XPATH, f"//div[@id='radix-:re:']//table//button[text()='{desired_day}']"))
)
day_button.click()

generateButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Generate')]")))
generateButton.click()

time.sleep(10)

unlockButton = driver.find_element(By.CLASS_NAME, "lucide-unlock-keyhole")
unlockButton.click()

time.sleep(3)

editable_element = driver.find_element(By.CLASS_NAME, 'bn-block-outer')
editable_element.send_keys("Hello World")

time.sleep(5)

downloadButton = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Download')]")))
downloadButton.click()

shareButton = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Share')]")))
shareButton.click()

time.sleep(3)

urlShare = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Share') and following-sibling::button[contains(text(), 'Close')]]")))
urlShare.click()

time.sleep(3)

copy = driver.find_element(By.CLASS_NAME, "lucide-copy")
copy.click()

url = pyperclip.paste()
print(url)

time.sleep(5)

driver.close()