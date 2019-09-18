import os
from selenium import webdriver
import time
#chrome_d=os.environ['CHROME_DRIVER']
driver = webdriver.Chrome('/var/lib/jenkins/workspace/G-Audit/chromedriver') #Path to ChromeDriver installation
driver.implicitly_wait(5)
print "Trying to login into Google..."
driver.get("https://accounts.google.com")
login_field = driver.find_element_by_name("identifier")
login_field.clear()
user_name = os.environ['GMAIL_USERNAME'] #Enter your username here
login_field.send_keys(user_name)
login_field.send_keys(u'\ue007') #unicode for enter key
time.sleep(2)

password_field = driver.find_element_by_name("password")
password_field.clear()
pass_value = os.environ['GMAIL_PASSWORD'] #Enter your password here
password_field.send_keys(pass_value)
password_field.send_keys(u'\ue007') #unicode for enter key
time.sleep(2)

print "Successfully logged into Google..."
fh=open("emails.txt","r")

websites=[]
for each in fh.readlines():
    websites.append(each.strip("\n"))
print "List of emails that will be tested:"+" "+str(websites)
driver.implicitly_wait(5)

for i in websites:
    try:
        driver.get("https://calendar.google.com/calendar/embed?src="+i)
        warning=driver.find_element_by_id('warningBox').text
        print "Access Restricted: "+i
    except:
        print "Public access: "+i
driver.close()
fh.close()
