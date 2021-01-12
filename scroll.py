from math import ceil
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

HEIGHT = 863

browser.get("https://nomadcoders.co")
browser.maximize_window()

sizes = [480, 960, 1366, 1920]

for size in sizes:
    browser.set_window_size(size,HEIGHT)
    time.sleep(1)
    scroll_size = browser.execute_script("return document.body.scrollHeight")
    total_section = ceil(scroll_size / HEIGHT)
    for section in range(total_section+1):
        browser.execute_script(f"window.scrollTo(0,{section*HEIGHT})")
        time.sleep(1)
        browser.save_screenshot(f"screenshots2/{size}x{section}.png")

browser.quit()