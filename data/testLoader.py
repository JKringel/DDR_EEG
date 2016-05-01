import numpy

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
	sampleList = []
	rowWindow = SAMPLE_SIZE
	index = 1

	# Get the first window and remove samples before time = 0
	sample = numpy.genfromtxt(file, delimiter=',', skip_header=index, max_rows=rowWindow, usecols=range(2,16))
	for i in range(len(sample)):
		if sample[i, 0] == 0.0:
			break
		else:
			index += 1

	# Add each window of values to the list
	while True:
		try:
			sample = numpy.genfromtxt(file, delimiter=',', skip_header=index, max_rows=rowWindow, usecols=range(2,16))
			if len(sample) == rowWindow:
				sampleList.append(sample)
			index += rowWindow
		except StopIteration:
			break

	return sampleList

def printCollection(collection):
	for i in range(len(collection)):
		print collection[i]

def printSample(sample):
	for i in range(len(sample)):
		print sample[i]

def main():
	fileDir = '01-01-15.04.16.18.06.35.csv'
	collection = parseFile(fileDir)
	printCollection(absoluteMax(collection))
	#printCollection(absoluteMin(collection))

if __name__ =="__main__":
	main()

# separate into 128x14 arrays
# find max -  min for each columnns