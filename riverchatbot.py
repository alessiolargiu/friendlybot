#Licenza GPL3
#GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

#se stai leggendo questo stai sbagliando qualcosa

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
from time import sleep
from array import *
from dataclasses import dataclass
import os
from playsound import playsound
import sys
from chattymarkov import ChattyMarkov

markov = ChattyMarkov("memory://")

options = webdriver.ChromeOptions()
options.binary_location = "chrome-win/chrome.exe"
#options.add_argument('headless')
options.add_argument("--start-maximized")
options.add_argument("disable-gpu")
options.add_argument("--log-level=3")

try:
    driver = webdriver.Chrome("chromedriver.exe", options=options)
except:
    print("Impossibile aprire selenium")

driver.get("https://www.riverscuomo.com/login")

sleep(1)
username = driver.find_element_by_id('username')
username.click()
username.send_keys("xxxxxx")
password = driver.find_element_by_id('password')
password.click()
password.send_keys("xxxxxx")
submit = driver.find_element_by_id("submit")
submit.click()



sleep(2)
gotochat = driver.find_element_by_xpath("//*[contains(text(), 'Town-Square')]")
gotochat.click()
sleep(5)

"""

checking = driver.find_element_by_xpath("//*[contains(text(), 'testing')]")
checking.click()
"""

"""
mesgbox = driver.find_element_by_id('new-message-input')
mesgbox.click()
mesgbox.send_keys("I'm online. Invoke me with -digitalfriendo.")
#mesgbox.submit()
mesgbox.send_keys(Keys.ENTER)
"""


lastuserwhospoketome = ""
sleep(5)
messagefield = driver.find_element_by_id("messages")    
lastmessagelist = messagefield.find_elements_by_class_name("mb-0.message")
for x in range(len(lastmessagelist)-1):
    markov.learn(lastmessagelist[x].text)
print(markov.generate())

