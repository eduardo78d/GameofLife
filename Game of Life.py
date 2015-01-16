#!/usr/bin/env python. 
# -*- coding: utf-8 -*-
__author__ = "Eduardo Ismael García Pérez"

import threading 
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
		self.matrix  = matrix
		self.loop =0
		self.max_loop = 10
		threading.Thread.__init__(self)

	def showMatrix(self):
		print "\n"
		for listRow in self.matrix:
			print listRow

	def run(self):
		while  self.loop < self.max_loop:
			self.showMatrix()
			self.matrix = self.__round()
			time.sleep(1)
			self.loop+=1

	def __round(self):
		matrix = []
		for posX in range(0, len( self.matrix ) ):
			list_row =[]
			for posY in range(0, len( self.matrix[posX])):
				list_row.append(  self.__algorithm( self.__getListNeighbor(posX, posY).count(1), posX, posY ) )
			matrix.append(list_row)	
		return matrix


	def __algorithm(self, neighborsALive, posX, posY):
		if neighborsALive == 3 or (neighborsALive == 2 and self.matrix[posX][posY]):
			return 1
		return 0

	def __getListNeighbor(self, posX, posY):
		listNeighbor = []
		for posxNeighbor,posyNeighbor in self.neighborList:
			if self.__is_posValid( posX + posxNeighbor ,  posY + posyNeighbor , len(self.matrix), len( self.matrix[posX])):
				listNeighbor.append ( self.matrix[ posX + posxNeighbor ][ posY + posyNeighbor ] )
		return listNeighbor

	def __is_posValid(self, posX, posY , size_row, size_column):
		return posX in range( size_row ) and posY in range( size_column )


Game = GameOfLife( Matriz_Blinker )
Game.start()