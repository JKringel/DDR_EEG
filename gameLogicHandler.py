from threading import Thread
from Queue import Queue
import random
import time
class GameLogicHandler():

	def __init__(self, arrowQ, syncQ, controlQ):
		self.arrowFromGenQueue = Queue()
		self.arrowToViewQueue = arrowQ
		self.viewDoneQueue = syncQ
		self.controllerQueue = controlQ
		self.Genthread = Thread(target = self.generateArrows, args=(2, self.arrowFromGenQueue,))

	def threadInit(self):
		self.Genthread.start()
		while True:
			try:
			   	direction = self.arrowFromGenQueue.get()
			   	# print("Current direction:" + str(direction))
		   	   	self.arrowToViewQueue.put(direction)
		   	   	self.arrowFromGenQueue.task_done()
		   	   	while True:
		   	   		drawingDone = False
		   	   		# Check if the drawing is done
		   	   		try: 
		   	   			drawingDone = self.viewDoneQueue.get()
		   	   			# print("Drawing Finished")
		   	   			self.viewDoneQueue.task_done()
		   	   			break;
		   	   		except Queue.Empty:
		   	   			pass

		   	   		try:
		   	   			userIn = self.controllerQueue.get()
		   	   			print(userIn)
		   	   		except Queue.Empty:
		   	   			pass
			except Queue.Empty:
			   	pass

	def generateArrows(self, waitTime, q):
		while True:
			d = random.randint(0,3)
			q.put(d)
			time.sleep(waitTime)	