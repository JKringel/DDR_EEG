from threading import Thread
import eeglistener

class Arrow(object):
	options = {	0 : u'\u2190'.encode("utf-8"),
			1 : u'\u2193'.encode("utf-8"),
			2 : u'\u2191'.encode("utf-8"),
			3 : u'\u2192'.encode("utf-8"),
			}
	def __init__(self, arrowType):
		print(Arrow.options[arrowType])
		#generate the listener
		thread = Thread(target = eeglistener.EEGListener().listen())
		thread.start()
		thread.join()
		#draw it

