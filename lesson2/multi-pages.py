#! python2
# coding=utf-8  
  
import requests  
from bs4 import BeautifulSoup  
  
# 获取html文档  
def get_html(url):  
    """get the content of the url"""  
    response = requests.get(url)  
    response.encoding = 'utf-8'
    #print response.text 
    return response.text  
      
# 获取笑话  
def get_certain_joke(html):  
    """get the joke of the html"""  
    soup = BeautifulSoup(html, 'lxml')  
    joke_content = soup.select('div.content')[0].get_text()  

    print joke_content
  
    return joke_content  
  
# url_joke = "https://www.qiushibaike.com"  
url_joke_pre = "https://www.qiushibaike.com/article/"
url_joke_index = 120380162
# 这里有个问题，糗事百科的index不是连续的，不能简单的for循环获取

# html = get_html(url_joke)  
# joke_content = get_certain_joke(html)  
# # print joke_content[0]

for x in range(0,10):
    tmp_url_joke_index = url_joke_index - x;
    html = get_html(url_joke_pre + bytes(tmp_url_joke_index))
    joke_content = get_certain_joke(html)
