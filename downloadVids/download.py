import os
import urllib.request
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome( service=Service(ChromeDriverManager().install()), options=chrome_options)

vidsAlreadyDownloaded = os.listdir('vids')
with open('/home/davidvalorwork/projects/notas/info/other/social/sargin/kat2.md') as f:
    lines = f.readlines()
for url in lines:
    print(str(lines.index(url))+'/'+str(len(lines)))
    filename = url[url.rfind('/Video/')+15:-2]+'.mp4'
    condition = filename in vidsAlreadyDownloaded
    if(not condition):
        driver.get(url)


        elements = driver.find_elements(by=By.CSS_SELECTOR, value=".rmp-overlay-button")
        if(len(elements)!= 0):
            try:
                elements[0].click()
            except Exception as e:
                pass
        time.sleep(2)

        elements = driver.find_elements(by=By.CSS_SELECTOR, value="video[class='rmp-object-fit-contain rmp-video']")
        #for e in elements:
        attr = elements[0].get_attribute('src')
        attr = attr.replace(' ','%20')
        if(attr.rfind('.mp4') != -1):
            videoUrl = attr

        if(videoUrl):
            urllib.request.urlretrieve(videoUrl, 'vids/'+filename)
        else:
            print("ERROR DOWNLOADING")
            raise "Error"
