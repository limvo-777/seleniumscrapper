from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

KEYWORD = "buy stocks"

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("http://google.com")


search_bar = browser.find_element_by_class_name("gLFyf")

search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

rm_element = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CLASS_NAME,"g-blk")))
rm_element2 = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CLASS_NAME,"kno-kp")))



browser.execute_script("""
    const rm = arguments[0];
    const rm2 = arguments[1];
    rm.parentElement.removeChild(rm);
    rm2.parentElement.removeChild(rm2);
""",
    rm_element, rm_element2,
)

search_results = browser.find_elements_by_class_name("g")

for index, result in enumerate(search_results):
    result.screenshot(f"screenshots/{KEYWORD}x{index}.png")

browser.quit()

