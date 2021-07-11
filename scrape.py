import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.commom.keys import Keys
import os

browser=webdriver.Chrome("chromedriver.exe")# creating a driver object
browser.get("https://www.linkedin.com")

username=browser.find_element_by_id("session_key")
username.send_keys("chamano.sr@gmail.com")
password=browser.find_element_by_id("session_password")
password.send_keys('LINKEDIN_PS')

login_button=browser.find_element_by_class_name("sign-in-form__submit-button")
login_button.click()

browser.get("https://linkedin.com/jobs")

job=browser.find_elements_by_class_name("job-card-square__title")
c=[]
for i in job:
    #print(i.text)
    c.append(i.text) 

print(c)
print()
print(len(c))

job_title=[]
for i in range(len(c)):
    job_title.append(c[i].strip("Job Title\n"))
    job_title

print(job_title)

job2=browser.find_elements_by_class_name("job-card-container__company-name")
comp_name=[]
for i in job2:
    #print(i.text)
    comp_name.append(i.text)

print(comp_name)
print()
print(len(comp_name))

job3=browser.find_elements_by_class_name("job-card-container__metadata-items")
loc_name=[]
for i in job3:
    #print(i.text)
    loc_name.append(i.text)

print(loc_name)
print()
print(len(loc_name))

comp_name.append(" ")
comp_name.append(" ")

len(comp_name)

col=["Company Name", "Job Title", "Location"]
df=pd.DataFrame({"Company Name":comp_name[slice(20)], "Job title": slice(job_title), "Location":loc_name})

df.head()

df.to_csv("linkedin_scrapejobs.csv")