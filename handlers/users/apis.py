import requests
from pprint import pprint

def currency_usd():
    url = "http://openlibrary.org/search.json?q=The+Harry+Potter"
    print(url)
    # url = "http://api.currencylayer.com/live?access_key=f6ea74d7d6ca5e77ce31d3ed0fe1b8e7&source=USD&currencies=UZS&format=1"
    result = requests.get(url).json()
    pprint(result)
    # f = open('test.txt','w')
    for i in result[0]:
        print(i)
    # f.write(f"{result}")
    return result

currency_usd()