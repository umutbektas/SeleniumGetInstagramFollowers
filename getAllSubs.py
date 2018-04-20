from selenium import webdriver
import time

#edit here you instagram account info
url = "https://instagram.com"
username = "username"
password = "password"

#open instagram
browser = webdriver.Chrome()
browser.get(url)
time.sleep(2)

#click login link
loginLink = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
loginLink.click()
time.sleep(2)

#filling username and password
usernameArea = browser.find_element_by_name("username")
passwordArea = browser.find_element_by_name("password")

usernameArea.send_keys(username)
passwordArea.send_keys(password)
time.sleep(2)

#click login button and login
loginButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/span/button")
loginButton.click()
time.sleep(3)

#if you have new account and open reactivated page uncomment bottom line

# reactivatedLink = browser.find_element_by_xpath("//*[@id='react-root']/div/div[2]/a[2]")
# reactivatedLink.click()
# time.sleep(1)

#click profile link
profileLink = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a")
profileLink.click()
time.sleep(1)

#click followers link
followersLink = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/header/section/ul/li[2]/a")
followersLink.click()
time.sleep(2)

#scroll down js code
jscommand = """
followers = document.querySelector("._gs38e");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage = followers.scrollHeight;
return lenOfPage;
"""

lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True

time.sleep(5)

#get the followers usernames
followersData = []
followersList = browser.find_elements_by_css_selector("._2g7d5.notranslate._o5iw8")

for follower in followersList:
    followersData.append(follower.text)

#writing followers username in followers.txt
with open("followers.txt", "w", encoding="UTF-8") as file:
    for follower in followersData:
        file.write(follower + "\n")

time.sleep(2)

#that's it ! :D and close
browser.close()
