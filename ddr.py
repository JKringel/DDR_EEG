from threading import Thread
from gameView import DDRWindow
from Queue import Queue
from gameLogicHandler import GameLogicHandler
from controller import Controller
import os

def main():
	arrowQueue = Queue()
	drawingDoneQueue = Queue()
	controllerQueue = Queue()
	scoreQueue = Queue()

	# Generating model and controller instances
	gameLogic = GameLogicHandler(arrowQueue, drawingDoneQueue, controllerQueue, scoreQueue)
	controller = Controller(controllerQueue)
	
	# Generating threads for the model and controller
	logicHandlerThread = Thread(target = gameLogic.threadInit)
	controllerThread = Thread(target = controller.readInput)

	# Open a view in the main thread
	# Start model and controller in separate threads
	win = DDRWindow("DDR", 500, 500, arrowQueue, drawingDoneQueue, scoreQueue)
	logicHandlerThread.start()
	controllerThread.start()
	win.startGame(2)

	os._exit(0)

if __name__ =="__main__": main()


	
