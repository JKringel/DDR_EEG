from sklearn import neighbors, datasets
import sample

# Class:	Classifier
# Description:	
#	This class is used to classify EEG data.  Training methods:
# 		- kNeighborsClassifier
class Classifier():

	# Constructor
	# Description:	
	#	Initialize the instance variables
	# Instance Variables:
	#	- model:	The mathematical model built by the classifier
	def __init__(self):
		self.model = None

	# Method:	trainKNeighbors
	# Description:	
	#	Trains the model using a kNeighborsClassifier algorithm
	# Arguments:
	#	dataSamples:	a list of EEG data points of type Sample
	#	n_neighbors:	the number of neighbors to look at when classifying a point
	#	weights:		the type of weighting system.  Either 'distance' or 'uniform'
	# Returns:
	#	model:	The trained model
	def trainKNeighbors(self, dataSamples, n_neighbors, weights):
		split = self.extractFeatures(dataSamples)
		data = split[0]
		target = split[1]

		clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
		clf.fit(data, target)

		self.model = clf
		return self.model

	# Method:	testData
	# Description:
	#	Classifies EEG data points by type of arrow, based on the model of this classifier
	# Arguments:
	#	dataSamples:	a list of EEG data points of type Sample
	# Retuns:
	#	prediction:		a list of integers that represent the predicted arrow of the data
	#					points in order.  1 - Up, 2 - Down, 3 - Left, 4 - Right
	#	percent:		the accuracy of the model
	def testData(self, dataSamples):
		split = self.extractFeatures(dataSamples)
		data = split[0]
		target = split[1]

		prediction = self.model.predict(data)

		# calculate percent correct
		correct = 0
		for i in range(len(prediction)):
			if prediction[i] == target[i]:
				correct += 1

		percent = float(correct)/len(prediction)
		print(str(correct) + " correct out of " + str(len(prediction)) + " samples.")

		return [prediction, percent]

	# Method:	extractFeatures
	# Description:
	#	Takes a list of data samples and extracts all of the features from the data and all of the targets.
	#	This should be used within this class only
	# Arguments:
	#	dataSamples:	a list of EEG data points of type Sample
	# Returns:
	#	[data, target]:	a list with the first element is data, which is a list of a list,
	#					and the second element is target, which is a list of directions
	def extractFeatures(self, dataSamples):
		data = []
		target = []

		# get the data and the targets
		for i in range(len(dataSamples)):
			sample = dataSamples[i]
			data.append(sample.maxOfFourierTransform())
			target.append(sample.getDirection())

		return [data, target]


		
