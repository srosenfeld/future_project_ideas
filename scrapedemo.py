#https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

soup = BeautifulSoup(page.text, 'html.parser')

#remove links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()


#find links in a class
artist_name_list = soup.find(class_='BodyText')

artist_name_list_items = artist_name_list.find_all('a')

#open csv file to write to
f = open('z-artist-names.csv',"w")
f.write('Last Name, First Name, Link\n')


for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')
    print(names)
    print(links)
    f.write(names + ',' + links + '\n')

f.close()
