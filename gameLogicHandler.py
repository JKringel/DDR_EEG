from threading import Thread
from Queue import Queue
import random
import time
class GameLogicHandler():

	def __init__(self, q):
		self.arrowFromGenQueue = Queue()
		self.arrowToViewQueue = q
		self.Genthread = Thread(target = self.generateArrows, args=(2, self.arrowFromGenQueue,))

	def threadInit(self):
		print("thread inti")
		self.Genthread.start()
		while True:
			try:
			   	direction = self.arrowFromGenQueue.get()
		   	   	self.arrowToViewQueue.put(direction)
		   	   	self.arrowFromGenQueue.task_done()
		   	   	endtime = time.time() + 2
		   	   	while (time.time() < endtime):
		   	   		if True:
		   	   			print("In Loop")
		   	   			# add points
		   	   			break
			except Queue.Empty:
			   	pass

	def generateArrows(self, waitTime, q):
		print("generating arrows")
		while True:
			d = random.randint(0,3)
			q.put(d)
			time.sleep(waitTime)

	def readInput(self, q):
		while True:
			key = input(": ")
			q.put(key - 1)

		