import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from twilio.rest import Client


account_sid = "AC3ccee2569f6c9e72707498f2af12d551"
auth_token = "b0bf61f7eb31a4fd97bb82f6aca8264b"
phone_number = "+19388884001"
my_phone="+923005067673"

client = Client(account_sid, auth_token)

def clear_console():
    os.system('cls')

clear_console()

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
search_title = "Ocama Effects"

#0 - Video
#1 - Channel


choice = 1
driver.get('https://www.youtube.com')

search = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
search.send_keys(search_title)
search.send_keys(Keys.RETURN)

if(choice == 0):
    video = driver.find_element_by_class_name('style-scope ytd-video-renderer').click()
    time.sleep(2)
    mute = driver.find_element_by_class_name('ytp-mute-button').click()
    '''
    embed = driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/paper-dialog[2]/yt-sharing-embed-renderer/div[2]/paper-dialog-scrollable/div/div[1]/paper-textarea/paper-input-container/div[2]/div/iron-autogrow-textarea/div[2]/textarea')
    print(embed.value)
    '''
    time.sleep(2)
    clear_console()

    print("Searched Title = ",search_title)
    print("Video Title = ", driver.title)
    print("Video Url = ", driver.current_url)

    channel = driver.find_element_by_class_name("ytd-video-owner-renderer").click()
    
    time.sleep(2)
    print("----")
    print("Channel Name = ", driver.title)
    print("Channel URL = ", driver.current_url)
else:
    driver.find_element_by_class_name('ytd-channel-name').click()
    time.sleep(2)
    clear_console()
    '''
    print("Searched Title = ",search_title)
    print("Channel Name = ", driver.title)
    print("Channel URL = ", driver.current_url)
    '''
    to_send = f'\n Search Title = {search_title} \n Channel Name = {driver.title} \n  Channel URL = {driver.current_url} \n '
    client.messages.create(
    to=my_phone,
    from_=phone_number,
    body= to_send
    )
    print(to_send)
    print(f'Message sent on {my_phone}!')
driver.quit()