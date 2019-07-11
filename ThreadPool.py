from queue import Queue
from ThreadManger import ThreadManger

"""
线程池
"""
class ThreadPool():
  def __init__(self,thread_num):
      self.thread_num = thread_num
      self.q  = Queue()
      self._thread_start()

  def _thread_start(self):
      for _ in range(self.thread_num) :
          thread = ThreadManger(self.q)
          self.thread = thread
          self.thread.start()

  def add2queue(self,func,*args):
      self.q.put((func,*args))    