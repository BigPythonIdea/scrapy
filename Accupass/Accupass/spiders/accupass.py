import scrapy
from scrapy_selenium import SeleniumRequest
import time

class AccupassSpider(scrapy.Spider):
    name = 'accupass'
    allowed_domains = ['accupass.com']
    start_urls = ['http://accupass.com/']

    def start_requests(self):
        yield SeleniumRequest(url='https://www.accupass.com/?area=north', 
        callback=self.parse)

    def parse(self, response):
        driver = response.request.meta['driver']
        time.sleep(5)
        for i in range(1,7):
            p = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div['+str(i)+']/div/div/div/div[2]/div[1]/div/a/p').text
            print(p)
        print("OK")
