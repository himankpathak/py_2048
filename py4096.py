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

def spacefunc(a,b):
	if(L[a][b]<10):
		return 5-1
	elif(L[a][b]<100):
		return 5-2
	elif(L[a][b]<1000):
		return 5-3
	elif(L[a][b]<10000):
		return 5-4
	else:
		return 1

def hightilefunc():
	global hightile
	for a in range(4):
		for b in range(4):
			if(L[a][b]>hightile):
				hightile=L[a][b]

def printfunc():
	hightilefunc()
	print ("\n")
	print ("#"*18)
	print (">","Score :",score)
	print (">","Moves :",moves)
	print (">","Highest Tile :",hightile)
	print ("#"*18,end="\n")
	print (" "*20,"_"*42)
	for a in range(4):
		print (" "*20,end="")
		print ("|",end="")
		for b in range(4):
			space=spacefunc(a,b)
			if(L[a][b]==0):
				print ("  ","  "*space,end="")
			else:
				print (L[a][b],"  "*space,end="")
		print ("|")
	print (" "*20,"--"*22)

def leftfunc(L,do):
	global pos
	global score
	for a in range(4):
		for b in range(4):
			if(L[a][b]!=0 and b-1>-1):
				while(n==False):
					if(L[a][b]==L[a][b-1]):
						pos=1
						L[a][b-1]+=L[a][b-1]
						score+=L[a][b-1]
						L[a][b-1]-=1000000
						L[a][b]=0
						break
					elif(L[a][b-1]!=0):
						break
					else:
						pos=1
						L[a][b-1]=L[a][b]
						L[a][b]=0
						if(b-2>-1):
							b-=1
						else:
							break
		if do:
			for b in range(4):
				if(L[a][b]<0):
					L[a][b]+=1000000

def rightfunc(L,do):
	global pos
	global score
	for a in range(4):
		for b in range(-1,-5,-1):
			if(L[a][b]!=0 and b+1<0):
				while(n==False):
					if(L[a][b]==L[a][b+1]):
						pos=1
						L[a][b+1]+=L[a][b+1]
						score+=L[a][b+1]
						L[a][b+1]-=1000000
						L[a][b]=0
						break
					elif(L[a][b+1]!=0):
						break
					else:
						pos=1
						L[a][b+1]=L[a][b]
						L[a][b]=0
						if(b+2<0):
							b+=1
						else:
							break
		if do:
			for b in range(4):
				if(L[a][b]<0):
					L[a][b]+=1000000


def main(L):
	global moves
	global pos
	global hightile
	global win
	global n
	pos=0
	while(n==False):
		#checklose n=True
		chance=input("Enter Where To Move : ")
		if(chance=="4" or chance=="a"):
			leftfunc(L,1)
			if(pos==1):
				moves+=1
				break
			else:
				print ("Its Not POSSIBLE!!")
		elif(chance=="6" or chance=="d"):
			rightfunc(L,1)
			if(pos==1):
				moves+=1
				break
			else:
				print ("Its Not POSSIBLE!!")
		elif(chance=="8" or chance=="w"):
			#moveup pos=1
			if(pos==1):
				moves+=1
				break
			else:
				print ("Its Not POSSIBLE!!")
		elif(chance=="2" or chance=="s"):
			#movedown pos=1
			if(pos==1):
				moves+=1
				break
			else:
				print ("Its Not POSSIBLE!!")
		elif(chance=="exo"):
			n=True
			win=True
		else:
			print ("Its Not POSSIBLE!!")
		if(hightile==4096):
			n=True
			win=True


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
	randomfunc()
	while(win==False):
		printfunc()
		main(L)
		randomfunc()
	if(win==True):
		print (cplayer,"Win!!")
	else:
		print (cplayer,"Lose Noob!!")
