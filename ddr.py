from threading import Thread
import random
import time
from gameView import DDRWindow
from Queue import Queue

def main():

	arrowGenQueue = Queue()
	inputQueue = Queue()
	win = DDRWindow("DDR", 500, 500)
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
		key = input(": ")
		q.put(key - 1)


if __name__ =="__main__": main()


	
