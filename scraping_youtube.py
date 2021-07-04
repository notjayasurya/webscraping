from selenium import webdriver;
from selenium.webdriver.common.keys import Keys # Import the needed keys
from selenium.webdriver.support.ui import WebDriverWait 
import time
import pandas as pd


driver = webdriver.Chrome("C:\chromedriver.exe")

url = 'https://www.youtube.com/c/Dave2D/videos'
driver.get(url)

driver.find_element_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[2]').click()

# class="style-scope ytd-grid-video-renderer"

# //*[@id="meta"]/h3
# //*[@id="metadata-line"]/span[1]
# //*[@id="metadata-line"]/span[2]

videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
element = driver.find_element_by_tag_name('body');
video_list =[]

while True:
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)

    for video in videos:

        title = video.find_element_by_xpath('.//*[@id="video-title"]').text 
        views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
        months = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
        


    
    vid_items = {
        'title':title,
        'views':views,
        'posted_On':months
    }

    video_list.append(vid_items)
    df = pd.DataFrame(video_list)
    df.to_csv('youtube.csv')




