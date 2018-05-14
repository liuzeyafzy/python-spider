#! python2
# coding=utf-8  
  
import requests  
import time
from bs4 import BeautifulSoup  
from selenium import webdriver

def COOKIES(url):
    driver=webdriver.Chrome()
    obj = {'needTickers': 1, 'symbol': 'huobibtcusdt', 'type': '15min', 'size': 1000}
    # driver.post(url, obj)
    driver.get('https://www.btc123.com/market?symbol=huobibtcusdt')
    time.sleep(10)
    p = driver.execute_script("return GLOBAL_VAR.KLineData")
    print p

    # cj= driver.get_cookies()
    # cookie=''
    # for c in cj:
    #     cookie += c['name'] +'='  +  c['value'] +';'
    # return cookie
    
    return driver;
    driver.quit()

# cookie = COOKIES()
  
# 获取html文档  
# def get_html(url):  
#     """get the content of the url"""  
#     r = requests.get('https://www.btc123.com/market?symbol=huobibtcusdt') 
#     cj = r.cookies;
#     print cj
#     # s = requests.utils.dict_from_cookiejar(cj)
#     # print s

#     # cj = requests.utils.add_dict_to_cookiejar(cj, {"__jsl_clearance": "1525919507.644|0|DAOv3e0vh8yyAX9TjZ4I92Z%2BF8g%3D"})
#     # cj = requests.utils.add_dict_to_cookiejar(cj, {"__jsluid": "0c69cdf56b8588a8b63b1382e4c08d46"})
#     # cj = requests.utils.add_dict_to_cookiejar(cj, {"chartSettings": "%7B%22ver%22%3A3%2C%22charts%22%3A%7B%22chartStyle%22%3A%22CandleStick%22%2C%22mIndic%22%3A%22MA%22%2C%22indics%22%3A%5B%22VOLUME%22%2C%22MACD%22%5D%2C%22indicsStatus%22%3A%22open%22%2C%22period%22%3A%2215m%22%2C%22period_weight%22%3A%7B%22line%22%3A7%2C%221min%22%3A6%2C%225min%22%3A5%2C%2215min%22%3A8%2C%2230min%22%3A4%2C%221hour%22%3A3%2C%221day%22%3A2%2C%221week%22%3A1%2C%223min%22%3A0%2C%222hour%22%3A0%2C%224hour%22%3A0%2C%226hour%22%3A0%2C%2212hour%22%3A0%2C%223day%22%3A0%7D%2C%22areaHeight%22%3A%5B%5D%2C%22market_from%22%3A%22huobibtcusdt%22%7D%2C%22indics%22%3A%7B%22MA%22%3A%5B7%2C30%2C0%2C0%2C0%2C0%5D%2C%22EMA%22%3A%5B7%2C30%2C0%2C0%2C0%2C0%5D%2C%22VOLUME%22%3A%5B5%2C10%5D%2C%22MACD%22%3A%5B12%2C26%2C9%5D%2C%22KDJ%22%3A%5B9%2C3%2C3%5D%2C%22StochRSI%22%3A%5B14%2C14%2C3%2C3%5D%2C%22RSI%22%3A%5B6%2C12%2C24%5D%2C%22DMI%22%3A%5B14%2C6%5D%2C%22OBV%22%3A%5B30%5D%2C%22BOLL%22%3A%5B20%5D%2C%22DMA%22%3A%5B10%2C50%2C10%5D%2C%22TRIX%22%3A%5B12%2C9%5D%2C%22BRAR%22%3A%5B26%5D%2C%22VR%22%3A%5B26%2C6%5D%2C%22EMV%22%3A%5B14%2C9%5D%2C%22WR%22%3A%5B10%2C6%5D%2C%22ROC%22%3A%5B12%2C6%5D%2C%22MTM%22%3A%5B12%2C6%5D%2C%22PSY%22%3A%5B12%2C6%5D%7D%2C%22theme%22%3A%22Dark%22%2C%22language%22%3A%22zh-cn%22%7D"})

#     # cookies = dict()
#     # obj = {'needTickers': 1, 'symbol': 'huobibtcusdt', 'type': '15min', 'size': 1000}
#     # response = requests.post(url, obj, cj)  
#     # response.encoding = 'utf-8'
#     # print response 
#     # return response.text  
      
# 获取笑话  
def get_certain_joke(html):  
    """get the joke of the html"""  
    soup = BeautifulSoup(html, 'lxml')  
    joke_content = soup.select('div.content')[0].get_text()  
  
    return joke_content  
  
ajax_data = "https://www.btc123.com/market/kline"  
# html = get_html(ajax_data)  
html = COOKIES(ajax_data)
print html
# joke_content = get_certain_joke(html)  
# print joke_content
