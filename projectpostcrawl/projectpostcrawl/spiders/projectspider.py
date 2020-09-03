import scrapy
import requests
url = ('http://192.168.217.132/freebix/')

r = requests.get(url)
p = r.status_code == requests.codes.ok

if p == True:
    print("Status_Ok")
    print(r.status_code)
else:
    print("Failed")

h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

xheaders = {'User-Agent': 'Mobile'}
xy = requests.get(headers=xheaders, url=(url))
print("Header:")
print("**********")
for h in xy.headers:
    print("\t ", h, ":", xy.headers[h])
print("**********")

class projectspider(scrapy.Spider):
    name = "crawlweb"

    start_urls = [
        'http://192.168.217.132/freebix/'
    ]

    def parse(self, response):
            filename = response.url.split("/")[-2] + '.json'
            with open(filename, 'wb') as f:
                f.write(response.body)
            # scrapy crawl crawlweb -o http.json

