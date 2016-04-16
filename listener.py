from threading import Lock
import time

class Listener(object):
	def __init__(self, direction):
		self.lock = Lock()
		self.direction = direction

	def listen(self):
		self.lock.acquire()
		print 'lock acquired by %d' % self.direction
		active = True
		try:
			time.sleep(1)
			print 'lock released by %d' % self.direction
			self.lock.release()
		except KeyboardInterrupt:
			print 'lock released by %d' % self.direction
			self.lock.release()