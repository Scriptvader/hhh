import urllib.request
from bs4 import BeautifulSoup
import requests

class string_crawler():
    url = []
    word = []

    def input_url(self):
        while True:
                try:
                    url_input = input('Enter Url: ')
                    urllib.request.Request(url_input)
                    self.url.append(url_input)
                    break
                except ValueError:
                    print ('Invalid url')

    def get_data(self):
        while True:
            try:
                url_no = int(input('How many web pages will you be searching: '))
                break
            except ValueError:
                print ('Please type in a digit')
        for i in range (url_no):
            self.input_url()    
        word_input = input('Enter word: ')
        self.word = word_input
        print('')

    def crawl_string(self):
        try:
            tot_freq = 0
            for url in self.url:
                markup = requests.get(url).text
                soup = BeautifulSoup(markup, 'html.parser')
                query = soup.find_all('body')	
                strng = str(query)
                freq = strng.count(self.word)
                tot_freq += freq
                print ('For '+url)
                print ('The word '+self.word+' appears '+str(freq)+' times.\n')
            print ('In total '+self.word+' appears '+str(tot_freq)+' times.')
        except requests.exceptions.ConnectionError:
            print ('You are not connected to the internet, Please check your connection and try again later.')

    def run_func(self):
        self.get_data()
        self.crawl_string()
        input('')



obj=string_crawler()
obj.run_func()
input('')



