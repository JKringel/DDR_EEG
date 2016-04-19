from threading import Thread
import random
import time
from gameView import DDRWindow
from Queue import Queue

def main():

	arrowGenQueue = Queue()
	win = DDRWindow("DDR", 500, 500)
	thread = Thread(target = generateArrows, args=(2, arrowGenQueue,))
	thread.start()
	win.startGame(2, arrowGenQueue)


def generateArrows(waitTime, q):

	while True:
		d = random.randint(0,3)
		q.put(d)
		time.sleep(waitTime)		

if __name__ =="__main__": main()


	
