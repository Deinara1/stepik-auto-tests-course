from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_xpath("//span[@id = 'input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(y)

    checkbox_robot = browser.find_element_by_xpath("//input[@id= 'robotCheckbox']")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox_robot)
    checkbox_robot.click()

    radio_robot = browser.find_element_by_xpath("//input[@id= 'robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robot)
    radio_robot.click()

    button = browser.find_element_by_xpath("//button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла