from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

SIMILAR_ACCOUNT = "instagram_username"   # 'chefclubtv'
CHROME_DRIVER_PATH = "/home/.../chromedriver"
USERNAME = "your instagram login"
PASSWORD = 'your instagram parol'


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(2)
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')  # find_elements_by_tag_name("button")[0]

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(2)

        not_now = self.driver.find_elements_by_tag_name("button")[1]  # find_element_by_css_selector(".cmbtv button")
        not_now.click()
        time.sleep(1)

                                                    # body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm
        not_now2 = self.driver.find_elements_by_tag_name("button")
        for knopka in not_now2:
            if knopka.text == "Not Now":   # nmadir bovotti
                not_now2 = knopka
        not_now2.click()

    def find_followers(self):
        url = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"
        self.driver.get(url)
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        # follow_click = self.driver.find_elements_by_css_selector("ul li button")
        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            follow_click = self.driver.find_elements_by_css_selector("ul li button")
            n = 0
            for button in follow_click:
                if button.text == "Requested" or button.text == "Following":
                    continue
                else:
                    button.click()
                    time.sleep(1)
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", button)
                    n += 1
                if n == 10:
                    break
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        pass


insta = InstaFollower(CHROME_DRIVER_PATH)
insta.login()
insta.find_followers()
insta.follow()
