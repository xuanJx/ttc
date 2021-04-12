import requests
from bs4 import BeautifulSoup
import re
HEAD = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.3'}

URL_MOTIF = 'https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=&ItemNamePattern=Crafting+Motif+%s&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=%s&PriceMax=%s'

URL_NOT_MOTIF = 'https://us.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=&ItemNamePattern=%s&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=%s&PriceMax=%s'


TTC_URL = 'https://us.tamrieltradecentre.com/'

FIND_LINK = 'link="(.*\d+)'

FIND_ITEM_NAME = '[\s]{1,}(.*\w+)\s+</h4>'

FIND_PLACE = 'align-center">[\s]{1,}(.*\w+)\s+</div>'

FIND_GOLD = 'gold-amount">[\s]{1,}(.*\d+)\s+</td>'

FIND_TIME = 'elapsed="(\d+)"'



class Ttc_Price():
    def __init__(self, num, minprice, hightprice, motif = True):
        if motif:
            self.response = requests.get(url=URL_MOTIF % (num, minprice, hightprice), headers=HEAD)
        else:
            self.response = requests.get(url=URL_NOT_MOTIF % (num, minprice, hightprice), headers=HEAD)
        self.res = self.response.text
    # def Main(self):
    #     ...

    def Old_Soup(self):
        soup_list = []
        soup = BeautifulSoup(self.res, 'html.parser')
        for item in soup.find_all('tr', class_="cursor-pointer"):
            soup_list.append(re.findall(FIND_LINK, str(item)))
        return soup_list

    def New_url(self):
        url = self.Old_Soup()
        new_url = []
        for u in url:
            new_url.append(TTC_URL + u[0])

        return new_url

    def New_Soup(self):
        url_list = self.New_url()
        new_list = []
        time_list = []
        for url in url_list:
            response = requests.get(url, headers=HEAD)
            res = response.text
            soup = BeautifulSoup(res, 'html.parser')
            for item in soup.find_all('div', class_="panel-title"):
                time_list.append(re.findall(FIND_TIME, str(item)))
            for item in soup.find_all('div', class_="glass-panel"):
                 new_list.append(self.Url_Format(item))
        for x, y in zip(time_list, new_list):
            y.insert(0, x[0])
        return new_list

    def Url_Format(self, item):
        item_name = re.findall(FIND_ITEM_NAME, str(item))[0]
        try:
            item_place = re.findall(FIND_PLACE, str(item))[0]
        except Exception as e:
            item_place = ' '
        single_price = re.findall(FIND_GOLD, str(item))[0]
        total_price = re.findall(FIND_GOLD, str(item))[1]
        return [item_name, item_place, single_price, total_price]
