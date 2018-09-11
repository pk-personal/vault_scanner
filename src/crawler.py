"""This is module is responsible for the crawler, that crawls out every available link"""

import re
from urllib.parse import *
import requests

class Crawl(object):

    def __init__(self, url):
        self.url = url
        self.target_links = []
        self.session = requests.Session()
        # TO DO : self.session = requests.Session()

    def extract_links_from(self):
        response = self.session.get(self.url)
        return re.findall('(?:href=")(.*?)"',response.text)

    def crawl(self,url=None):
        if url == None:
            url = self.url
        href_links = self.extract_links_from()

        for link in href_links:
            link = urljoin(url, link)

            if '#' in link:
            	print(link)
            	link = link.split('#')[0]

            if self.url in link and link not in self.target_links:
            	if '.css' not in link and '.ico' not in link:
            		self.target_links.append(link)
            		print('[+] ',link)
            		self.crawl(link)

    def getList(self):
        self.extract_links_from()
        self.crawl()
        return self.target_links
