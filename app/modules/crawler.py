import requests
from bs4 import BeautifulSoup


class StringCrawler(object):

    def __init__(self, word, urls, **kwargs):
        self.urls = urls
        self.word = word

    def crawl_string(self):
        try:
            results = []

            for url in self.urls:

                markup = requests.get(url).text
                soup =  BeautifulSoup(markup, 'html.parser')

                query = soup.find_all('body')
                
                frequency = '{0}'.format(query).count(self.word)
                
                results.append({
                    'url': url,
                    'frequency': frequency
                })

            return results

        except requests.exceptions.ConnectionError:
            raise Exception('Unable to establish connection')


if __name__ == '__main__':
    print('Please run main.py')
