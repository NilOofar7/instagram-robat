from selenium.webdriver.common import keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from info import username,userpassword
from time import sleep 
import random
import os
import json


browser = webdriver.Edge()

def Login():
    browser.get('http://instagram.com/')
    sleep(2)
    insta_usernam = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    insta_usernam.send_keys(username)
    sleep(1)
    insta_password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    insta_password.send_keys(userpassword)
    sleep(1)
    insta_password.send_keys(Keys.ENTER)
    sleep(5)

def GetMyFollowings():
    browser.get('https://www.instagram.com/accounts/access_tool/accounts_following_you') # addres URL followin of my instagram
    elm = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/main/button')
    for i in range(2):
        elm.click()
        sleep(3)

    list_id = []
    for nam in browser.find_elements_by_class_name('-utLf'): # list of my folowing's ID
        list_id.append(nam.text)

    print(list_id)
    return list_id

def MyRandom(l):
    y = len(l)
    x = random.randint(0, y-1)
    return l[x]

def GetProfile(id_profile): #محاسبه تعداد فالورها و فالویینگ ها

    browser.get(f'https://www.instagram.com/{id_profile}')
    sleep(4)

    name = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/h1').text
    id = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/h2').text
    number_followers = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text
    number_followings = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text
    # user = {
    #         'Fullname': name,
    #         'ID': id,
    #         ' number_of_followers': number_followers,
    #         'number_of_followings': number_followings,
    #         'list_of_followers' : '  '
    #        }
    user = {'Fullname': name, 'ID': id, 'followers': number_followers, 'followings': number_followings}
    
    if not os.path.exists(id):
        os.mkdir(id)
     
    with open(f'{id}/followers.txt', 'w+', encoding='utf8') as f:
        f.write(json.dumps(user))

    print(user)
    return user
    
def GetListOfFollows(id_profile): #ساخت لیست فالوورهای یکی از فالوویینگ های خودم

    # browser.get(f'https://www.instagram.com/{id_profile}')
    # sleep(4)

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click() # click on folower button
    sleep(2)

    fBody = browser.find_element_by_xpath("//div[@class='isgrP']")
    for i in range(5):
        browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)

    sleep(5)

    list_followers = []
    for nam in browser.find_elements_by_xpath("//div[@class='isgrP']//li"):
        list_followers.append(nam.text)

    sleep(12)
    print(f'list_follower= {list_followers}')
    return list_followers



Login()
f = GetMyFollowings()
id = MyRandom(f)
list1 =GetListOfFollows(id)
GetProfile(id)
GetListOfFollows(id)

with open(f'{id}/followers.txt', 'a+', encoding='utf8') as f:
    for i in list1:
        f.write(i)
    
#----------------------------------------------------