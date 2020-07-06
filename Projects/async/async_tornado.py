import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient

urls = [
    'https://pypi.org',
    'https://habr.com/en/',
    'https://www.bbc.com',
    'https://www.milwaukeetool.eu'
]

def headers(response):
    if response.error:
        #print(f'Ошибка: {response.error}')
        print(1)
    else:
        url = response.request.url
        data = response.body
        #print(f'URL: {url}, {len(data)}: {data}')
        print(2)

http = AsyncHTTPClient()

for url in urls:
    http.fetch(url, headers)

tornado.ioloop.IOLoop.instance().start()
