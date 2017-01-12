import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page =1
    while page <= max_pages:
        url = "https://thenewboston.com/forum/recent_activity.php?page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll("a", {'class': 'title text-semibold'}):
            href = link.get('href')
            title = link.string
            #print (href)
            #print (title)
            get_data(href)
        page+=1

def get_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('h1', {"class": "forum-title no-margin-b no-margin-t inline"}):
        print (item_name.string)

spider(3)


