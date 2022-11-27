import scrapy
from scrapy_selenium import SeleniumRequest
import time
import pandas as pd

class DocSpider(scrapy.Spider):
    name = 'doc'
    allowed_domains = ['learn.microsoft.com']
    start_urls = ['http://learn.microsoft.com/']

    def start_requests(self):
        yield SeleniumRequest(url='https://learn.microsoft.com/zh-tw/docs/', callback=self.parse)

    def parse(self, response):
        title = []
        driver = response.request.meta['driver']
        time.sleep(2)
        for item in range(1,99):
            element = driver.find_element_by_xpath(f"/html/body/div[2]/div/section/div/div/main/div[2]/section[2]/div/div/ul/li[{item}]/a").text
            title.append(element)
        t = pd.DataFrame(title)
        t.to_csv("microsoft_doc.csv", encoding = "utf_8_sig")

