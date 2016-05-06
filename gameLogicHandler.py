from threading import Thread
from Queue import *
import random
import time
class GameLogicHandler():

	def __init__(self, arrowQ, syncQ, controlQ, scoreQ):
		self.arrowToViewQueue = arrowQ
		self.viewDoneQueue = syncQ
		self.controllerQueue = controlQ
		self.scoreToViewQueue = scoreQ

		# internal threading specific to arrow generation
		self.arrowFromGenQueue = Queue()
		self.Genthread = Thread(target = self.generateArrows, args=(2, self.arrowFromGenQueue,))

	def threadInit(self):
		self.Genthread.start()
		while True:
		   	direction = self.arrowFromGenQueue.get()
		   	print("Current Direction = " + str(direction))
	   	   	self.arrowToViewQueue.put(direction)
	   	   	self.arrowFromGenQueue.task_done()
	   	   	while True:
	   	   		if self.viewDoneQueue.empty():
	   	   			if not self.controllerQueue.empty():
	   	   				userIn = self.controllerQueue.get()
	   	   				print("EEG: " + str(userIn))
	   	   				if userIn == direction:
	   	   					print("Corrrect!: " + str(userIn))
	   	   					self.scoreToViewQueue.put(1)
	   	   		else:
	   	   			self.viewDoneQueue.get(block = False)
	   	   			print("Drawing Finished")
	   	   			self.viewDoneQueue.task_done()
	   	   			if not self.controllerQueue.empty():
	 					self.controllerQueue.queue.clear()
	   	   			break

	# This method runs in a separate thread to allow independent arrow generation
	# The thought here was to eventually generate arrows from a file to allow
	# for specific timings in relation to some song.
	# The current implementation generates a random arrow, then waits for some time
	def generateArrows(self, waitTime, q):
		while True:
			d = random.randint(0,3)
			q.put(d)
			time.sleep(waitTime)	