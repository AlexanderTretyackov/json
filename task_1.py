import requests
import json
import re

patternRegExIp='((25[0-5]|2[0-4][0-9]|1\d{2}|\d{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1\d{2}|\d{1,2})'

urlWiki = 'https://en.wikipedia.org/w/rest.php/v1/page/Word/history'
#headersWiki = {'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://meta.wikimedia.org/wiki/User:APaskulin_(WMF))'}

responseWiki = requests.get(urlWiki)
responseWikiJson = json.loads(responseWiki.text)

#словарь: ключ-название страны, значение-количество пользователей
countryStatisticDict = {}

for revision in responseWikiJson['revisions']:
    if(re.match(patternRegExIp, revision['user']['name']) != None):
        reviserIp=revision['user']['name']
        print(reviserIp)
        ipStackUrl='http://api.ipstack.com/{0}?access_key=536a0b25ceaa698fd398d2203749e0ed'.format(reviserIp)
        responseIpStack = requests.get(ipStackUrl)
        responseIpStackJson = json.loads(responseIpStack.text)
        countryName=responseIpStackJson['country_name']
        if countryStatisticDict.get(countryName) is None:
            countryStatisticDict[countryName] = 1
        else:
            countryStatisticDict[countryName] += 1

#сортируем элементы словаря по значению
list = list(countryStatisticDict.items())
list.sort(key=lambda i: i[1], reverse=True)

#выводим отсортированные элементы словаря
print('Страна', 'Число пользователей')
for i in list:
    print('{0} {1}'.format(i[0], i[1]))


