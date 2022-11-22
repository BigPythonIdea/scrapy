import scrapy



class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['movies.yahoo.com.tw']
    start_urls = ['https://movies.yahoo.com.tw/movie_intheaters.html']

    def parse(self, response):
        for i in range(1,13):
            name = response.xpath('//*[@id="content_l"]/div[2]/ul[2]/li['+str(i)+']/div[2]/div[1]/div[1]/a/text()').get()
            english_name = response.xpath('//*[@id="content_l"]/div[2]/ul[2]/li['+str(i)+']/div[2]/div[1]/div[1]/div/a/text()').get()
            level = response.xpath('//*[@id="content_l"]/div[2]/ul[2]/li['+str(i)+']/div[2]/div[1]/div[1]/dl/dt/div[2]/span/text()').get()
            print('{}({}) 期待度：{}'.format(name, english_name, level))


