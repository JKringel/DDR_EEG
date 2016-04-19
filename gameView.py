from graphics import *
import time
import random
from button import *

class DDRWindow(GraphWin):
	def __init__(self):
		GraphWin.__init__(self)
	def __init__(self, name, xdim, ydim):
		GraphWin.__init__(self, name, xdim, ydim)
		self.startGame(1)
		
	def startMenu(self):
		b = Button(self, Point(30, 25), 20, 10, 'Quit')

	def startGame(self, acceptanceInterval, q):
		self.time = acceptanceInterval
		middle = self.getWidth()/2
		yBuff = self.getHeight() - 50
		self.drawArrowOnce(middle - 75, yBuff, 0)
		self.drawArrowOnce(middle - 25, yBuff, 1)
		self.drawArrowOnce(middle + 25, yBuff, 2)
		self.drawArrowOnce(middle + 75, yBuff, 3)

		# Initialize score
		self.score = 0;
		self.scoreText = None
		self.updateScoreText()

		while True:
			direction = q.get()
			self.drawArrow(direction)

	def drawArrowOnce(self, x, y, dir):
		x1 = x
		y1 = y
		if dir == 0:
			x = x + 12
			x1 = x - 24
		elif dir == 1:
			y = y - 12
			y1 = y + 24
		elif dir == 2:
			y = y + 12
			y1 = y - 24
		elif dir == 3:
			x = x - 12
			x1 = x1 + 24
		l = Line(Point(x, y), Point(x1, y1))
		l.setArrow('last')
		l.draw(self)
		return l

	def drawArrow(self, dir):
		x = 0
		if dir == 0:
			x = self.getWidth()/2 - 75
		elif dir == 1:
			x = self.getWidth()/2 - 25
		elif dir == 2:
			x = self.getWidth()/2 + 25
		elif dir == 3:
			x = self.getWidth()/2 + 75

		y = self.getHeight() - 50
		yDiff = y/(33 * self.time)
		while (y > 0):
			l = self.drawArrowOnce(x, y, dir)
			time.sleep(0.03)
			self.delete(l.id)
			y = y - yDiff

	def updateScoreText(self):
		if self.scoreText is not None:
			self.delete(self.scoreText.id)
		self.scoreText = Text(Point(self.getWidth() - 50, 50), 'Score: '+str(self.score))
		self.scoreText.draw(self)

	def addPoints(self, points):
		self.score += points
		self.updateScoreText()