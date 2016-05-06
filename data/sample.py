import numpy

class Sample():

	def __init__(self, dataWindow, direction):
		self.sampleList = zip(*dataWindow)		# matrix transpose
		self.direction = direction

	def maxOfFourierTransform(self):
		maxFourier = []

		for i in range(len(self.sampleList)):
			sensorData = self.sampleList[i]
			fourier = numpy.fft.fft(sensorData)
			maxFourier.append(numpy.abs(fourier).max())

		return maxFourier

	def getDirection():
		return self.direction

	def printSensors(self):
		for i in range(len(self.sampleList)):
			print("_____________SENSOR" + str(i) + "_____________")
			for j in range(len(self.sampleList[i])):
				print self.sampleList[i][j]

