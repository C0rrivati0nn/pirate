import sys
import os
import requests
from bs4 import BeautifulSoup

def get_soup(url):
	request = requests.get(url, headers=headers)
	content = request.content
	soup = BeautifulSoup(content, 'html.parser')
	return(soup)
	

search = 'black panther'

#Set search term
search_term = search.replace(' ', '+')
#set user agent string
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#Find a working bay mirror
mirror = (get_soup('http://proxybay.bz').find('a', class_='t1')['href'])
print(mirror)

# Search the working mirror, find the top result, get link to specific torrent
torrent = get_soup(mirror+'/search/{}/'.format(search_term)).find('a', class_='detLink')['href']
print(torrent)

#visit the result url and get the magnet link
#magnet = get_soup(mirror+torrent).find('div', class_='download').find('a')['href']
magnet = get_soup(mirror+torrent).find('a', class_='download')['href']
print(magnet)







