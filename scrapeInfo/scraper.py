from urllib.request import urlopen
from urllib.request import urlretrieve
from selenium import webdriver
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import urllib.request
from enum import Enum
import json
import os
from imageClassify import getAssociations

# Set API credentials from json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\sesch\\Desktop\\GitHub\\VTHACKS7\\scrapeInfo\\image-classification-json.json"


def socialMedias(Enum):
	facebook = 0
	instagram = 1
	twitter = 2

facebookText = []
twitterText = []
instagramImages = []
instagramText = []
allText = []

# list of tuples of predefined social media names and user handles populated by JSON file
# Ex: JSON file says facebook, instagram - then it would onl search those two accounts
websites = {'twitter':'SamSchoedel', 'facebook':'barackobama', 'instagram':'elonmusk'}
# social media possibilities:
# facebook
# instagram
# twitter

driver = webdriver.Chrome("C:\\Program Files (x86)\\webdrivers\\chromedriver.exe")

# webscrapers

# text classes in facebook: 
def searchFacebook(facebookHandle):
	searchURL = 'https://www.facebook.com/' + facebookHandle + '/posts/?ref=page_internal'
	try:  # make sure social media account is public
		content = urlopen(searchURL)
		soup = BeautifulSoup(content, features="html.parser")  # get content
		for textBox in soup.find_all('div', attrs={'class':'_3576'}):
			facebookText.append(textBox.find('p').text)
		print(f'facebook posts: {facebookText}')
	except:
		print("facebook page is not public :(")

def searchTwitter(twitterHandle):
	searchURL = 'https://www.twitter.com/' + twitterHandle # + '/posts/?ref=page_internal'
	try:  # make sure social media account is public
		content = urlopen(searchURL)
		soup = BeautifulSoup(content, features="html.parser")  # get content
		for textBox in soup.find_all('div', attrs={'class':'js-tweet-text-container'}):
			twitterText.append(textBox.find('p').text)
		print(f'tweets: {twitterText}')
	except:
		print("this twitter page is not public :(")

# This one gets pictures from instagram and turns them into text
# instead of finding image captions
def searchInstagram(instagramHandle):
	localImageLinks = []
	imageName = "instagram-image-"
	searchURL = 'https://www.instagram.com/' + instagramHandle
	driver.get(searchURL)
	content = driver.page_source
	soup = BeautifulSoup(content, features="html.parser")
	body = soup.find('body')
	for i,imageBox in enumerate(body.find_all('div', attrs={'class':'eLAPa'})):
		srcBox = imageBox.find('img')
		src = srcBox.get('src')
		instagramImages.append(src)
		# print(f'instagram images: {instagramImages}')
		imageName += str(i)
		try:
			# print(f'src: {str(src)}')
			# print(f'local link: {str(imageName) + ".jpg"}')
			urllib.request.urlretrieve(str(src), "instagramImages\\" + str(imageName) + ".jpg")
			localImageLinks.append('C:\\Users\\sesch\\Desktop\\GitHub\\VTHACKS7\\scrapeInfo\\instagramImages\\' + str(imageName) + ".jpg")
		except: 
			print("Instagram not allowing src retrieval for some reason or page not public")
		imageName = imageName.strip(str(i))
	print(localImageLinks)
	return localImageLinks

	# Wouldn't have to open a tab if this code worked
	# try:  # make sure social media account is public
	# 	content = urlopen('https://www.instagram.com/experienceutah/')
	# 	soup = BeautifulSoup(content, features="html.parser")  # get content
	# 	body = soup.find('body')
	# 	article = body.find('article', attrs={'class':'ySN3v'})
	# 	for imageBox in body.find_all('div', attrs={'class':'KL4Bh'}):
	# 		srcBox = imageBox.find('img')
	# 		print("hi")
	# 		instagramImages.append(srcBox.get('src'))
	# 	print(instagramImages)
	# except:
	# 	print("this instagram page is not public :(")

	# try:
	# 	soup = BeautifulSoup(self.driver.page_source, 'lxml')
	# 	all_images = soup.find_all('img', attrs = {'class': 'FFVAD'}) 

	# 	for img in all_images:
	# 	    if img not in image_list:
	# 	        image_list.append(img)

	# 	if self.no_of_posts > 12: # 12 posts loads up when we open the profile
	# 	    no_of_scrolls = round(self.no_of_posts/12) + 6 # extra scrolls if any error occurs while scrolling.

	# 	    # Loading all the posts
	# 	    print('Loading all the posts...')
	# 	    for __ in range(no_of_scrolls):
		        
	# 	        # Every time the page scrolls down we need to get the source code as it is dynamic
	# 	        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
	# 	        sleep(2) # introduce sleep time as per your internet connection as to give the time to posts to load
		        
	# 	        soup = BeautifulSoup(self.driver.page_source, 'lxml')
	# 	        all_images = soup.find_all('img') 

	# 	        for img in all_images:
	# 	            if img not in image_list:
	# 	                image_list.append(img)
	# except Exception:
	#     print('Some error occurred while scrolling down and trying to load all posts.')
	#     sys.exit()  
	# return image_list


# Driver code
if 'facebook' in websites:
	searchFacebook(websites['facebook'])
	print(facebookText)
if 'instagram' in websites:
	localImageLinks = searchInstagram(websites['instagram'])
	for link in localImageLinks:
		instagramText.append(getAssociations(link))
	print(instagramText)
if 'twitter' in websites:
	searchTwitter(websites['twitter'])
	print(twitterText)

allText = facebookText + instagramText + twitterText
print(allText)