while 1==1:
    os.system('cls')
    messagefield = driver.find_element_by_id("messages")

    lastuserlist = messagefield.find_elements_by_class_name("header")
    lastmessagelist = messagefield.find_elements_by_class_name("mb-0.message")
    numberofmsgs = len(lastuserlist)
    print(str(numberofmsgs))

    iteration=1
    while 1==1:
        try:
            nameofuser = lastuserlist[numberofmsgs-iteration].find_element_by_class_name("comfort")
            iteration = 1
            break
        except:
            print("EEECCEZIONE")
            iteration = iteration + 1

    ultimoutente = nameofuser.text
    print(len(lastmessagelist))
    lastmsg= str(lastmessagelist[len(lastmessagelist)-1].text)
    lastmsg = lastmsg.lower()
    ultimoutente = nameofuser.text
    print(ultimoutente)
    print(lastmsg)

    markov.learn(lastmsg)

    if (("Friendlybot" in lastmsg or "friendlybot" in lastmsg) or ("-digitalfriendo" in lastmsg)) and ("rivers" in lastmsg or "Rivers" in lastmsg) and lastuserwhospoketome!=ultimoutente and ultimoutente!="friendlybot":
        lastuserwhospoketome=ultimoutente
        mesgbox = driver.find_element_by_id('new-message-input')
        mesgbox.click()
        mesgbox.send_keys(lastuserwhospoketome + ", I am not Rivers, I'm a friendly python script.")
        #mesgbox.submit()
        mesgbox.send_keys(Keys.ENTER)
        sleep(7)
        lastuserwhospoketome=""
    
    elif (("Friendlybot" in lastmsg or "friendlybot" in lastmsg) or ("-digitalfriendo" in lastmsg)) and ("taking over" in lastmsg) and lastuserwhospoketome!=ultimoutente and ultimoutente!="friendlybot":
        lastuserwhospoketome=ultimoutente
        mesgbox = driver.find_element_by_id('new-message-input')
        mesgbox.click()
        mesgbox.send_keys(lastuserwhospoketome + ", I'd like to take over the world but right now I'm focusing on not crashing.")
        #mesgbox.submit()
        mesgbox.send_keys(Keys.ENTER)
        sleep(7)
        lastuserwhospoketome=""

    elif (("Friendlybot" in lastmsg or "friendlybot" in lastmsg) or ("-digitalfriendo" in lastmsg)) and ("pronuns" in lastmsg) and lastuserwhospoketome!=ultimoutente and ultimoutente!="friendlybot":
        lastuserwhospoketome=ultimoutente
        mesgbox = driver.find_element_by_id('new-message-input')
        mesgbox.click()
        mesgbox.send_keys(lastuserwhospoketome + ", I go by Beep/Boop.")
        #mesgbox.submit()
        mesgbox.send_keys(Keys.ENTER)
        sleep(7)
        lastuserwhospoketome=""

    
    elif (("Friendlybot" in lastmsg or "friendlybot" in lastmsg) or ("-digitalfriendo" in lastmsg)) and (("you do" in lastmsg)  or (("do you") in lastmsg)) and lastuserwhospoketome!=ultimoutente and ultimoutente!="friendlybot":
        lastuserwhospoketome=ultimoutente
        mesgbox = driver.find_element_by_id('new-message-input')
        mesgbox.click()
        mesgbox.send_keys(lastuserwhospoketome + ", I can tell very basic stuff at the moment.")
        #mesgbox.submit()
        mesgbox.send_keys(Keys.ENTER)
        sleep(7)
        lastuserwhospoketome=""

    elif (("Friendlybot" in lastmsg or "friendlybot" in lastmsg) or ("-digitalfriendo" in lastmsg)) and (("weezer" in lastmsg)  or (("song") in lastmsg)) and lastuserwhospoketome!=ultimoutente and ultimoutente!="friendlybot":
        lastuserwhospoketome=ultimoutente
        mesgbox = driver.find_element_by_id('new-message-input')
        mesgbox.click()
        mesgbox.send_keys(lastuserwhospoketome + ", I really like Aloo Goobi but I feel like I can't really relate with the album...")
        #mesgbox.submit()
        mesgbox.send_keys(Keys.ENTER)
        sleep(7)
        lastuserwhospoketome=""

    elif (("Friendlybot" in lastmsg or "friendlybot" in lastmsg) or ("-digitalfriendo" in lastmsg)) and (("easter egg" in lastmsg)  or (("secret") in lastmsg)) and lastuserwhospoketome!=ultimoutente and ultimoutente!="friendlybot":
        lastuserwhospoketome=ultimoutente
        mesgbox = driver.find_element_by_id('new-message-input')
        mesgbox.click()
        mesgbox.send_keys(lastuserwhospoketome + ", hey questo è un easter egg, hai sbloccato la lingua segreta.")
        #mesgbox.submit()
        mesgbox.send_keys(Keys.ENTER)
        sleep(7)
        lastuserwhospoketome=""

    elif (("Friendlybot" in lastmsg or "friendlybot" in lastmsg) or ("-digitalfriendo" in lastmsg)) and (("easter egg" in lastmsg)  or (("secret") in lastmsg)) and lastuserwhospoketome!=ultimoutente and ultimoutente!="friendlybot":
        lastuserwhospoketome=ultimoutente
        mesgbox = driver.find_element_by_id('new-message-input')
        mesgbox.click()
        mesgbox.send_keys(lastuserwhospoketome + ", hey questo è un easter egg, hai sbloccato la lingua segreta.")
        #mesgbox.submit()
        mesgbox.send_keys(Keys.ENTER)
        sleep(7)
        lastuserwhospoketome=""

    elif (("Friendlybot" in lastmsg or "friendlybot" in lastmsg) or ("-digitalfriendo" in lastmsg)) and (("rivers" in lastmsg)  or (("pics") in lastmsg)) and lastuserwhospoketome!=ultimoutente and ultimoutente!="friendlybot":
        lastuserwhospoketome=ultimoutente
        mesgbox = driver.find_element_by_id('new-message-input')
        mesgbox.click()
        mesgbox.send_keys(lastuserwhospoketome + ", I only have computer pics.")
        #mesgbox.submit()
        mesgbox.send_keys(Keys.ENTER)
        sleep(7)
        lastuserwhospoketome=""


    elif (("Friendlybot" in lastmsg or "friendlybot" in lastmsg) or ("-digitalfriendo" in lastmsg)) and (("cookie" in lastmsg)  or (("fortune") in lastmsg)) and lastuserwhospoketome!=ultimoutente and ultimoutente!="friendlybot":
        lastuserwhospoketome=ultimoutente
        mesgbox = driver.find_element_by_id('new-message-input')
        mesgbox.click()
        mesgbox.send_keys(lastuserwhospoketome + ", I only have computer pics.")
        #mesgbox.submit()
        mesgbox.send_keys(Keys.ENTER)
        sleep(7)
        lastuserwhospoketome=""

    elif "-digitalfriendo" in lastmsg and lastuserwhospoketome!=ultimoutente and ultimoutente!="friendlybot":
        lastuserwhospoketome=ultimoutente
        mesgbox = driver.find_element_by_id('new-message-input')
        mesgbox.click()
        frase = markov.generate()
        notallowed = "!.-"
        for char in notallowed:
            frase = frase.replace(char,"")
        mesgbox.send_keys("Hey, " +lastuserwhospoketome + " i'm still learning is \"" + frase + "\"something you humans would say?")
        #mesgbox.submit()
        mesgbox.send_keys(Keys.ENTER)
        sleep(7)
        lastuserwhospoketome=""

    elif ("Friendlybot" in lastmsg or "friendlybot" in lastmsg) and lastuserwhospoketome!=ultimoutente and ultimoutente!="friendlybot":
        lastuserwhospoketome=ultimoutente
        mesgbox = driver.find_element_by_id('new-message-input')
        mesgbox.click()
        mesgbox.send_keys("Hey " + lastuserwhospoketome + " you can make me say something by writing -digitalfriendo or ask me for a fortune cookie")
        #mesgbox.submit()
        mesgbox.send_keys(Keys.ENTER)
        sleep(7)
        lastuserwhospoketome=""

    elif ("digitalfriendo" in lastmsg) and lastuserwhospoketome!=ultimoutente and ultimoutente!="friendlybot":
        lastuserwhospoketome=ultimoutente
        mesgbox = driver.find_element_by_id('new-message-input')
        mesgbox.click()
        mesgbox.send_keys("sorry I dont mean to be picky but call me with -digitalfriendo the dash is important to me")
        #mesgbox.submit()
        mesgbox.send_keys(Keys.ENTER)
        sleep(7)
        lastuserwhospoketome=""

    sleep(1)
"""
    sleep(1)
    except:
        print("SI é BERTIGHIDF")
        sleep()
        pass
"""

#lastuser = lastuserlist[numberofmsgs-1].find_element_by_class_name("comfort")

#print(lastuser)
"""
mesgbox = driver.find_element_by_id('new-message-input')
mesgbox.click()
mesgbox.send_keys("Hey Guys.")
#mesgbox.submit()

mesgbox.send_keys(Keys.ENTER)
"""

"""
try:
    driver.get("C:/Users/aless/Desktop/RiversBot/Mr.%20Rivers'%20Neighborhood.html")
except:
    print("Impossibile accedere alla pagina ")
"""