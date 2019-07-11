from  threading import Thread
"""
线程类
"""
class ThreadManger(Thread):
  def __init__(self,work_queue):
      Thread.__init__(self)
      self.work_queue = work_queue
      self.daemon = True

  def run(self):
      while True:
        target,args = self.work_queue.get()
        print(self.name+'开始下载')
        target(*args)
        print(self.name+'完成下载')
        self.work_queue.task_done()
