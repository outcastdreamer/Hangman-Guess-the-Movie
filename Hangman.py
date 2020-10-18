#Let the game begin
import random as r
import pprint 
import os
import string
from threading import Timer
from stopwatch import Stopwatch                 
import time


os.system("cls")

f=open("movies.txt","r")
k=f.readlines()
k.pop()
#pprint.pprint(k)
m=[]
for i in k:
	l=i.split()
	m.append(l)
	

for i in range(len(m)):
	m[i].pop(0)


for r1 in range(3):
	i=0
	flag=0
	while i!=len(m):
		j=0
		z=0
		while j!=len(m[i]):
			z=0
			#print (m[i][j][z])
			while z!=len(m[i][j]):
				if m[i][j][z].isalpha()==False:
					m.pop(i)
					flag=1
					break
				z+=1
				flag=0
			if flag==0:
				j+=1
			else:
				break
		i+=1



movies=[]
for i in range(len(m)):
	s=" "
	s=s.join(m[i])
	movies.append(s)
i=0
while i!=len(movies):
	if len(movies[i])<8:
		movies.pop(i)
	i+=1

r.shuffle(movies)

#pprint.pprint(movies)
#print ("\n\n ",len(movies))
#print ("\n\n ",len(k))
wins=0
losses=0

def timer():
	print ("\n\n\nTime is up!! Please try again! Restarting a new movie!!")
	time.sleep(4)
	os.system("cls")
	hangman()

tm = Timer(180, timer)
tm.start()


def hangman():
	global wins
	global losses
	chances=5
	replaced_letters=[]
	replaced_index=[]
	choice=r.choice(movies)
	#choice="Stuart Little"
	l_ogi=[x.upper() for x in choice]
	#print ("l_ogi : ",l_ogi)
	l_choice=[x.upper() for x in choice]
	for i in range(len(l_choice)+10):
		c=r.randint(0,len(l_choice)-1)
		c1=r.randint(0,len(l_choice)-1)
		while c-1==c1 or c-2==c1 or c1-1==c or c1-2==c:
			c=r.randint(0,len(l_choice)-1)
		if l_choice[c]==" ":
			pass
		if l_choice[c]=="_":
			pass
		elif l_choice[c]==" ":
			pass
		else:
			#print (l_choice[c])
			l_choice[c]="_"
	s=" "
	s=s.join(l_choice)
	print ("\n\n\n\t\tWELCOME TO HANGMAN GAME!!!")
	print ("\n\nGUESS THE FOLLOWING MOVIE : ")
	print ("\n\n",s,"\n")
	#print (choice,"\n")
	l=string.ascii_uppercase
	letters=[x for x in l]
	temp=[x.upper() for x in choice]
	for i in range(len(l_choice)):
		if l_choice[i].isalpha()==False and l_choice[i].isspace()==False:
			replaced_letters.append(temp[i])
			replaced_index.append(i)
	#print ("replaced_letters :",replaced_letters)
	#print (replaced_index)
	i=0
	j=0
	while i!=len(replaced_letters):
		while letters.count(replaced_letters[i])>0:
			letters.pop(letters.index(replaced_letters[i]))
		i+=1
	#print (letters)
	temp_replaced_letters=[]
	temp_replaced_letters+=replaced_letters
	r.shuffle(temp_replaced_letters)
	for i in range(8):
		r.shuffle(letters)
		h=r.choice(letters)
		temp_replaced_letters.append(h)
		r.shuffle(temp_replaced_letters)
	i=0
	for e in range(5):
		while i!=len(temp_replaced_letters):
			if temp_replaced_letters.count(temp_replaced_letters[i])>1:
				temp_replaced_letters.pop(i)
			i+=1
	stopwatch = Stopwatch()
	tt = 1
	while chances!=0:
		#print (int(stopwatch.duration))
		if tt == 1:
			print ("\n\n\t YOU HAVE 3 minutes and %d CHANCES LEFT TO WIN THE GAME!!!!"%(chances))
			tt = 0
		else:
			temp_time = float(stopwatch.duration)
			new_min = (180 - temp_time)//60
			new_sec = (180 - temp_time)%60
			print ("\n\n\t YOU HAVE %d min %d secs AND %d CHANCES LEFT !!!!"%(new_min,new_sec,chances))		
		temp_s="  "
		temp_s=temp_s.join(temp_replaced_letters)
		print ("\nGUESS FROM THESE LETTERS : \n\n\t\t",temp_s)
		while True:
			try:
				#os.system("python timer.py")
				"""print ("Stopwatch time : ",int(stopwatch.duration))
				if int(stopwatch.duration) > 5:
					print ("\nTime is up!! Please try again! Restarting a new movie!!")
					time.sleep(4)
					os.system("cls")
					hangman()
				"""
				user_letter_choice=input("\n\tEnter your choice : ").upper()
				temp_index=temp_replaced_letters.index(user_letter_choice)
				temp_replaced_letters.pop(temp_index)
				break
			except ValueError:
				print ("\n\t\t\tERROR!! The letter you chose is not in the given list! Please try again!!")
		os.system("cls")
		while True:
			try:
				index=replaced_letters.index(user_letter_choice)
				print ("\n\n\tNOT BAD! Right guess!")
				if replaced_letters.count(user_letter_choice)>1:
					while replaced_letters.count(user_letter_choice)>=1:
						#v=replaced_letters.count(user_letter_choice)
						#print ("count : ",v)
						index=replaced_letters.index(user_letter_choice)
						l_choice[replaced_index[index]]=user_letter_choice
						#print ("index : ",index)
						replaced_letters.pop(index)
						replaced_index.pop(index)
						#print ("replaced_letters :",replaced_letters)
						#print ("l_choice : ",l_choice)
				else:
					l_choice[replaced_index[index]]=user_letter_choice
				break
			except ValueError:
				print ("\n\n\t\t WRONG GUESS!! PLEASE TRY AGAIN!!")
				chances-=1
				break
		s=" "
		s=s.join(l_choice)
		print ("\n\n",s)
		if l_choice.count("_")==0:
			print ("\n\n\n\n\n\t\t YOU HAVE GUESSED THE RIGHT MOVIE!!!")
			wins+=1
			print ("\n\nYour current no. of wins is : ",wins)
			print ("\n\nYour current no. of losses is : ",losses)
			print ("\n\n\tDo you want to play again?")
			u=input("\n\t\tEnter \'Y\' for YES and \'N\' for NO : ").upper()
			if u.upper()=="Y":
				os.system("cls")
				hangman()
			else:
				print ("\n\n\nTHANKS FOR PLAYING THE GAME!! PLEASE PLAY AGAIN!\n\n\n\n")
				exit()
		if chances==0:
			losses+=1
			print ("\n\n\n\n\n\n\t\t BOO!! YOUR CHANCES ARE OVER AND YOU COULDN\'T GUESS THE MOVIE!!")
			print ("\n\n\t\tThe movie\'s name is : ",choice)
			print ("\n\nYour current no. of wins is : ",wins)
			print ("\n\nYour current no. of losses is : ",losses)
			print ("\n\n\tDo you want to play again?")
			u=input("\n\t\tEnter \'Y\' for YES and \'N\' for NO : ").upper()
			if u.upper()=="Y":
				os.system("cls")
				hangman()
			else:
				print ("\n\n\nTHANKS FOR PLAYING THE GAME!! PLEASE PLAY AGAIN!\n\n\n\n")
				exit()
	tm.join()





hangman()