import os
from flask import Flask, request, render_template
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask
from flask import send_file
import re
import wget

app = Flask(__name__)


@app.route('/download', methods=['POST'])
def download_files():
    # Get the input from the text field
    input_text = request.form['input_text']

    # Modify the code to use the input_text variable
    # connect to website and get list of all pdfs
    url = input_text
    try:
        response = urlopen(url).read()
    except:
        return urlopen(url).read() + 'Invalid URL! ' + url
    soup = BeautifulSoup(response, "html.parser")
    links = soup.find_all('a', href=re.compile(r'(.pdf)'))

    # clean the pdf link names
    url_list = []
    for el in links:
        if el['href'].startswith('http'):
            url_list.append(el['href'])
        else:
            url_list.append(input_text + el['href'])

    # download the pdfs to a specified location
    count = 0
    for url in url_list:
        if count < 2:
            try:
                new_url = url.replace(" ", "%20")
                print(new_url)
                wget.download(new_url, "webscraping")
                count += 1
            except:
                pass
        else:
            exit
    return 'Files downloaded!'


if __name__ == '__main__':
    app.run()


@app.route('/')
def home():
    return send_file('index.html')
