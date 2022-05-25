import urllib.request
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print("1. Starting selenium")
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome( service=Service(ChromeDriverManager().install()), options=chrome_options)

with open('/home/davidvalorwork/projects/notas/info/other/social/sargin/kat2.md') as f:
    lines = f.readlines()
    print("Cantidad de videos",len(lines))

for url in lines:
    print("2. Setting URL's and filename")
    filename = url[url.rfind('/Video/')+15:-2]+'.mp4'
    print(url, filename)

    print("3. Driver getting url")
    driver.get(url)

    print("4. Pressing the play button")

    elements = driver.find_elements(by=By.CSS_SELECTOR, value=".rmp-overlay-button")
    print("Cantidad de elementos con la clase .rmp-overlay-button", len(elements))
    if(len(elements)!= 0):
        try:
            elements[0].click()
        except Exception as e:
            print("Elemento no iteraccionable")
            pass
    time.sleep(2)

    print("5. Finding video url for download")
    elements = driver.find_elements(by=By.CSS_SELECTOR, value="div#rmpPlayer")
    print("Elements with selector .rmp-object-fit-contain rmp-video",len(elements))
    for e in elements:
        attr = e.get_attribute('data-video-filepath')
        print("Link del elemento", attr)
        if(attr.rfind('.mp4') != -1):
            videoUrl = attr

    print("6. Creating the file")
    urllib.request.urlretrieve(videoUrl, 'vids/'+filename)
