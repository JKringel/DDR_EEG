from threading import Thread

class Arrow(object):
	directions = {
			0 : u'\u2190'.encode("utf-8"), 			#left
			1 : u'\u2193'.encode("utf-8"),			#down
			2 : u'\u2191'.encode("utf-8"),			#up
			3 : u'\u2192'.encode("utf-8"),			#right
			}
			
	def __init__(self, arrowType, listener):
		self.listener = listener
		print(Arrow.directions[arrowType])
		#generate the listener
		#draw it

	def waitForInput(self):
		self.listener.listen()
