from selenium import webdriver
import time
import requests
import json
import warnings

mailapi = str(input("Please Enter your kopeechka API key!"))

warnings.filterwarnings("ignore", category=DeprecationWarning) 

#tiktok detection bypass
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options) #driver path

driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36'})
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#driver.add_cookie({"name":"cookie-consent", "domain":".tiktok.com", "value":"{%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22version%22:%22v8%22}"})

driver.get("https://www.tiktok.com/")
#driver.find_element_by_xpath('/html/body/tiktok-cookie-banner//div/div[2]/button[2]').click()
#time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/button').click()
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/div[2]/a/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/div[1]/div/div/a/div').click()
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/form/div[3]/div[1]/div[1]').click()
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/form/div[3]/div[1]/div[2]/div[10]').click()
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/form/div[3]/div[2]/div[1]').click()
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/form/div[3]/div[2]/div[2]/div[8]').click()
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/form/div[3]/div[3]/div[1]').click()
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/form/div[3]/div[3]/div[2]/div[35]').click()
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/form/div[5]/a').click()

inboxcreate = requests.get(f"http://api.kopeechka.store/mailbox-get-email?site=tiktok.com&mail_type=mail.com&token={mailapi}")
inboxfull = inboxcreate.text
inboxjson = json.loads(inboxfull)
inbox = inboxjson['mail']
inboxid = inboxjson['id']
print(inbox)
print(inboxid)

driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/form/div[6]/div/input').send_keys(inbox) #Enters Email
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/form/div[7]/div/input').send_keys("GoodPASS123!") #Enters Password
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/form/div[8]/div/button').click()

time.sleep(15)
getcode = requests.get(f"http://api.kopeechka.store/mailbox-get-message?id={inboxid}&token={mailapi}&api=2.0")
codefull = getcode.text
codejson = json.loads(codefull)
code = codejson['value']
print(code)

driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/form/div[8]/div/div/input').send_keys(code)
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/form/button').click()
time.sleep(10)



