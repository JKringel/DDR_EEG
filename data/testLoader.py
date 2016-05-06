import numpy
from sample import Sample
from classifier import Classifier

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

def main():
	fileDir = 'trainingData.csv'
	trainingSamples = parseFile(fileDir)
	fileDir = 'Test01.csv'
	testingSamples = parseFile(fileDir)

	accuracy = []
	c = Classifier()
	c.extractTrainingFeatures(trainingSamples)
	c.extractTestingFeatures(testingSamples)

	for i in range(1, 26) :
		c.trainKNeighbors(i, 'distance')
		out = c.testData()
		accuracy.append(out[1])

	print(accuracy)



if __name__ =="__main__":
	main()

# separate into 128x14 arrays
# find max -  min for each columnns