import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib import request

with open('/YourPath/YourPath_TheSequel/YourFile.txt', 'r') as f:
    for line in f:
        url = line.strip()
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find('title')
        #print(title) # Prints the tag
        print("*******************************************")
        print(title.string) # Prints the tag string content
        print(line)
        tables=pd.read_html(url)
        pd.set_option('display.max_colwidth', None)
        pd.set_option('display.max_columns', None)
        for i in range(0,4):
            #display(tables[i])
            try:
                display(tables[i])
            except IndexError:
                gotdata = 'null'
