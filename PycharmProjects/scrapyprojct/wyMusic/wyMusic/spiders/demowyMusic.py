import scrapy

class DemoWxnucis(scrapy.Spider):
    name = 'wymusic'
    start_urls = [
        'https://music.163.com/'
    ]
    
    def parse(self, response):
        print(response)
