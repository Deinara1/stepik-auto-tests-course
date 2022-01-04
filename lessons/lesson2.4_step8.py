from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element(By.XPATH, "//button[@id = 'book']")
    button.click()

    x_element = browser.find_element_by_xpath("//span[@id = 'input_value']")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element_by_xpath("//input[@id ='answer']")
    answer_input.send_keys(y)

    button_submit = browser.find_element_by_xpath("//button[text()='Submit']")
    button_submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла