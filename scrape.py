import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
from gun_infocard import GunInfocard

session = requests.Session()
search_request = session.get(url='https://discoverygc.com/forums/showthread.php?tid=189916')
response = BeautifulSoup(search_request.text, 'lxml')

spoilers = response.select('.spoiler_wrap')
level = 4
f = open("gwg_inventory.csv", "w")
for spoiler in spoilers:
    inner_spoilers = spoiler.select('.spoiler_wrap')
    if(len(inner_spoilers) > 0):
        level += 1
    else:
        header = spoiler.select('a')[0].text.split(' - ')
        name = header[0]
        price = header[1]
        details = spoiler.select('.mycode_color')
        count = details[0].text
        hull = details[1].text
        shield = details[2].text
        range = details[3].text
        speed = details[4].text
        rate = details[5].text
        energy = details[6].text
        info = GunInfocard(level, name, price, count, hull, shield, range, speed, rate, energy)
        f.write(info.__str__()+'\n')
f.close()
