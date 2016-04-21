from threading import Thread
import random
import time
from gameView import DDRWindow
from Queue import Queue
from gameLogicHandler import GameLogicHandler

def main():
	arrowQueue = Queue()
	gameLogic = GameLogicHandler(arrowQueue)
	logicHandlerThread = Thread(target = gameLogic.threadInit)
	win = DDRWindow("DDR", 500, 500)
<<<<<<< HEAD
	Genthread = Thread(target = generateArrows, args=(2, arrowGenQueue,))
	inputThread = Thread(target = readInput, args=(inputQueue,))
	Genthread.start()
	inputThread.start()
	win.startGame(2, arrowGenQueue)


def generateArrows(waitTime, q):
	while True:
		d = random.randint(0,3)
		q.put(d)
		time.sleep(waitTime)

def readInput(q):
	while True:
		# key = input(": ")
		q.put(key - 1)
=======
	win.startGame(2, arrowQueue)
>>>>>>> 756d15c012a64ae5d4c9c6132a60173f0c03c3e7


if __name__ =="__main__": main()


	
