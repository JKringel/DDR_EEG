from threading import Thread
from gameView import DDRWindow
from Queue import Queue
from gameLogicHandler import GameLogicHandler
from controller import Controller

def main():
	arrowQueue = Queue()
	drawingDoneQueue = Queue()
	controllerQueue = Queue()

	gameLogic = GameLogicHandler(arrowQueue, drawingDoneQueue, controllerQueue)
	controller = Controller(controllerQueue)
	
	logicHandlerThread = Thread(target = gameLogic.threadInit)
	controllerThread = Thread(target = controller.readInput)

	win = DDRWindow("DDR", 500, 500)
	logicHandlerThread.start()
	controllerThread.start()
	win.startGame(2, arrowQueue, drawingDoneQueue)


if __name__ =="__main__": main()


	
