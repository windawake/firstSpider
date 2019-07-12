import Config
from request import Session
from ThreadPool import ThreadPool
import string
def main():
      ##线程池
      pool  = ThreadPool(20)
      lists = ['31.137.107.98:8080','32.137.106.98:8080','33.137.105.98:8080','34.137.104.98:8080','35.137.103.98:8080','36.135.107.98:8080','37.137.107.98:8080','38.137.107.98:8080','39.137.107.98:8080','40.137.107.98:8080'] 

      for i in lists:
        pool.add2queue(sum,(i,))
      pool.q.join()

def sum(ip):
  url ='http://icanhazip.com/'
  ##会话
  session = Session(Config.config['session'])
  content = session.instance.get(url)
  text = content.text
  print('当前ip:{},访问ip:{}'.format(text,ip))


if __name__ == '__main__':
   main()