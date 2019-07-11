import Config
from request import Session
import string
url ='http://icanhazip.com/'
session = Session(Config.config['session'])

content = session.instance.get(url)
proxy = False
text = content.text
for i,v in session.instance.proxies.items():
  v = v.split(':')[0]
  if v ==  text.strip() :
    proxy = True
    break

if proxy:
  print('代理成功，当前ip:{}'.format(text))
else:
  print('代理失败,当前ip:{}'.format(text))  