from time import sleep

import sys

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select

import pytesseract

from PIL import Image, ImageEnhance, ImageFilter

## 訂票第一頁

chrome_path = "C:\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

target_page = "http://railway.hinet.net/ctno1.htm"

driver.get(target_page)

driver.maximize_window()

form_page = driver.find_element_by_xpath('//*[@id="person_id"]')

form_page.send_keys("A166129192")

form_page = Select(driver.find_element_by_xpath('//*[@id="from_station"]'))		
#選單使用select目標xpath

form_page.select_by_value('100')	
#再查其option value即可選擇

form_page = Select(driver.find_element_by_xpath('//*[@id="to_station"]'))

form_page.select_by_value('102')

form_page = Select(driver.find_element_by_xpath('//*[@id="getin_date"]'))

form_page.select_by_value('2017/06/04-09')

form_page = driver.find_element_by_xpath('//*[@id="train_no"]')

form_page.send_keys("1191")

form_page = Select(driver.find_element_by_xpath('//*[@id="order_qty_str"]'))

form_page.select_by_value('1')

![https://github.com/BarryFu/python/blob/master/selenium/pic/page1.png]

form_page = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[9]/td[2]/button')

form_page.click()		#按按鈕找到xpath後，可直接click


sleep(2)

## 第二頁選擇圖片

picture = driver.find_element_by_xpath('//*[@id="idRandomPic"]')

driver.save_screenshot('screen1.png')

sleep(1)

!(https://github.com/BarryFu/python/blob/master/selenium/pic/screen1.png)

location = picture.location

size=picture.size	#先把隨機出現的圖片擷取下來

rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))

i=Image.open('screen1.png')	#用Image打開圖片	

frame4=i.crop(rangle)	#rangle會把目標外的圖給刪除

frame4.save('123.png')

qq=Image.open('123.png')

!(https://github.com/BarryFu/python/blob/master/selenium/pic/123.png)

imgry = qq.convert('L')

sharpness =ImageEnhance.Contrast(imgry)

sharp_img = sharpness.enhance(2.0)

sharp_img.save('123h.png')

!(https://github.com/BarryFu/python/blob/master/selenium/pic/123h.png)

text=pytesseract.image_to_string(sharp_img)

print text
