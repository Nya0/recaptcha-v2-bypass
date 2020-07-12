import selenium
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from converter import convert
from recognition import recognize
import time
    
optionss = webdriver.FirefoxOptions()
optionss.add_argument("--disable-popup-blocking")
optionss.add_argument("--disable-extensions")

browser = webdriver.Firefox(options=optionss)
    
browser.get("https://www.google.com/recaptcha/api2/demo")

if "iframe" in browser.page_source:
	
	    recaptchaFrame = browser.find_element_by_tag_name("iframe")
	    frameName = recaptchaFrame.get_attribute('name')
    
	    print(frameName)
 
	    browser.switch_to.frame(recaptchaFrame)

	    CheckBox = WebDriverWait(browser, 10).until(
		EC.presence_of_element_located((By.ID ,"recaptcha-anchor"))
		)

	    CheckBox.send_keys(Keys.ENTER)

	    browser.switch_to.default_content()

	    time.sleep(5)
    
	    captcha = browser.find_elements_by_tag_name("iframe")[2]

	    print(captcha)

	    browser.switch_to.frame(captcha)

	    time.sleep(5)

	    audio = browser.find_element_by_css_selector('#recaptcha-audio-button')

	    time.sleep(10)

	    audio.send_keys(Keys.ENTER)

	    browser.switch_to.default_content()

	    time.sleep(2)

	    voice = browser.find_elements_by_tag_name("iframe")[2]

	    browser.switch_to.frame(voice)

	    time.sleep(2)

	    download = browser.find_element_by_css_selector('.rc-audiochallenge-tdownload-link')

	    download.send_keys(Keys.ENTER)

	    time.sleep(15)

	    convert()

	    recognize()
	    
	    result = browser.find_element_by_css_selector('#audio-response')
	    result.send_keys(recognize.text , Keys.ENTER)
		    
	    time.sleep(15)
	    
	    while "iframe" in browser.page_source:
		    download = browser.find_element_by_css_selector('.rc-audiochallenge-tdownload-link')
		    download.send_keys(Keys.ENTER)
		
		    time.sleep(15)

		    convert()

		    recognize()

		    result = browser.find_element_by_css_selector('#audio-response')
		    result.send_keys(recognize.text , Keys.ENTER)
		    
		    os.remove('./Downloads/audio.mp3')
		    os.remove('./Downloads/audio.wav')
		    
	    print("reCaptcha Bypass Successful")
	    browser.quit()

else:
	print("No reCaptcha in frame")
	browser.quit()
