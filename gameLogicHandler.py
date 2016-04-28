from threading import Thread
from Queue import *
import random
import time
class GameLogicHandler():

	def __init__(self, arrowQ, syncQ, controlQ, scoreQ):
		self.arrowFromGenQueue = Queue()
		self.arrowToViewQueue = arrowQ
		self.viewDoneQueue = syncQ
		self.controllerQueue = controlQ
		self.scoreToViewQueue = scoreQ
		self.Genthread = Thread(target = self.generateArrows, args=(2, self.arrowFromGenQueue,))

	def threadInit(self):
		self.Genthread.start()
		while True:
		   	direction = self.arrowFromGenQueue.get()
		   	print("Current direction:" + str(direction))
	   	   	self.arrowToViewQueue.put(direction)
	   	   	self.arrowFromGenQueue.task_done()
	   	   	while True:
	   	   		if self.viewDoneQueue.empty():
	   	   			if not self.controllerQueue.empty():
	   	   				userIn = self.controllerQueue.get()
	   	   				print("Dectected:" + str(userIn))
	   	   				if userIn == direction:
	   	   					print(str(userIn) + " = " + str(direction))
	   	   					self.scoreToViewQueue.put(1)
	   	   		else:
	   	   			self.viewDoneQueue.get(block = False)
	   	   			print("Drawing Finished")
	   	   			self.viewDoneQueue.task_done()
	   	   			if not self.controllerQueue.empty():
	 					self.controllerQueue.clear()
	   	   			break


	def generateArrows(self, waitTime, q):
		while True:
			d = random.randint(0,3)
			q.put(d)
			time.sleep(waitTime)	