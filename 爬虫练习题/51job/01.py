# -*- coding=utf-8 -*-
import requests
url = "https://we.51job.com/api/job/search-pc?api_key=51job&timestamp=1710728486&keyword=python&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb"

headers = {
    "Referer": "https://we.51job.com/pc/search?keyword=python&searchType=2&sortType=0&metro=",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "User-Token": "",
    "Uuid": "8367bee63f5f9f6eb6aeb206a88f6ee2"
}
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.text)