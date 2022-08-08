import os
import random

class newgame:
	def __init__(self,player1,player2):
		self.p=[player1,player2]
		self.c=[0,0]
		self.last=[0,0]
	def saapsidhi(self,a):
		if self.c[a]==96:
			self.c[a]=42
		elif self.c[a]==94:
			self.c[a]=71
		elif self.c[a]==75:
			self.c[a]=32
		elif self.c[a]==47:
			self.c[a]=16
		elif self.c[a]==37:
			self.c[a]=3
		elif self.c[a]==28:
			self.c[a]=10
		elif self.c[a]==4:
			self.c[a]=56
		elif self.c[a]==12:
			self.c[a]=50
		elif self.c[a]==14:
			self.c[a]=55
		elif self.c[a]==22:
			self.c[a]=58
		elif self.c[a]==41:
			self.c[a]=79
		elif self.c[a]==54:
			self.c[a]=88
	def board(self):
		print("Snakes: 96->42\t94->71\t75->32\t47->16\t37->3\t28->10")
		print("Ladder: 4->56\t12->50\t14->55\t22->58\t41->79\t54->88")
		for i in range(100,0,-1):
			if(i%10==0):
				if i==self.c[1]:
					print("\n",(self.p[1])[0],end="   ")
				elif i==self.c[0]:
					print("\n",(self.p[0])[0],end="   ")
				else:
					print("\n",i,end="   ")
			else:
				if i==self.c[1]:
					print((self.p[1])[0],end="   ")
				elif i==self.c[0]:
					print((self.p[0])[0],end="   ")
				else:
					print(i,end="   ")
		print("\t",self.p[0]," : ",self.last[0],"\t",self.p[1]," : ",self.last[1])
	def move(self,a):
		if self.p[a]!='Computer':
			dice=input("\nPress any key to roll : ")
		self.last[a]=random.randint(1,6)
		if self.c[a]==0 and self.last[a]==6:
			self.c[a]=1
		elif self.c[a]!=0 and self.c[a]+self.last[a]<=100:
			self.c[a]+=self.last[a]
		self.saapsidhi(a)
	def start(self):
		flag=0
		while self.c[0]!=100 and self.c[1]!=100:
			os.system('clear')
			self.board()
			if flag==0:
				print("Player ",self.p[0]," Move")
				self.move(0)
				flag=1
			elif flag==1:
				print("Player ",self.p[1]," Move")
				self.move(1)
				flag=0	
			if self.c[0]==100:
				print("\t\t",self.p[0]," is Winner")
			elif self.c[1]==100:
				print("\t\t",self.p[1]," is Winner")
			
			
print("\t\t\tWELCOME TO SAAP SIDHI KHEL")
print("\t1.Man To Man")
print("\t2.Man To COMPUTER")
print("\t3.EXIT")
choice=int(input("Enter Choice : "))
while choice!=3:
	if choice==1:
		player1=input("Enter First Player Name : ")
		player2=input("Enter Second Player Name : ")
		game=newgame(player1,player2)
		game.start()
		choice=3
	elif choice==2:
		player=input("Enter player Name : ")
		game=newgame(player,"Computer")
		game.start()
		choice=3
