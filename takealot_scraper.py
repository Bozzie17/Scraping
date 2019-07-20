import requests
from bs4 import BeautifulSoup



def __scraper__():
    url = 'https://www.takealot.com/4est-shades-wooden-polarized-sunglasses-brown-bamboo/PLID48111025'
    #headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/74.0.3729.169 Chrome/74.0.3729.169 Safari/537.36'}
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}
    page = requests.post(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    spans = soup.find("span", class_= "currency")
    idd = soup.find(id='shopfront-app')
    print(soup.prettify())


__scraper__()