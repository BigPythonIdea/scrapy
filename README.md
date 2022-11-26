# scrapy
This is scrapy project

練習0.安裝 Scrapy

> 開發環境 vscode

環境 : 切換python 切換cmd
```
C:/Users/Takodachi/anaconda3/Scripts/activate   
```

> 開始建立環境

```
pip install scrapy
```

```
scrapy startproject 你的專案名稱 .
```

![](https://i.imgur.com/lR7eoXD.png)

scrapy genspider 網頁爬蟲檔案名稱 目標網站的網域名稱
```
scrapy genspider inside www.inside.com.tw
```

* name屬性：網頁爬蟲的名稱，在專案中必須是唯一的。
* allowed_domains屬性：目標網站的網域名稱清單。
* start_urls屬性：想要爬取的一至多個網頁網址清單。
* parse()方法：撰寫網頁爬蟲程式邏輯的地方，特別注意此方法名稱不得更改。

* 加上User-Agent(使用者代理)，如下範例：
```
USER_AGENT = '
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
```

* 執行
```
scrapy crawl inside
```
