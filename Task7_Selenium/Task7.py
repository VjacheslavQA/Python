from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Page_elements import FormPage
import time

url = "https://httpbin.org/forms/post"

def form_to_fill():
    driver_service = Service(executable_path="/Users/podlypenskyi/Python/Task7_Selenium/chromedriver")
    driver = webdriver.Chrome(service=driver_service)
    driver.get(url)

    try:

        page = FormPage(driver)
        page.customer_name = 'Tester'
        page.tel = '+38097654321'
        page.email = 'putler@kaput'
        page.medium_size.click()
        page.bacon_topping.click()
        page.cheese_topping.click()
        page.mushroom_topping.click()
        page.delivery = '12.30'
        page.comments = 'I won\'t wait more than 30min'
        page.submit.click()

    finally:
        time.sleep(10)
        driver.quit()





if __name__ == '__main__':
    form_to_fill()