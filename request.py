"""
封装会话类
"""
import requests
class Session():
  instance = None
  """
  setting {headers:{},proxies:{}} 
  """
  def __init__(self,setting):
      if self.instance is None:
        session = requests.Session()
        session.keep_alive = False
        for key,value in setting.items():
          session.__setattr__(key,value) 
        self.instance = session

  def appendHeaders(self,setting):
        for s in setting:
           self.instance.headers[s] = setting.get(s)