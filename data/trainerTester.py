import numpy
from sample import Sample
from classifier import Classifier

# Method:	parseFile
# Description:	
#	Converts a csv of EEG data into a list of samples
#	A sample is defined as a list of samplings collected by the EEG under one direction
# Arguments:
#	file:	The file path
# Returns:
#	samples:	A list of collected samples
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

	# increase the data window until the samples change direction
	# Then pass the window to a new Sample object
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
	print("Parsing the training data from \'" + fileDir +"\'")
	trainingSamples = parseFile(fileDir)
	fileDir = 'Test01.csv'
	print("Parsing the testing data from \'" + fileDir + "\'")
	testingSamples = parseFile(fileDir)

	c = Classifier()
	print("Extracting features from the training samples")
	c.extractTrainingFeatures(trainingSamples)
	print("Extracting features from the testing samples")
	c.extractTestingFeatures(testingSamples)

	# testing number of samples correctly predicted
	for i in range(1, 26) :
		print("Training the model using a kNeighborsClassifier with k = " + str(i))
		c.trainKNeighbors(i, 'distance')
		out = c.testData()
		percent = out[1] * 100
		print("Accuracy: " + "{0:.2f}".format(percent) + "%\n")



if __name__ =="__main__":
	main()

# separate into 128x14 arrays
# find max -  min for each columnns