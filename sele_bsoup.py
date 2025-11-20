from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
file = 0
for i in range(1, 26):
    driver.get(f"https://www.flipkart.com/search?q=smartwatch&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=smartwatch%7CSmart+Watches&requestId=0346cb15-901c-4cf4-bcdb-9d04bd1170a9&as-searchtext=smartw&page={i}")
    elems = driver.find_elements(By.CLASS_NAME, "_1sdMkc")
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/smartwatch_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
driver.close()
print("finished!!")
