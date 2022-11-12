from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pwinput

username = input('''
Enter your linkedin username or mobile number 
''')

password = password = pwinput.pwinput(prompt='Enter your Linkedin Password: ', mask='*')
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2F")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/main/p[1]/a').click()
username_element = driver.find_element(By.XPATH,'//*[@id="username"]')
username_element.clear()
username_element.send_keys(username)
password_element = driver.find_element(By.XPATH,'//*[@id="password"]')
password_element.clear()
password_element.send_keys(password)
driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="global-nav"]/div/nav/ul/li[2]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//a[contains(@href,"/mynetwork/invite-connect/connections/")]').click()
time.sleep(2)
element = driver.find_element(By.CSS_SELECTOR,'mn-connection-card__name')
time.sleep(2)
time.sleep(200)



 

