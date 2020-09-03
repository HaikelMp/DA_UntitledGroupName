import requests
url = ('http://192.168.217.132/freebix/')

x = requests.get(url)
xheaders = {'Title': 'Mobile'}
xy = requests.get(headers=xheaders, url=(url))

p = x.status_code == requests.codes.ok
if p == True:
    print("Status_Ok")
    print(x.status_code)
else:
    print("Failed")
