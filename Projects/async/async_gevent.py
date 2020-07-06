import gevent.monkey
from urllib.request import urlopen
gevent.monkey.patch_all()

urls = [
    'https://pypi.org',
    'https://habr.com/en/',
    'https://www.bbc.com',
    'https://www.milwaukeetool.eu'
]

def headers(url):
    print(f'Подключаюсь к {url}.')
    data = urlopen(url).read()
    print(f'{len(data)}: {data}')

working = [gevent.spawn(headers, url) for url in urls]

gevent.wait(working)
