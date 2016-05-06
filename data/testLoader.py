import numpy
from sample import Sample
from classifier import Classifier

SAMPLE_SIZE = 129

def absoluteMax(collection):
	maxCollection = []
	for i in range(len(collection)):
		maxCollection.append(max(collection[i]))

	return maxCollection

def absoluteMin(collection):
	minCollection = []
	for i in range(len(collection)):
		minCollection.append(min(collection[i]))

	return minCollection

def localMaxMin(sample):
	maxList = [[]]
	minList = [[]]

	

def max(sample):
	maxList = sample[0]

	for i in range(len(sample)):
		sampling = sample[i]
		for j in range(len(sampling)):
			if sampling[j] >  maxList[j]:
				maxList[j] = sampling[j]

	return maxList

def min(sample):
	minList = sample[0]

	for i in range(len(sample)):
		sampling = sample[i]
		for j in range(len(sampling)):
			if sampling[j] <  minList[j]:
				minList[j] = sampling[j]

	return minList

# Parses file into list of samples (currently 128 rows)
def parseFile(file):
	samples = []
	index = 1
	columnSelection = range(2,16)
	columnSelection.append(35)

	# Get the first window and remove samples before column 35 = 5, the init number
	dataSet = numpy.genfromtxt(file, delimiter=',', skip_header=index, usecols=columnSelection)
	for i in range(len(dataSet)):
		index += 1
		if dataSet[i, 14] == 5:
			break

	# Gets a 2D array of all data
	dataSet = numpy.genfromtxt(file, delimiter=',', skip_header=index, usecols=columnSelection)

	dataWindow = []
	for i in range(len(dataSet)):
		sampling = dataSet[i]
		dataWindow.append(sampling[0:14])
		direction = dataSet[i, 14]
		if direction != 0:
			samples.append(Sample(dataWindow, direction))
			dataWindow = []

	return samples

def printCollection(collection):
	for i in range(len(collection)):
		print collection[i]

def printSample(sample):
	for i in range(len(sample)):
		print sample[i]

def main():
	fileDir = 'test02-test02-04.05.16.21.03.39.csv'
	collection = parseFile(fileDir)

	c = Classifier(5, 'distance')

	#printCollection(collection)
	#printCollection(absoluteMin(collection))

if __name__ =="__main__":
	main()

# separate into 128x14 arrays
# find max -  min for each columnns