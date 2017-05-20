import requests
from bs4 import BeautifulSoup
html = requests.get("http://140.118.160.184/jjcfarm/cluster/SUSE_Install.html")
soup = BeautifulSoup(html.text)

def findli():
    print soup.find_all('li')

