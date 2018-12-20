from random import *
from string import *


def randomfunc():
	while(n==False):
		a1=randint(0,3)
		b1=randint(0,3)
		if(L[a1][b1]==0):
			count=randint(1,3)
			if(count==1 or count==2):
				L[a1][b1]=2
			elif(count==3):
				L[a1][b1]=4
			break

if __name__ == "__main__":

	print("""
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
				s - Down""")
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
	
	randomfunc()
