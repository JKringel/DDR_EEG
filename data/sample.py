import numpy
from scipy.signal import butter, lfilter

class Sample():

	def __init__(self, dataWindow, direction):
		self.sampleList = zip(*dataWindow)		# matrix transpose
		self.direction = direction

	def butter_bandpass(self, lowcut, highcut, fs, order=5):
	    nyq = 0.5 * fs
	    low = lowcut / nyq
	    high = highcut / nyq
	    b, a = butter(order, [low, high], btype='band')
	    return b, a


	def butter_bandpass_filter(self, data, lowcut, highcut, fs, order=5):
	    b, a = self.butter_bandpass(lowcut, highcut, fs, order=order)
	    y = lfilter(b, a, data)
	    return y

	def filterUsingBandpass(self):
		filteredSensors = []
		fs = 250
		lowcut = 8
		highcut = 30

		for i in range(len(self.sampleList)):
			sensorData = self.sampleList[i]
			filteredSensors.append(self.butter_bandpass_filter(sensorData, lowcut, highcut, fs, order=6))

		self.sampleList = filteredSensors

	def maxOfFourierTransform(self):
		maxFourier = []

		for i in range(len(self.sampleList)):
			sensorData = self.sampleList[i]
			fourier = numpy.fft.fft(sensorData)
			maxFourier.append(numpy.abs(fourier).max())

		return maxFourier

	def getDirection(self):
		return self.direction

	def printSensors(self):
		for i in range(len(self.sampleList)):
			print("____SENSOR " + str(i) + "____")
			for j in range(len(self.sampleList[i])):
				print self.sampleList[i][j]

