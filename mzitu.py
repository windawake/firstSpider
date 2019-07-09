import requests
from bs4 import BeautifulSoup
import os
##地址
url  = 'https://www.mzitu.com/all/'
##目录
base_path = '/Volumes/work/photos/'
##header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
##创建目录
def createDir(path):
 if os.path.exists(path) is False:
    os.makedirs(path)
 os.chdir(path)

"""
写入文件
file 文件名
content 图片
"""
def saveImg(file,content):
  with open(file,'ab') as handler:
    print(print("保存图片 {}".format(file)))
    handler.write(content)

"""
url 图片详情抓取
"""
def getImgs(url,cur_page,text=''):
  ##创建文件夹
   if text:
    createDir(base_path+text)
  ## get content
   content = requests.get(url,headers=headers)
   soup = BeautifulSoup(content.text,'html.parser')
   ###总页数
   pageTotal = int(soup.find('div','pagenavi').find_all('a')[4].string)
   print(print("一共{}页".format(pageTotal)))
   try:  
      for page in range(1,pageTotal+1):
        ###图片
        subUrl = url+'/'+str(page)
        content = requests.get(subUrl,headers=headers)
        soup = BeautifulSoup(content.text,'html.parser')
        src = soup.find('div','main-image').find('img').get('src')
        headers['Referer'] = url
        imgcontent = requests.get(src,headers=headers)
        array = src.split('/')
        file_name = array[len(array)-1]
        saveImg(file_name,imgcontent.content)
   except Exception as e:
        print(e)
"""
主函数
"""
def Main():
  createDir(base_path)
  content = requests.get(url,headers=headers)
  soup = BeautifulSoup(content.text,'html.parser')
  archives = soup.find('ul','archives').find_all('a')
  for archive in archives:
    #href
    href = archive.get('href')
    #text
    text = archive.string
    ##抓取图片
    ##下载图片
    if href:
      print("正在下载{}".format(text))
      getImgs(href,'',text = text)
if __name__ == "__main__":
  Main()