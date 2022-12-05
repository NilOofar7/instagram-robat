from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver

class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Edge()
        self.email = email
        self.password = password
        
    def signIn(self):
        self.browser.get('http://instagram.com/')
        sleep(2)

        emailInput = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        sleep(5)
        
    def requests(self):
        list_of_usernames = []
        self.browser.get('https://www.instagram.com/accounts/access_tool/current_follow_requests')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/article/main/button')

        for item in range(2):
            self.browser.send_keys(Keys.ENTER)
            sleep(3)

        for names in self.browser.find_elements_by_class_name('-utLf'):
            list_of_usernames.append(names.text)
        
        return list_of_usernames

    def unfollow(self, requestList):
        for username in requestList:
            try:
                self.browser.get(f'http://instagram.com/{username}')
                sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div/button').click()
                sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
                print(username + " has been unfollowed")
                sleep(2)
            except:
                self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
                sleep(2)
    
    def profile(self):
        self.browser.get('http://www.instagram.com')
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a').click()
        sleep(3)


        username = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/h2').getText()
        postCount = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span').getText()
        followerCount = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').getText()
        followingCount = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').getText()

        return {
            'username': username, 
            'postCount': postCount,
            'followerCount': followerCount,
            'followingCount': followingCount,
        }

    def getFollowers(self, username):
        self.browser.get(f'http://instagram.com/{username}')
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(1)

        followers = self.browser.find_elements_by_class_name('wo9IH')
        print (followers)

#--------------------------------------------
email = input('Email Address : ')      
password = input('Enter Password : ')
bot=InstagramBot(email, password)
bot.signIn()
print(bot.profile())
print(bot.getFollowers('ebi'))

#bot.unfollow(requests)
#bot.unfollow(bot.requests())