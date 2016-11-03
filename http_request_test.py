import urllib3 as url
import certifi
import json


http = url.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

apiKey = '14dfc18e49814678975cffc6ec6b5f75'

res = http.request('GET', 'https://newsapi.org/v1/articles?source=t3n&sortBy=top&apiKey=' + apiKey)
data = json.loads(res.data.decode('utf-8'))
articles = data['articles']
print(len(articles))
