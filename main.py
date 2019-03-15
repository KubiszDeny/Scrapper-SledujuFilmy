from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import os
import time
import sys

#Nastavení Driveru
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-sll-errors')
options.add_argument('log-level=3') #Ignorovat výpis erorů
options.add_argument("--disable-infobars") #DISABLE: Chrome is being controlled by automated test software
#options.add_argument('headless') #Bez Hlavičky
options.add_argument('--blink-settings=imagesEnabled=false') #Bez Obrázků
#options.add_argument("--no-first-run")
#options.add_argument("--disable-default-apps") 
#chrome_options.add_argument("--disable-extensions")
options.add_argument("--disable-javascript") #Vypnout JS 2
options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2}) #Vypnout JS 1
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=options)
os.system('cls')
sys.tracebacklimit = 0

#Scrap Funkce
def scrapy():
#Frame1
	try:
		if driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div/div/div[5]').is_displayed():
			frameA = driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div/div/div[5]/iframe').get_attribute('src')
			obrazek = driver.find_element_by_xpath("//meta[@name='og:image']").get_attribute('content')
			jmeno = driver.title
			zanr = ('')

			file = open("Filmy_json.txt","a", encoding='utf-8') 
			file.write('{')
			file.write('"name": "{0}",'.format(jmeno))
			file.write('"genre": "{0}",'.format(zanr))
			file.write('"thumb": "{0}",'.format(obrazek))
			file.write('"video": "{0}"'.format(frameA))
			file.write('},')
			file.write('\n')
			file.close()
			print('Frame1 OK') #DEBUG
			print(jmeno)
		else:
			print('Frame1 Neexistuje') #DEBUG
	except NoSuchElementException:
		print('Frame1 Neexistuje') #DEBUG

#Frame 2
	try:
		if driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div[2]/div/div[5]/iframe').is_displayed():
			frameB = driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div[2]/div/div[5]/iframe').get_attribute('src')
			obrazek = driver.find_element_by_xpath("//meta[@name='og:image']").get_attribute('content')
			jmeno = driver.title
			zanr = ('')

			file = open("Filmy_json.txt","a", encoding='utf-8') 
			file.write('{')
			file.write('"name": "{0}",'.format(jmeno))
			file.write('"genre": "{0}",'.format(zanr))
			file.write('"thumb": "{0}",'.format(obrazek))
			file.write('"video": "{0}"'.format(frameB))
			file.write('},')
			file.write('\n')
			file.close()
			print('Frame2 OK') #DEBUG
			print(jmeno)
		else:
			print('Frame2 Neexistuje') #DEBUG
	except NoSuchElementException:
		print('Frame2 Neexistuje') #DEBUG

#Frame 3
	try:
		if driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div[3]/div/div[5]/iframe').is_displayed():
			frameC = driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div[3]/div/div[5]/iframe').get_attribute('src')
			obrazek = driver.find_element_by_xpath("//meta[@name='og:image']").get_attribute('content')
			jmeno = driver.title
			zanr = ('')

			file = open("Filmy_json.txt","a", encoding='utf-8') 
			file.write('{')
			file.write('"name": "{0}",'.format(jmeno))
			file.write('"genre": "{0}",'.format(zanr))
			file.write('"thumb": "{0}",'.format(obrazek))
			file.write('"video": "{0}"'.format(frameC))
			file.write('},')
			file.write('\n')
			file.close()
			print('Frame3 OK') #DEBUG
			print(jmeno)
		else:
			print('Frame3 Neexistuje') #DEBUG
	except NoSuchElementException:
		print('Frame3 Neexistuje') #DEBUG

#Frame 4 
	try:
		if driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div[4]/div/div[5]/iframe').is_displayed():
			frameD = driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div[4]/div/div[5]/iframe').get_attribute('src')
			obrazek = driver.find_element_by_xpath("//meta[@name='og:image']").get_attribute('content')
			jmeno = driver.title
			zanr = ('')

			file = open("Filmy_json.txt","a", encoding='utf-8') 
			file.write('{')
			file.write('"name": "{0}",'.format(jmeno))
			file.write('"genre": "{0}",'.format(zanr))
			file.write('"thumb": "{0}",'.format(obrazek))
			file.write('"video": "{0}"'.format(frameD))
			file.write('},')
			file.write('\n')
			file.close()
			print('Frame4 OK') #DEBUG
			print(jmeno)
		else:
			print('Frame4 Neexistuje') #DEBUG
	except NoSuchElementException:
		print('Frame4 Neexistuje') #DEBUG

