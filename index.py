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



 

# <a id="ember316" class="ember-view mn-community-summary__link link-without-hover-state" aria-label="See 3,417 connections" href="/mynetwork/invite-connect/connections/">
#           <div class="mn-community-summary__info-container t-black t-16 t-normal">
#             <div class="mn-community-summary__entity-info">
#               <li-icon aria-hidden="true" type="people" class="mr4" size="medium"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
#   <path d="M12 16v6H3v-6a3 3 0 013-3h3a3 3 0 013 3zm5.5-3A3.5 3.5 0 1014 9.5a3.5 3.5 0 003.5 3.5zm1 2h-2a2.5 2.5 0 00-2.5 2.5V22h7v-4.5a2.5 2.5 0 00-2.5-2.5zM7.5 2A4.5 4.5 0 1012 6.5 4.49 4.49 0 007.5 2z"></path>
# </svg></li-icon>
#               Connections
#             </div>

#             <div class="pl3">
#                 3,417
#             </div>
#           </div>
#         </a>