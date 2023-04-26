from urllib import request

import pdfplumber as pdfplumber
from bs4 import BeautifulSoup
import re
import os

# connect to website and get list of all pdfs
url="paste URL here"
response = request.urlopen(url).read()
soup= BeautifulSoup(response, "html.parser")     
links = soup.find_all('a', href=re.compile(r'(.pdf)'))


# clean the pdf link names
url_list = []
for el in links:
    if(el['href'].startswith('http')):
        url_list.append(el['href'])
    else:        url_list.append("paste URL here" + el['href'])



print(url_list)

# download the pdfs to a specified location
for url in url_list:
    try:
        print(url)
        fullfilename = os.path.join('D:\webscraping', url.replace("paste URL here", ""))
        print(fullfilename)
        request.urlretrieve(url, fullfilename)
    except:
        pass