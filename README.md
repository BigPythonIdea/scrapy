# scrapy
This is scrapy project

# scrapy-selenium

![](https://i.imgur.com/7b6uxQ1.png)

0. 安裝&設定
```
pip install scrapy
```
```
scrapy startproject <YOUR PROJECT NAME>
```
```
scrapy genspider <YOUR PROJECT NAME> <website>
```
```
pip install scrapy-selenium
```
開啟settings.py檔案，加入scrapy-selenium Middleware的相關設定
```
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}
 
SELENIUM_DRIVER_NAME = 'chrome'  #瀏覽器名稱
SELENIUM_DRIVER_EXECUTABLE_PATH = 'chromedriver.exe'  #驅動程式路徑
SELENIUM_DRIVER_ARGUMENTS = ['-headless']
```


Microsoft Doc

```
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

```

* 執行
```
scrapy crawl inside
```
