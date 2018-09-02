from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver import ChromeOptions, Chrome
import time

def main():
    opts = ChromeOptions()

    opts.add_experimental_option("detach", True)
    opts.add_argument("--incognito")

    chromedriver = '/home/zak/chromedriver'

    driver = webdriver.Chrome(chromedriver,0,opts)
    driver.get('https://www.mohmal.com/en')

    driver_nord = webdriver.Chrome(chromedriver,0,opts)
    driver_nord.get('https://free.nordvpn.com/')

    start_button = driver.find_element_by_xpath('//*[@id="rand"]')
    start_button.click()

    change_button = driver.find_element_by_xpath('//*[@id="delete"]')
    change_button.click()

    str_email = driver.find_element_by_xpath('//*[@id="email"]/div[1]')
    str_email_value = str_email.get_attribute('data-email')
    print(str_email_value)

    nord_email_value = driver_nord.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]')
    nord_email_value.clear()
    nord_email_value.send_keys(str_email_value)

    nord_submit = driver_nord.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/button[1]/span[1]')
    nord_submit.click()

    wait = ui.WebDriverWait(driver_nord,600)

    wait.until(lambda driver_nord: driver_nord.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]'))
    driver_nord.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]').click()

    time.sleep(10)

    driver.find_element_by_xpath('//*[@id="refresh"]/i[1]').click()

    driver.find_element_by_xpath('//*[@id="inbox-table"]/tbody[1]/tr[1]/td[1]/a[1]').click()

    continue_link = driver.find_element_by_link_text('Set Password and Activate Account')

    time.sleep(3)
    continue_link.click()


main()