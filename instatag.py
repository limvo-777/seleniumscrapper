import time
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
INSTAGRAM_ID = "01084650230"

main_hashtag = "surfing"

browser.get("https://www.instagram.com/accounts/login/")
WebDriverWait(browser, 3).until(
EC.presence_of_element_located((By.CLASS_NAME, "_2hvTZ")))

insta_id = browser.find_element_by_name("username")
insta_password = browser.find_element_by_name("password")

insta_id.send_keys(INSTAGRAM_ID)
insta_password.send_keys(input("What is your password"))
insta_password.send_keys(Keys.ENTER)


# browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")

header = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.TAG_NAME,"header")))

search_bar = browser.find_element_by_class_name("XTCLo")
search_bar.send_keys(f"#{main_hashtag}")
time.sleep(1)
search_tag = browser.find_element_by_class_name("fuqBx")

hashtags = search_tag.find_elements_by_class_name("yCE8d")
report = []


for hashtag in hashtags:

    # ActionChains(browser).context_click(hashtag).send_keys("t").perform()
    # ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").perform()
    # ActionChains(browser).context_click(hashtag).perform()
    # time.sleep(3)
    # ActionChains(browser).send_keys("t").perform()
    # time.sleep(3)
    rep = hashtag.text.replace( "," , "").split("\n")

    report.append((rep))


print(report)
file = open(f"screenshots3/{main_hashtag}-report.csv", "w")
writer = csv.writer(file)
writer.writerow(["Hashtag", "Post Count"])

for hashtag in report :
    writer.writerow(hashtag)
browser.quit()