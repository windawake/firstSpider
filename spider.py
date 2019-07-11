import os
from bs4 import BeautifulSoup

class Spider():
    """
    开始抓取
    """
    def __init__(self,config,session):
        self.config = config
        self.session = session
        self.session_instance = session.instance
        
    """ 
    获取首页内容 
    """ 
    def getIndex(self):
        ##创建根目录
        self.createDir(self.config['base_path']) 
        content = self.session_instance.get(self.config['index_url'])
        if not content.text:
          print('糟糕，换代理吧')
          return False
        soup = BeautifulSoup(content.text,'html.parser')
        archives = soup.find('ul','archives').find_all('a')
        total  = "一共 {} 套图".format(len(archives))
        print(total)
       
        downList = []
        for index,archive in enumerate(archives):
          #href
          href = archive.get('href')
          #text
          text = archive.string
          ##下载图片
          if index > 10:
            break
          if href:
            downList.append((href,index,text))  
        return downList 

    """   
    获取内容页
    url 内容页地址
    index 第几套图
    dirname 套图名称（目录名称）
    """
    def getImgs(self,url,index,dirname):
      ##创建文件夹，定位到当前文件夹
      self.createDir(self.config['base_path']+dirname)
      ## get content
      try: 
          content = self.session_instance.get(url)
          soup = BeautifulSoup(content.text,'html.parser')
          ###总页数
          pageTotal = int(soup.find('div','pagenavi').find_all('a')[4].string)
          print(print("{}一共{}页".format(dirname,pageTotal))) 
          for page in range(1,pageTotal+1):
            ###图片
            subUrl = url+'/'+str(page)
            content = self.session_instance.get(subUrl)            
            soup = BeautifulSoup(content.text,'html.parser')
            src = soup.find('div','main-image').find('img').get('src')
            self.session.appendHeaders({'Referer':url})
            imgcontent = self.session_instance.get(src)

            array = src.split('/')
            file_name = array[len(array)-1]
            full_path = self.config['base_path']+dirname+"/"+file_name
            print(print("{}一共{}页 当前{} 保存路径{}".format(dirname,pageTotal,index,full_path))) 
            self.saveImg(full_path,imgcontent.content)
      except Exception as e:
            print(e)
    """ 
    创建目录
    path 目录
    """
    def createDir(self,path):
        if os.path.exists(path) is False:
            os.makedirs(path)

    """
    写入文件
    file 文件名
    content 图片
    """
    @staticmethod
    def saveImg(file,content):
      with open(file,'ab') as handler:
        handler.write(content)

  