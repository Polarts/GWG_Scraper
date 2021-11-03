import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
from gun_infocard import GunInfocard

session = requests.Session()
search_request = session.get(url='https://discoverygc.com/forums/showthread.php?tid=189916')
response = BeautifulSoup(search_request.text, 'lxml')

spoilers = response.select('.spoiler_wrap')
f = open("gwg_inventory.csv", "w")
f.write('Category,Name,Price,Inventory Count,Hull Damage,Shield Damage,Range,Projectile Speed,Refire Rate,Energy Usage\n')
category = ''
for spoiler in spoilers:
    inner_spoilers = spoiler.select('.spoiler_wrap')
    if(len(inner_spoilers) > 0):
        category = spoiler.select('a')[0].text.replace(',', ' -')
    else:
        header = spoiler.select('a')[0].text.split(' - ')
        name = header[0]
        price = header[1].replace('.','')
        details = spoiler.select('.mycode_color')
        count = details[0].text
        hull = details[1].text
        shield = details[2].text.replace('m','')
        range = details[3].text
        speed = details[4].text
        rate = details[5].text
        energy = details[6].text
        info = GunInfocard(category, name, price, count, hull, shield, range, speed, rate, energy)
        f.write(info.__str__()+'\n')
f.close()
