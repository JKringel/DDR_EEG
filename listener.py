from threading import Lock
import time

class Listener(object):
	def __init__(self, direction):
		self.lock = Lock()
		self.direction = direction

	def listen(self):
		self.lock.acquire()
		active = True
		try:
			time.sleep(2)
		except KeyboardInterrupt:
			self.lock.release()