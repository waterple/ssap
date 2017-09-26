# -*- coding: utf-8 -*-
'''chromedriver path : at _path_cd'''

from time import sleep
from selenium import webdriver
from sys import exit
_path_cd = './chromedriver.exe'

def work(argv):
	_id = argv[1]
	_pw = argv[2]

	_1 = int(argv[3])
	_2 = int(argv[4])
	_3 = int(argv[5])
	_4 = int(argv[6])

	driver = webdriver.Chrome(executable_path=_path_cd)

	driver.get('https://djs.weschool.kr/front.html')
	sleep(0.8)


	btn = driver.find_element_by_name('UID')
	btn.send_keys(_id)
	btn = driver.find_element_by_name('PASSWD')
	btn.send_keys(_pw)
	btn.submit()
	sleep(0.8)

	try:
		driver.get('https://djs.weschool.kr/sph_manager/prep/registration.php')
	except:
		driver.quit()
		sys.exit()

	sleep(0.8)

	if _1 != 0:
		while True:
			try:
				btn = driver.find_element_by_id('btn_app_1_')
				break
			except:
				pass
		btn.click()
		sleep(.5)

		while True:
			btn = driver.find_elements_by_name('facil_id')
			if len(btn)>0:
				break

		btn[_1 - 1].click()

		btn = driver.find_element_by_id('btn_submit')
		btn.click()

		while True:
			try:
				btn = driver.find_element_by_id('btn_save')
				break
			except:
				pass
		btn.click()
		
		driver.get('https://djs.weschool.kr/sph_manager/prep/registration.php')

	if _2 != 0:
		while True:
			try:
				btn = driver.find_element_by_id('btn_app_2_')
				break
			except:
				pass
		btn.click()
		sleep(.5)

		while True:
			btn = driver.find_elements_by_name('facil_id')
			if len(btn)>0:
				break
		
		btn[_2 - 1].click()
		btn = driver.find_element_by_id('btn_submit')
		btn.click()
		while True:
			try:
				btn = driver.find_element_by_id('btn_save')
				break
			except:
				pass
		btn.click()
		
		driver.get('https://djs.weschool.kr/sph_manager/prep/registration.php')

	if _3 != 0:
		while True:
			try:
				btn = driver.find_element_by_id('btn_app_3_')
				break
			except:
				pass
		btn.click()
		sleep(.5)

		while True:
			btn = driver.find_elements_by_name('facil_id')
			if len(btn)>0:
				break

		btn[_3 - 1].click()
		btn = driver.find_element_by_id('btn_submit')
		btn.click()
		while True:
			try:
				btn = driver.find_element_by_id('btn_save')
				break
			except:
				pass
		btn.click()
		
		driver.get('https://djs.weschool.kr/sph_manager/prep/registration.php')

	if _4 != 0:
		while True:
			try:
				btn = driver.find_element_by_id('btn_app_4_')
				break
			except:
				pass
		btn.click()
		sleep(.5)

		while True:
			btn = driver.find_elements_by_name('facil_id')
			if len(btn)>0:
				break
		
		btn[_4 - 1].click()
		btn = driver.find_element_by_id('btn_submit')
		btn.click()
		while True:
			try:
				btn = driver.find_element_by_id('btn_save')
				break
			except:
				pass
		btn.click()
		
		driver.get('https://djs.weschool.kr/sph_manager/prep/registration.php')

	driver.quit()

	exit()