#Frame 5 
	try:
		if driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div[5]/div/div[5]/iframe').is_displayed():
			frameE = driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div[5]/div/div[5]/iframe').get_attribute('src')
			obrazek = driver.find_element_by_xpath("//meta[@name='og:image']").get_attribute('content')
			jmeno = driver.title
			zanr = ('')

			file = open("Filmy_json.txt","a", encoding='utf-8') 
			file.write('{')
			file.write('"name": "{0}",'.format(jmeno))
			file.write('"genre": "{0}",'.format(zanr))
			file.write('"thumb": "{0}",'.format(obrazek))
			file.write('"video": "{0}"'.format(frameE))
			file.write('},')
			file.write('\n')
			file.close()
			print('Frame5 OK') #DEBUG
			print(jmeno)
		else:
			print('Frame5 Neexistuje') #DEBUG
	except NoSuchElementException:
		print('Frame5 Neexistuje')  #DEBUG

#Zapsat ID Filmu + url a scrap
def film_id():
	ids = driver.find_element_by_xpath('//*[@id="play_block"]/a').get_attribute('data-loc')
	#Zapsat (DEBUG)
	file = open("filmid.txt","a", encoding='utf-8') 
	file.write(ids)
	file.write('\n')
	file.close()
	print(ids) #DEBUG
	id_url = 'http://stream-a-ams1xx2sfcdnvideo5269.eu/okno.php?movie={0}&new_way'.format(ids)
	driver.get(id_url)

	scrapy()


page = 1310
while page < 1758:
	print(page) #DEBUG
	urlio = 'https://sledujufilmy.cz/?pg={0}'.format(page)
	driver.get(urlio)

	#Ziskat data 
	try:
		filmQ = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[4]/div[2]/div[2]/a').get_attribute('href')
	except NoSuchElementException:
		filmQ = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[4]/div[2]/div/a').get_attribute('href')
	try:		
		filmW = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[5]/div[2]/div[2]/a').get_attribute('href')
	except NoSuchElementException:
		filmW = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[5]/div[2]/div/a').get_attribute('href')
	try:
		filmE = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[6]/div[2]/div[2]/a').get_attribute('href')
	except NoSuchElementException:
		filmE = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[6]/div[2]/div/a').get_attribute('href')
	try:
		filmR = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[7]/div[2]/div[2]/a').get_attribute('href')
	except NoSuchElementException:
		filmR = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[7]/div[2]/div/a').get_attribute('href')
	try:
		filmT = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[8]/div[2]/div[2]/a').get_attribute('href')
	except NoSuchElementException:
		filmT = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[8]/div[2]/div/a').get_attribute('href')
	try:
		filmZ = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[9]/div[2]/div[2]/a').get_attribute('href')
	except NoSuchElementException:
		filmZ = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[9]/div[2]/div/a').get_attribute('href')
	try:
		filmU = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[10]/div[2]/div[2]/a').get_attribute('href')
	except NoSuchElementException:
		filmU = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[10]/div[2]/div/a').get_attribute('href')
	try:
		filmI = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[11]/div[2]/div[2]/a').get_attribute('href')
	except NoSuchElementException:
		filmI = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[11]/div[2]/div/a').get_attribute('href')
	try:
		filmO = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[12]/div[2]/div[2]/a').get_attribute('href')
	except NoSuchElementException:
		filmO = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[12]/div[2]/div/a').get_attribute('href')

	driver.get(filmQ)
	film_id()

	driver.get(filmW)
	film_id()

	driver.get(filmE)
	film_id()

	driver.get(filmR)
	film_id()

	driver.get(filmT)
	film_id()

	driver.get(filmZ)
	film_id()

	driver.get(filmU)
	film_id()

	driver.get(filmI)
	film_id()

	driver.get(filmO)
	film_id()

	page += 1

