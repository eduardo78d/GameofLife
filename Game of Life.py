import threading #The Theread is Just for Display the Matrix
import time

Matriz_Blinker  = [	
	[0,0,0,0,0], 
	[0,0,0,0,0], 
	[0,1,1,1,0], 
	[0,0,0,0,0], 
	[0,0,0,0,0] ]

Matriz_Beacon = [
	[0,0,0,0,0,0],
	[0,1,1,0,0,0],
	[0,1,1,0,0,0],
	[0,0,0,1,1,0],
	[0,0,0,1,1,0],
	[0,0,0,0,0,0],
]

Matriz_Toad = [
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,1,1,1,0],
	[0,1,1,1,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
]

class GameOfLife(threading.Thread):

	def __init__(self, matrix):
		self.neighborList = [ (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1)]
		self.lifeGame = True
		self.matrix  = matrix
		threading.Thread.__init__(self)


	def showMatrix(self):
		print "\n"
		for listRow in self.matrix:
			print listRow

	def run(self):
		populationDead = 0
		max_lopp = 0

		while self.lifeGame and max_lopp < 10: # In casa that you have a infinite matrix
			matrixNewG = []	
			for posX in range(0, len(self.matrix)):
				listRowNewG = []
				for posY in range(0, len(self.matrix[posX])):
					
					numberOfL = self.getListNeighborL(posX, posY)
					
					if self.matrix[posX][posY]:
						if  numberOfL == 2 or numberOfL==3:
							listRowNewG.append(1)
						else:
							listRowNewG.append(0)
							populationDead+=1
					else:
						if  numberOfL == 3:
							listRowNewG.append(1)
						else:
							listRowNewG.append(0)
							populationDead+=1
				
				matrixNewG.append(listRowNewG)

			self.showMatrix()

			if populationDead == (len(self.matrix) * len(self.matrix[0]) ):
				self.lifeGame = False
			else:
				populationDead=0
				self.matrix = matrixNewG
			
			time.sleep(1) #No neccessary for the Algorithm
			max_lopp+=1 #No neccessary for the Algorithm
		
	def getListNeighborL(self, posX, posY):
		count = 0
		for valor in self.neighborList:
			try:
				if  posX + valor[0] >= 0 and posY + valor[1] >= 0:
					if self.matrix[ posX + valor[0] ][ posY + valor[1] ] == 1:
						count +=1
			except Exception, e:
				pass
		return count
		

Game = GameOfLife( Matriz_Beacon )
Game.start()