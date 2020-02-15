from urllib.request import urlopen
from urllib.request import urlretrieve
from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
import xml.etree.ElementTree as ET
import urllib.request
from enum import Enum
import json
import re
from nltk.corpus import wordnet as guru

def socialMedias(Enum):
	facebook = 0
	instagram = 1
	twitter = 2

facebookText = []
twitterText = []
instagramImages = []
instagramText = []

# list of tuples of predefined social media names and user handles populated by JSON file
# Ex: JSON file says facebook, instagram - then it would onl search those two accounts
websites = {'twitter':'SamSchoedel', 'facebook':'SamSchoedel', 'instagram':'sschoedel'}
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
	imageName = "instagram-image-"
	searchURL = 'https://www.instagram.com/' + instagramHandle
	driver.get(searchURL)
	content = driver.page_source
	soup = BeautifulSoup(content, features="html.parser")
	body = soup.find('body')
	for i,imageBox in enumerate(body.find_all('div', attrs={'class':'KL4Bh'})):
		srcBox = imageBox.find('img')
		src = srcBox.get('src')
		instagramImages.append(src)
		imageName += str(i)
		urllib.request.urlretrieve(str(src), "instagramImages\\" + str(imageName) + ".jpg")
		imageName = imageName.strip(str(i))

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

# Driver code
if 'facebook' in websites:
	searchFacebook(websites['facebook'])
	print(facebookText)
if 'instagram' in websites:
	searchInstagram(websites['instagram'])
	print(instagramImages)
if 'twitter' in websites:
	searchTwitter(websites['twitter'])
	print(twitterText)
