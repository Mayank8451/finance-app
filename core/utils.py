import datetime as dt

class Timer():

    def __init__(self):
             self.start_dt = None

    def start(self):
           self.start_dt = dt.datetime.now()

    def stop(self):
           end_at = dt.datetime.now()
           print('Time taken: %s' % (end_at - self.start_dt))                