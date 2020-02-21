import scrapy
import unittest
import requests

class MySpider(scrapy.Spider):
    name = "my_spider"
    # Use the Request library

    # Set the target webpage
    url = 'http://172.18.58.238/snow'
    r = requests.get(url)
    # This will get the full page
    print(r.text)

    # This will just get just the headers
    h = requests.head(url)
    print("Header:")
    print("**********")
    # To print line by line
    for x in h.headers:
        print("\t ", x, ":", h.headers[x])
    print("**********")

    # This will modify the headers user-agent
    headers = {
        'User-Agent': 'Iphone 8'
    }
    # Test it on an external site
    url2 = 'http://172.18.58.238/headers.php'
    rh = requests.get(url2, headers=headers)
    print(rh.text)

    start_urls = ['http://172.18.58.238/snow']
    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

class Test_MySpider(unittest.TestCase):
    name = "my_spider2"


def test_spider(self):
    MySpider()  # call MySpider Class


if __name__ == '__main__': unittest.main()
