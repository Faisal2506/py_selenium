from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





driver = webdriver.Chrome()
driver.get("https://outriskai.com/login")
# assert "outrisk" in driver.title

# termsCheckbox = driver.find_element(By.ID, "agreeToTerms")
# termsCheckbox.click()
wait = WebDriverWait(driver, 10)

# cookiesAcceptButton = wait.until(EC.element_to_be_clickable(By.ID,''))

accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]")))
accept_button.click()

# time.sleep(3)

# Now wait for the 'Agree to Terms' button to be clickable (if needed)
terms_button = wait.until(EC.element_to_be_clickable((By.ID, 'agreeToTerms')))
terms_button.click()


userName = driver.find_element(By.ID,"email")
userName.clear()
userName.send_keys("outriskairpa@gmail.com")
# userName.send_keys(Keys.RETURN)

signInPassword = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In with Password')]")))
signInPassword.click()

# time.sleep(3)

password = driver.find_element(By.ID,"password")
password.clear()
password.send_keys("hVZB1WGTWZCsxu")
# password.send_keys(Keys.RETURN)
signInPassword = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In with Password')]")))
signInPassword.click()


time.sleep(3)

contract_button = wait.until(EC.element_to_be_clickable((By.ID, 'create-contract')))
contract_button.click()

time.sleep(2)

contractTitle = driver.find_element(By.ID,"title")
contractTitle.clear()
contractTitle.send_keys("Job offer")

promisor = driver.find_element(By.NAME,"promisor")
promisor.clear()
promisor.send_keys("Rishabh")


promisor = driver.find_element(By.NAME,"promisee")
promisor.clear()
promisor.send_keys("Faisal")

country_dropdown_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@role='combobox' and .//span[contains(text(), 'Country')]]")
    ))
country_dropdown_button.click()
# wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='India']")))
india_option = driver.find_element(By.XPATH, "//span[text()='India']")
india_option.click()

state_dropdown_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox' and .//span[contains(text(), 'State')]]")))
state_dropdown_button.click()
# wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='India']")))
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
# wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='India']")))
pending_option = driver.find_element(By.XPATH, "//span[text()='Pending']")
pending_option.click()

duration = driver.find_element(By.ID,"contractDuration")
duration.clear()
duration.send_keys("6")

contractType = driver.find_element(By.ID,"contractType")
contractType.clear()
contractType.send_keys("Legal")

# calendar_button = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, "//button[@aria-haspopup='dialog' and .//svg[@class='lucide lucide-calendar']]"))
#     )
# calendar_button.click()

#     # Step 8: Wait for the calendar popup to load (adjust if necessary)
# wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-expanded='true']")))

#     # Step 9: Select the desired date (December 3rd, 2024)
# print("Selecting 'December 3rd, 2024'...")
# date_to_select = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//button[@aria-label='Go to December 3, 2024']"))
#     )
# date_to_select.click()





# calendar_button = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//button[@aria-haspopup='dialog' and .//svg[@class='lucide lucide-calendar']]"))
# )
# calendar_button.click()

#     # Step 8: Wait for the calendar popup to open and confirm it's expanded
# print("Waiting for the calendar popup to open...")
# wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-expanded='true']")))

#     # Step 9: Select the desired date (December 3rd, 2024)
#     # We can first navigate to the correct month (December 2024), if necessary.
#     # Check if the month is already December 2024, or we need to click the month navigation buttons

#     # Open the month selector and navigate to December 2024
# print("Navigating to December 2024...")
# month_selector = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//button[@aria-label='Select month']"))
# )
# month_selector.click()

#     # Select December from the month selector (adjust if necessary based on the calendar's structure)
# december_button = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//span[text()='December']"))
# )
# december_button.click()

#     # Select the year (2024)
# year_selector = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//button[@aria-label='Select year']"))
# )
# year_selector.click()

# year_2024 = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//span[text()='2024']"))
# )
# year_2024.click()

#     # Now, select December 3rd, 2024
# print("Selecting December 3rd, 2024...")
# date_to_select = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//button[@aria-label='Go to December 3, 2024']"))
# )
# date_to_select.click()


contractDescription = driver.find_element(By.ID,"contractDescription")
contractDescription.clear()
contractDescription.send_keys("If I let Rishabh kill me everytime in valorant on sunday, then he will give me job")

time.sleep(5)
driver.close()
