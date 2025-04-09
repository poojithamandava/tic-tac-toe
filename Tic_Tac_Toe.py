#TIC-TAC-TOE
#PIRATES OF PYTHON
#Prerequisite: The user must have installed the pygame module to run the following code.

#importing the required libraries
import pygame
import sys
pygame.init()							#initiating pygame module

length= 900							#giving values of length and breadth of the required 
breadth=900

screen = pygame.display.set_mode( (length,breadth) )		#creating the required interface 
pygame.display.set_caption("TIC TAC TOE")

#------------------------------------------------------FUNCTIONS-----------------------------------------------------------------------------------------------------#

def board():
	'''
	defining a function to print the empty game board in the interface
	'''
	screen.fill((25,150,120))				#filling the screen with required color

	pygame.draw.line(screen,(0,0,0), (300,0), (300,900), 10)	#drawing the lines accodingly to create a game board
	pygame.draw.line(screen,(0,0,0), (600,0), (600,900), 10)	#surface,color,start pos,end pos, width of the line
	pygame.draw.line(screen,(0,0,0), (0,300), (900,300), 10)
	pygame.draw.line(screen,(0,0,0), (0,600), (900,600), 10)



Board=[[0,0,0],[0,0,0],[0,0,0]]          #using this board as the replica or reference to the actual game board


def mark_box(i,j,player):
	'''
	we defined a function mark_box to mark a box in those 9 boxes
	accordingly by considering it's position by it's row and column.
	Here, i,j implies row and column of the box(position).It marks the box as 1 
	for player 1 and as 2 for player-2.
	'''
	Board[i][j]= player


def check_box_avail(i,j):
	'''
	defining a function to check whether a box is empty or not.
	'''
	if (Board[i][j]==0):
		return 1
	return 0


def check_board_full():
	'''
	defining a function to check whether the board is full or not.
 	'''
	for i in range(3):
		for j in range(3):
			if (Board[i][j]==0):
				return 0						#checks every box of the board and returns 1 everyone of them are marked.
	return 1

def check_win(player):
	'''
	This function checks whether the player won the game or not, if won draws a line striking all the 3 matched boxes and returns 1, else 0.
	'''
	#checking for horizontal win 
	if (Board[0][0]==player and Board[1][0]==player and Board[2][0]==player):	#1st row 
		return 1
	if (Board[0][1]==player and Board[1][1]==player and Board[2][1]==player):	#2nd row 
		return 1	
	if (Board[0][2]==player and Board[1][2]==player and Board[2][2]==player):	#3rd row 
		return 1


	#checking vertical win
	if (Board[0][0]==player) and (Board[0][1]==player) and (Board[0][2]==player):	#1st column
		return 1			
	if (Board[1][0]==player) and (Board[1][1]==player) and (Board[1][2]==player):	#2nd column
		return 1
	if (Board[2][0]==player) and (Board[2][1]==player) and (Board[2][2]==player):	#3rd column
		return 1

	
	#check for diagonal win
	if Board[0][0]==player and Board[1][1]==player and Board[2][2]==player :	#descending diagonal from left

		return 1
	if Board[0][2]==player and Board[1][1]==player and Board[2][0]==player:		#ascending diagonal from left

		return 1	

	
def draw_OX():
	'''
	defined a function to draw 'O' in the boxes which are marked as 1 and 
	to draw 'X' in the boxes which are marked as 2.
	'''
	for i in range(3):
		for j in range(3):
			if Board[i][j] ==1:					#drawing circle in the boxes which are marked as 1.	
				pygame.draw.circle(screen, (5,10,5) , (int(i*300)+150,int(j*300)+150), 100 ,30)		#surface, color, centre pos, radius of circle, width of the circle
			if (Board[i][j]==2): 					#drawing two lines in a way to create a 'X' in the boxes marked as 2.
				pygame.draw.line(screen, (210,230,255) , (i*300+50,j*300+50),(i*300+250,j*300+250) , 50) 						#surface, color, start_pos,end_pos,width of the desired line
				pygame.draw.line(screen, (210,230,255) , (i*300+250,j*300+50),(i*300+50,j*300+250) ,50)



