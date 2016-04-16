import time
class EEGListener(object):

	def listen(self):
		active = True
		try:
			time.sleep(2)
		except KeyboardInterrupt:
			pass