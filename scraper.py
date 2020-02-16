from urllib.request import urlopen
from urllib.request import urlretrieve
from selenium import webdriver
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import urllib.request
from enum import Enum
import json
import os
import re
from imageClassify import getAssociations

# Driver function at bottom

# Set API credentials from json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\sesch\\Desktop\\GitHub\\VTHACKS7\\scrapeInfo\\image-classification-json.json"


driver = webdriver.Chrome("C:\\Program Files (x86)\\webdrivers\\chromedriver.exe")

facebookText = []
twitterText = []

# webscrapers
# text classes in facebook: 
def searchFacebook(facebookHandle):
	searchURL = 'https://www.facebook.com/' + facebookHandle + '/posts/?ref=page_internal'
	try:  # make sure social media account is public
		content = urlopen(searchURL)
		soup = BeautifulSoup(content, features="html.parser")  # get content
		for textBox in soup.find_all('div', attrs={'class':'_3576'}):
			facebookText.append(textBox.find('p').text)
		# print(f'facebook posts: {facebookText}')
	except:
		print("facebook page is not public :(")

def searchTwitter(twitterHandle):
	searchURL = 'https://www.twitter.com/' + twitterHandle # + '/posts/?ref=page_internal'
	try:  # make sure social media account is public
		content = urlopen(searchURL)
		soup = BeautifulSoup(content, features="html.parser")  # get content
		for textBox in soup.find_all('div', attrs={'class':'js-tweet-text-container'}):
			twitterText.append(textBox.find('p').text)
		# print(f'tweets: {twitterText}')
	except:
		print("this twitter page is not public :(")

# This one gets pictures from instagram and turns them into text
# instead of finding image captions
def searchInstagram(instagramHandle):
	localImageLinks = []
	instagramImages = []
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
	# print(localImageLinks)
	return localImageLinks

# Driver function
def getSocialMediaText(websites):

	instagramText = []
	allText = []

	# Search each website
	if websites['facebook'] != "":
		searchFacebook(websites['facebook'])
		# print(facebookText)
		print('Facebook scraped')
	if websites['instagram'] != "":
		localImageLinks = searchInstagram(websites['instagram'])
		for link in localImageLinks:
			instagramText += getAssociations(link)
		# print(instagramText)
		print('Instagram scraped')
	if websites['twitter'] != "":
		searchTwitter(websites['twitter'])
		# print(twitterText)
		print('Twitter scraped')

	# Clean up discovered text
	allText = facebookText + instagramText + twitterText
	allText = " ".join(allText)
	allTextNoPunc = re.sub('[^A-Za-z0-9]+', ' ', allText)
	print(allTextNoPunc)

	return allTextNoPunc

# dict of predefined social media names and user handles populated by JSON file
# Ex: JSON file says facebook, instagram - then it would onl search those two accounts

# json displays "" for key if user doesn't enter handle for value

if __name__ == '__main__':
    pass