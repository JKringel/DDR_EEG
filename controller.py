from Queue import Queue
import time
import random

class Controller():

	def __init__(self, q):
		self.directionQueue = q

	def readInput(self):
		while True:
			key = random.randint(0,3)
			self.directionQueue.put(key)
			time.sleep(1)