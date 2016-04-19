from threading import Thread, Lock
import random
import os
import time
from arrow import Arrow
from listener import Listener
from gameView import DDRWindow
from Queue import Queue

def main():
	leftListener = Listener(0)
	downListener = Listener(1)
	upListener = Listener(2)
	rightListener = Listener(3)

	listener = {
		0 : leftListener,
		1 : downListener,
		2 : upListener,
		3 : rightListener,
		}

	arrowGenQueue = Queue()
	win = DDRWindow("DDR", 500, 500)
	view = Thread(target = win.startGame, args=(2, arrowGenQueue,))
	view.start()

	while True:
		d = random.randint(0,3)
		print(d)
		arrowGenQueue.put(d)
		time.sleep(5)
		#arrow = Arrow(d, listener[d])
		# win.drawArrow(d)
		# thread = Thread(target = arrow.waitForInput())
		# thread.start()
		#os.system('clear')

if __name__ =="__main__": main()


	
