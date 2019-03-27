import numpy as np
import os
import cv2
import os.path
import glob
import re

os.system('clear')
print('\033[1;31m          -Intersect Data Base-\033[1m')
print('\033[1;31m                            v1.0\033[1m')
print(' ')
print('\033[1;31m   For commands type\033[1m \033[1;36mhelp\033[1m')

x = 0
y = 1

korisnik = input("\033[1;37mUsername: \033[1m")
lozinka = input("\033[1;37mPassword: \033[1m")

if korisnik == "admin":
	if lozinka == "admin":
		x = 1
else:
	print('\033[1;31m   [!]Wrong username or password\033[1m')
	exit()

def createImage(xName, rnsName):
	os.rename(xName, rnsName)

	os.system("cp " + xName + " /root/Desktop/IntersectDataBase")

def add():
	userName = input("\033[1;36m   User's name:\033[1m \033[1;37m")
	userLastname = input("\033[1;36m   User's lastname:\033[1m \033[1;37m")
	userBirth = input("\033[1;36m   User's birthday:\033[1m \033[1;37m")
	userAddress = input("\033[1;36m   User's address:\033[1m \033[1;37m")
	userAbout = input("\033[1;36m   About user:\033[1m \033[1;37m")
	userImage = input("\033[1;36m   Do you want to add image(y/n):\033[1m \033[1;37m")

	if userImage == "y":
		userImagePath = input("\033[1;36m   Path to image:\033[1m \033[1;37m")
		rnsAddName = userName + '_' + userLastname + '.jpg'
		createImage(userImagePath, rnsAddName)

	myFile = open(userName + '_' + userLastname + '.txt', 'w')
	myFile.write('\033[1;36m   Name:\033[1m \033[1;37m%s' % userName)
	myFile.write('\n')
	myFile.write('\033[1;36m   Lastname:\033[1m \033[1;37m%s\033[1m' % userLastname)
	myFile.write('\n')
	myFile.write('\033[1;36m   Birthday:\033[1m \033[1;37m%s\033[1m' % userBirth)
	myFile.write('\n')
	myFile.write('\033[1;36m   Address:\033[1m \033[1;37m%s\033[1m' % userAddress)
	myFile.write('\n')
	myFile.write('\033[1;36m   About:\033[1m \033[1;37m%s\033[1m' % userAbout)
	myFile.close()
	print('\n')
	print('\033[1;32m   [+]Successfully added!\033[1m')

def read():
	fileName = input("\033[1;36m   File name:\033[1m \033[1;37m")
	grupa = []

	a, b = fileName.split('.')
	imeFajla = a + ".png"

	print('\n')
	openFile = open(fileName, "r")
	for line in openFile:
		print(line)
	print('\n')

	for f123 in glob.glob("*.png"):
		x, y = f123.split('.')

		if a in x:
			grupa.append(f123)

	for item in grupa:
		ovaSlika = cv2.imread(f123)
		cv2.imshow(item, ovaSlika)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

def search():
	searchName = input("\033[1;36m   Search for:\033[1m \033[1;37m")

	baza = []
	b = 'index'

	for myfile in glob.glob("*.txt"):
		baza.append(myfile)
		if searchName in myfile:
			b = myfile
	if b != 'index':
		print('\033[1;32m   [+]Successfully found!\033[1m')
		print('   %s' % b)
	else:
		print('\033[1;31m   [!]User data does not exist!\033[1m')

def listAll():

	numUsera = 0

	for myfile in glob.glob("*.txt"):
		numUsera += 1
		print('\033[1;36m   %s\033[1m' % myfile)
	if numUsera == 0:
		print('\033[1;31m   [!]User data does not exist!\033[1m')

def delete():
	fileName = input("\033[1;36m   File name:\033[1m \033[1;37m")
	k, l = fileName.split('.')
	imeSlike = k + ".png"
	sveSlike = []

	for ime in glob.glob('*.png'):
		if k in imeSlike:
			sveSlike.append(ime)

	if os.path.isfile(fileName):
		os.remove(fileName)
		if sveSlike:
			for i in range(0, len(sveSlike)):
				os.remove(sveSlike[i])
		print('\n')
		print('\033[1;32m   [+]Successfully deleted!\033[1m')
	else:
		print('\n')
		print('\033[1;31m   [!]%s does not exist\033[1m' % fileName)

def logout():
	os.system('python Intersect.py')
	exit()

def defInput():
	myInput = input("\033[1;37m> \033[1m")
	#help
	if myInput == "help":
		print('\033[1;36m   help   -> Open help menu\033[1m')
		print('\033[1;36m   ------------------------------------------------------\033[1m')
		print('\033[1;36m   add    -> Create new user data\033[1m')
		print('\033[1;36m   read   -> Read user data\033[1m')
		print('\033[1;36m   delete -> Delete user data\033[1m')
		print('\033[1;36m   list   -> List all user data\033[1m')
		print('\033[1;36m   search -> Search for user data by name or lastname\033[1m')
		print('\033[1;36m   logout -> Logout from Intersect Data Base\033[1m')
		print('\033[1;36m   exit   -> Exit Intersect Data Base\033[1m')

	#add user data
	elif myInput == "add":
		add()

	#read user data
	elif myInput == "read":
		read()

	#delete user data
	elif myInput == "delete":
		delete()

	#list user data
	elif myInput == "list":
		listAll()

	#logout
	elif myInput == "logout":
		logout()

	#search for users
	elif myInput == "search":
		search()

	#exit
	elif myInput == "exit":
		exit()
	else:
		print('\033[1;31m   [!]%s is not in Intersect command list\033[1m' % myInput)


def startAdmin():
	while 2 > 1:
		defInput()

if x == 1:
	startAdmin()
