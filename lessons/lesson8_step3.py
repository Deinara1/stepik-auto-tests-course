from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_num = browser.find_element_by_xpath("//span[@id = 'num1']")
    first = first_num.text
    second_num = browser.find_element_by_xpath("//span[@id = 'num2']")
    second = second_num.text
    summa = str((int(first) + int(second)))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(summa)
    button = browser.find_element_by_xpath("//button")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла