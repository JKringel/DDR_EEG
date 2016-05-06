
from sklearn import neighbors, datasets

class Classifier():

	def __init__(self, n, w):
		self.n_neighbors = n
		self.weights = w

	def trainData(self, dataSamples):
		data = []
		target = []

		# get the data nd the targets
		for i in len(dataSamples):
			sample = dataSamples[i]
			data.append(sample.maxOfFourierTransform())
			target.append(data.getDirection())

		# create an instance of Neighbours Classifier and fit the data.
    	clf = neighbors.KNeighborsClassifier(self.n_neighbors, weights=self.weights)
    	clf.fit(data, target)


		
