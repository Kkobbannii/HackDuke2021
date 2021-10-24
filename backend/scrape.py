import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time 
import os
from os import listdir
from PIL import Image


# try:
#     img = Image.open("photos/filename1.png")
#     print('available')
# except: 
#     print("unavailable")



for filename in listdir("photos"):
    if filename.endswith('.png'):
        try:
            img = Image.open("photos/"+filename)
        except:
            os.remove("photos/"+filename)

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")

print(os.getcwd()+"/chromedriver.exe")
  

# //*[@id="siteTable"]
subreddits = ["justneckbeardthings","gocommitdie","noahgettheboat","niceguys","animemes","edp445","floppa"]
links =[]
for s in subreddits:
    driver = webdriver.Chrome(executable_path=os.getcwd()+"/chromedriver",options=chrome_options)  
    url = "https://www.reddit.com/r/"+s+"/top/?t=all"
    driver.get(url) 

# html = driver.page_source 
    
    elems = driver.find_elements_by_xpath("//a[contains(@href,'/r/"+s+"/comments/')]")
# print(elems)
    for elem in elems:
        # if ("https://www.reddit.com/r/justneckbeardthings/comments" in (elem.get_attribute("href"))):
        # print(elem.get_attribute("href"))
        links.append(elem.get_attribute("href"))
   

    driver.close()
    driver.quit()

res = []
for i in links:
    if i not in res:
        res.append(i)
for z in res:
    print(z)

l = 0
for url in res:
    l += 1
    
    driver = webdriver.Chrome(executable_path=os.getcwd()+"/chromedriver",options=chrome_options)   
# l=0
# url = "https://www.reddit.com/r/Animemes/comments/qe9w12/here/"
    driver.get(url)
    with open('photos/filename'+str(l)+'.png', 'wb') as file:
        try:
            file.write(driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div[4]/div/a/img").screenshot_as_png)
            try:
                img = Image.open("photos/"+'photos/filename'+str(l)+'.png')
            except:
                os.remove("photos/"+'photos/filename'+str(l)+'.png')
        except:
            continue
        else:
            continue
        
    driver.close()
    driver.quit()

print(len(res))