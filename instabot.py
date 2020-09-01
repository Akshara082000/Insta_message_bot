from selenium import webdriver
from time import sleep
class InstaBot:
    def __init__(self,username,pw):
        self.driver=webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
      #  self.driver.find_element_by_xpath("//a[contains(text(),'Log in')]").click()
        self.client=#<Client username>#
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        self.driver.find_element_by_xpath("//input[@type=\"text\"]").send_keys(self.client)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]").click()
        sleep(2)

    def get_unfollower(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self._get_names()
        print(len(following))
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self._get_names()
        print(len(followers))
        not_following_back = [user for user in following if user not in followers]
        print(len(not_following_back))
        self.send_message(not_following_back)

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        sleep(1)
        close = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")
        close.click()
        return names
    def send_message(self,names):
        self.driver.find_element_by_xpath("//button[contains(text(),\"Message\")]").click()
        for name in names:
            message="https://www.instagram.com/"+name
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
        
username=#<your username>#
password=#<your password>#
Bot=InstaBot(username,password,client)
Bot.get_unfollower()