HEAD = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.3'}

URL = 'https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=&ItemNamePattern=Crafting+Motif+80&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=0&PriceMax=30000'

TTC_URL = 'https://us.tamrieltradecentre.com/'

FIND_LINK = 'link="(.*\d+)'

FIND_ITEM_NAME = '[\s]{1,}(.*\w+)\s+</h4>'

FIND_PLACE = 'align-center">[\s]{1,}(.*\w+)\s+</div>'

FIND_GOLD = 'gold-amount">[\s]{1,}(.*\d+)\s+</td>'

FIND_TIME = 'elapsed="(\d+)"'