
from sklearn import neighbors, datasets
import sample


# Class:	Classifier
# Description:	This class is used to classify EEG data.  Training methods:
# 			- kNeighborsClassifier
class Classifier():

	# Constructor
	# Description:	Initialize the instance variables
	# Instance Variables:
	#	- model:	The mathematical model built by the classifier
	def __init__(self):
		self.model = None

	# Method:	trainKNeighbors
	# Description:	
	def trainKNeighbors(self, dataSamples, n_neighbors, weights):
		split = self.splitData(dataSamples)
		data = split[0]
		target = split[1]

		# create an instance of Neighbours Classifier and fit the data.
		clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
		clf.fit(data, target)

		self.model = clf

	def testData(self, dataSamples):
		split = self.splitData(dataSamples)
		data = split[0]
		target = split[1]

		# predit the output
		prediction = self.model.predict(data)

		# calculate percent correct
		correct = 0
		for i in range(len(prediction)):
			if prediction[i] == target[i]:
				correct += 1

		percent = correct/len(prediction)
		print(str(correct) + " correct out of " + str(len(prediction)) + " samples.")

		return prediction

	def splitData(self, dataSamples):
		data = []
		target = []

		# get the data and the targets
		for i in range(len(dataSamples)):
			sample = dataSamples[i]
			data.append(sample.maxOfFourierTransform())
			target.append(sample.getDirection())

		return [data, target]


		
