from Queue import Queue
import time
import random

# Controller class that runs within a separate thread
# Here is where we would hook up the EEG and run
# logic that classifies the input and sends it to the model.
# The current implementation guesses a random direction twice
# during the draw time for demonstration purposes.
class Controller():

	def __init__(self, q):
		self.directionQueue = q

	def readInput(self):
		while True:
			key = random.randint(0,3)
			self.directionQueue.put(key)
			time.sleep(1)