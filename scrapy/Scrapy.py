import requests
import importlib
import sys
import re
from bs4 import BeautifulSoup

importlib.reload(sys)

def get_response(url):
    
    response = requests.get(url=url)
    return response.text

def output_file(param):
    target = open('E:\\response.html', 'a+', encoding='utf-8') 
    target.writelines(str(param))
    target.close

if __name__ == '__main__':
    url = 'https://segmentfault.com/hottest/weekly'
    soup = BeautifulSoup(get_response(url), 'html.parser')
    print('\n'.join([x.text for x in  soup.find_all('h4')]))
