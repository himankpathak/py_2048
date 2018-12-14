from random import *
from string import *


if __name__ == "__main__":
  	
	print"""
	Welcome to 4096 v0.1

	Objective: Make The 4096 Tile To Win!!

	Instructions :
	1. Turn On Your Num Lock.
	2. Use Following Keys To Navigate:

				8 - Up
		4 - Left        6 - Right
				2 - Down
				
	3. You can also use WASD.
				w - Up
		a - Left        d - Right
				s - Down

	"""
	L=[]
	n=win=False
	score=pos=hightile=moves=0
	for a in range(4):
		l=[]
		for b in range(4):
			l.append(0)
		L.append(l)
    
	cplayer=input("Enter Your Name : ")
	cplayer=cplayer.capitalize()