def end_screen(player):
	'''
	defining the function to show who won the game, once the game ends.
	'''
	pygame.draw.line(screen,(0,0,0),(0,450),(900,450),900)			#drawing a line to fill the screen

	font= pygame.font.Font(None,100)					#selecting the required font
	f=pygame.font.Font(None,60)						
	p1_won= font.render('"Player -1 won the Match"',True,(255,255,255))	#Command  to display when player 1 won
	p2_won= font.render('"Player -2 won the Match"',True,(255,255,255))	#same for the player 2
	r=f.render('Press any \'key\' to restart the game',True,(255,255,255))	#common statement for a general instruction

	if(player==1):								#if player-1 won the game
		screen.blit(p1_won, (30,350))					#blitting the statement on the screen
		screen.blit(r, (100,800))					#blitting the common instruction on screen
		pygame.display.update()						#updating the screen
	
	if(player==2):								#repeating the same if player-2 wins the game 
		screen.blit(p2_won, (30,350))
		screen.blit(r, (100,800))	
		pygame.display.update()
						
def end_draw():
	'''
	defining a function to create end screen when no player won the game('draw')
	'''
	pygame.draw.line(screen,(0,0,0),(0,450),(900,450),900)			#repeating the same stuff that we have done for the above function when the game got drawn.

	font= pygame.font.Font(None,100)
	f=pygame.font.Font(None,60)
	draw= font.render('"DRAW"',True,(255,255,255))
	r=f.render('Press any \'key\' to restart the game',True,(255,255,255))

	screen.blit(draw, (325,350))				
	screen.blit(r, (100,800))
	pygame.display.update()






#----------------------------------------------------------#MAIN LOOP #--------------------------------------------------------------------------------------------------#


board()								#prints the empty board

GAME_OVER= 0							#setting Game_over=0
player=1							#setting the default player =1


while True :							#To create an infinte loop for the game

	for event in pygame.event.get():                      
		if (event.type == pygame.QUIT):			#exiting the game when the game is closed by tapping 'X'
			sys.exit()
		if (event.type == pygame.MOUSEBUTTONDOWN) and (GAME_OVER==0):      
			X = event.pos[0]			#To store the X-coordinate of the position of the mouse pointer.
			Y = event.pos[1]			#To store the Y-coordinate of the position of the mouse pointer.
			X_box= int(X//300)			#Storing the position of the box in which  the mouse is tapped according to the coordinates of the mouse's position.
			Y_box=int(Y//300)
	
			if(check_box_avail(X_box,Y_box)==1): 		#checking whether the box in which the mouse pointed is empty or not.
				if (player==1):						#creating the loop for the 1st player
					mark_box(X_box,Y_box,1)				#marks the box as 1 in which the played -1 pointed the mouse
					check_win(player)				#checking whether player-1 won the match or not. if won strikes all the 3 matching boxes
					if (check_win(player)==1):			#when player-1 won the match
			
						end_screen(1)				#showing the end screen(result) in the window
						GAME_OVER=1				#ending the loop by changing the GAME_OVER to 1
						break		
					if (check_board_full()==1):
						end_draw()
						GAME_OVER=1
						break

					player=2					#giving the chances to the players alterntively until the game gets over.
			
				elif(player==2):					#creating the loop for player 2 same as the player 1.
					mark_box(X_box,Y_box,2)
					check_win(player)
					if (check_win(player)==1):
						end_screen(2)

						GAME_OVER=1
						break
					if (check_board_full()==1):
						end_draw()
						GAME_OVER=1
						break
					player=1
												
			draw_OX()							#drawing the 'O' and 'X' symbols in the boxes according to the marks 1 and 2.
			print(Board)				
			


		if(event.type== pygame.KEYDOWN):					#creating a loop to restart the game.
			board()
			GAME_OVER=0
			player=1
			Board=[[0,0,0],[0,0,0],[0,0,0]]
		

	pygame.display.update()								#updating the screen for every step.


