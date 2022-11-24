# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 22:14:44 2022

@author: Takodachi
"""

import nest_asyncio
nest_asyncio.apply()

import requests
import asyncio
import aiohttp
import time

from bs4 import BeautifulSoup
from aiohttp import ClientSession


async def main():
    links = list()
    for page in range(1, 50):
        links.append(f"https://www.104.com.tw/jobs/search/?ro=0&keyword=Data%20Scientist&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=15&asc=0&page={page}&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1")
        
    #打包任務
    async with ClientSession() as session:
        tasks = [asyncio.create_task(fetch(link, session)) for link in links]
        await asyncio.gather(*tasks)
        
async def fetch(link, session):
    async with session.get(link) as response:
        html_body = await response.text()
 
        soup = BeautifulSoup(html_body, "lxml")  # 解析HTML原始碼
 
        blocks = soup.find_all("div", {"class": "b-block__left"})  # 職缺區塊
        for block in blocks:
 
            job = block.find("a", {"class": "js-job-link"})  # 職缺名稱
            
            if job is None:
                continue
 
            company = block.find_all("li")[1]  # 公司名稱
            salary = block.find("span", {"class": "b-tag--default"})  # 待遇
 
            print(job.get_text())

            
            
start_time = time.time()  #開始執行時間
loop = asyncio.get_event_loop()  #建立事件迴圈(Event Loop)
loop.run_until_complete(main())  #執行協程(coroutine)
print("花費:" + str(time.time() - start_time) + "秒")
        
        