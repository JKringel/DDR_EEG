from threading import Thread
from gameView import DDRWindow
from Queue import Queue
from gameLogicHandler import GameLogicHandler

def main():
	arrowQueue = Queue()
	drawingDoneQueue = Queue()
	gameLogic = GameLogicHandler(arrowQueue, drawingDoneQueue)
	logicHandlerThread = Thread(target = gameLogic.threadInit)
	win = DDRWindow("DDR", 500, 500)
	logicHandlerThread.start()
	win.startGame(2, arrowQueue, drawingDoneQueue)


if __name__ =="__main__": main()


	
