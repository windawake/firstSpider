config ={}
##爬取的网址
config['index_url'] = 'https://www.mzitu.com/all'#
##存图片的根目录
config['base_path'] = '/Volumes/work/photos/'

config['session'] = {
   ##代理
   'proxies':{'http':"39.137.107.98:8080"},#'http://39.137.107.98:8080','http://39.137.69.9:8080','http://39.137.69.8:8080','http://47.107.190.212:8118'
   ##http头
  'headers':{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
}
##线程数量
config['threatNum'] = 3