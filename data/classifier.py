
from sklearn import neighbors, datasets
import sample

class Classifier():

	def __init__(self, n, w):
		self.n_neighbors = n
		self.weights = w
		self.model = None

	def trainData(self, dataSamples):
		split = self.splitData(dataSamples)
		data = split[0]
		target = split[1]

		# create an instance of Neighbours Classifier and fit the data.
		clf = neighbors.KNeighborsClassifier(self.n_neighbors, weights=self.weights)
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


		
