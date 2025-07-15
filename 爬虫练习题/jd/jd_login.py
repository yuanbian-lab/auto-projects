import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome()
driver.get("https://jd.com")


element = driver.find_element(By.CLASS_NAME, "link-login")
element.click()

time.sleep(3)

element = driver.find_element(By.ID, "loginname")
element.send_keys("luxp4588@126.com")

element = driver.find_element(By.ID, "nloginpwd")
element.send_keys("LINlin52)")
element = driver.find_element(By.ID, "loginsubmit")
element.click()
print("等待拖动滚动条")
time.sleep(3)
element = driver.find_element(By.CSS_SELECTOR, ".JDJRV-slide-btn")
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(element, 100, 0).perform()
time.sleep(3)
actions.drag_and_drop_by_offset(element, 150, 0).perform()
time.sleep(3)
actions.drag_and_drop_by_offset(element, 150, 0).perform()
time.sleep(30)