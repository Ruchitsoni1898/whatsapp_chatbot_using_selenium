import sys
import time
from selenium import webdriver

def user_chat(name_user):
    try:
        chat_new = browser.find_element("XPATH", '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')
        chat_new.click()
        user_chat = browser.find_element("XPATH", '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/div/div/label/input')
        user_chat.send_keys(name_user)
        time.sleep(2)

        try:
            user = browser.find_element("XPATH", f'//span[@title="{name_user}"]')
            user.click()
        except Exception as e:
            print(f"User {name_user} is not in the contacts")

        time.sleep(10)
        box_message = browser.find_element("XPATH", '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
        box_message.send_keys("Hey Jinal Here.... using the whatsapp bot")

        send_button = browser.find_element("XPATH", '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]/button')
        send_button.click()
        time.sleep(20)
    except Exception as e:
        print(e)
        browser.close()
        sys.exit()

if __name__ == '__main__':
    my_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=my_options)
    browser.get("https://web.whatsapp.com/")
    time.sleep(20)

    name_list = ['Jinal Anand']
    for name_user in name_list:
        user_chat(name_user)

    browser.close()
