from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fake_useragent import UserAgent
import accountInfoGenerator as account
import getVerifCode as verifiCode
from selenium import webdriver
import fakeMail as email
import sys , os , random , requests , time , pyperclip
import argparse
from webdriver_manager.chrome import ChromeDriverManager as CM

#color
class color:
   PURPLE = '\033[95m'
   GREEN = '\033[92m'
   BOLD = '\033[1m'
   CWHITE  = '\33[37m'

#args = parser.parse_args()
ua = UserAgent()
userAgent = ua.random
print(userAgent)


#replace 'your path here' with your chrome binary absolute path
driver = webdriver.Chrome(executable_path=CM().install())

#saves the login & pass into accounts.txt file.
acc = open("accounts.txt", "a")

driver.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(8)
try:
    cookie = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/button[1]'))).click()
except:
	pass

# Create temporary email
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://mail.tm")
time.sleep(6)
copy_button = driver.find_element(By.XPATH, """//*[@id="DontUseWEBuseAPI"]""")
copy_button.click()
generated_email = pyperclip.paste()

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
#Fill the email value
email_field = driver.find_element_by_name('emailOrPhone')
email_field.send_keys(generated_email)
print(generated_email)
time.sleep(2.8)

# Fill the fullname value
fullname_field = driver.find_element_by_name('fullName')
fullname_field.send_keys(account.generatingName())
print(account.generatingName())
time.sleep(2.57)

# Fill username value
name = "ndiniuya151"
username_field = driver.find_element_by_name('username')
username_field.send_keys(name)
print(name)
time.sleep(3.98)

# Fill password value
password_field = driver.find_element_by_name('password')
acc_password = account.generatePassword()
password_field.send_keys(acc_password) # You can determine another password here.
password_field.send_keys(Keys.ENTER)
print(name+":"+acc_password, file=acc)
time.sleep(4.4526)

acc.close()

#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()

time.sleep(8)

birth_month = Select(driver.find_element_by_class_name("_aau-"))
# select by value 
birth_month.select_by_value('5')
time.sleep(2.8)

birth_day = Select(driver.find_element(By.XPATH, """//*[@title="Day:"]"""))
# select by value 
birth_day.select_by_value('5')
time.sleep(3.4)

birth_year = Select(driver.find_element(By.XPATH, """//*[@title="Year:"]"""))
# select by value 
birth_year.select_by_value('1991')
time.sleep(5.1489)

birthday_next_button = driver.find_element_by_class_name("_acan _acap _acaq _acas")
birthday_next_button.click()

#get opt
driver.switch_to.window(driver.window_handles[1])
print()
print(color.GREEN + "[!] " + color.CWHITE + "Waiting for otp ")

print(color.GREEN + "[!] " + color.CWHITE + "Opening mail box in 15 seconds")

for remaining in range(15, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\rComplete!            \n")
driver.refresh()
time.sleep(2)

read_otp = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/main/div/div[2]/ul/li/a/div/div[1]/div[2]/div[2]/div/div[1]').text

# Read otp from mail

# Save response to response.Text

with open("response.text","w") as file:
   file.write(str(read_otp))

read_otp_file = open("response.text")

lines = read_otp_file.readlines()

for line in lines:
   my_otp = str(line[0:6])

print(color.GREEN + "[!] " + color.CWHITE + "OTP Recieved : " + my_otp)

instCode =  my_otp
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)

driver.find_element_by_name('email_confirmation_code').send_keys(instCode, Keys.ENTER)
time.sleep(10)

#accepting the notifications.
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
time.sleep(2)

#logout
driver.find_element_by_xpath(
    "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click()
driver.find_element_by_xpath(
    "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div").click()

try:
    not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
    if(not_valid.text == 'That code isn\'t valid. You can request a new one.'):
      time.sleep(1)
      driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
      time.sleep(10)
      instCodeNew = verifiCode.getInstVeriCodeDouble(mailName, domain, driver, instCode)
      confInput = driver.find_element_by_name('email_confirmation_code')
      confInput.send_keys(Keys.CONTROL + "a")
      confInput.send_keys(Keys.DELETE)
      confInput.send_keys(instCodeNew, Keys.ENTER)
except:
      pass

time.sleep(5)
driver.quit()
