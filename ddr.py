from threading import Thread, Lock
import random
import os
from arrow import Arrow
from listener import Listener

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

	while True:
		d = random.randint(0,3)
		arrow = Arrow(d, listener[d])
		thread = Thread(target = arrow.waitForInput())
		thread.start()
		#os.system('clear')

if __name__ =="__main__": main()
	
