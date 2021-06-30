from enum import Enum

"""
-represent game as a 2D array
-each row and column coincides
[[EMPTY,EMPTY,EMPTY],
 [EMPTY,EMPTY,EMPTY],
 [EMPTY,EMPTY,EMPTY]
]
-seperate game and drawing class
input handled by tkinter which is passed to the game to draw

"""


class gridState(Enum):
	EMPTY = 0
	NAUGHT = 1
	CROSS = 2



class mainGame:
	gameGrid = []
	def __init__(self,player1,player2):
	self.player1 = player1
	self.player2 = player2
	generateGameGrid()

	def generateGameGrid(self):
		for i in range(3):
			self.gameGrid.append([gridState.EMPTY]*3)
		




class drawingClass:



