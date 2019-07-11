import Config
from ThreadPool import ThreadPool
from spider import Spider
from request import Session
import requests


def main():
  config = Config.config
  ##线程池
  pool  = ThreadPool(config['threatNum'])
  ##会话
  session = Session(config['session'])
  ##爬虫开始
  spider = Spider(config,session)
  ##获取首页索引页 进队列 多线程并发下载
  lists = spider.getIndex()  
  if  lists:
    for li in lists:
      pool.add2queue(spider.getImgs,li)

    for _ in  range(config['threatNum']):
      pool.thread.join()  

    pool.q.join()  
  else:
      print('抓取异常，没有数据')

if __name__ == "__main__":
  main()
  