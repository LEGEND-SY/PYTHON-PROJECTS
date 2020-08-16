i#Hello and welcome to LEGEND ASSISTANT
#first of all its alpha , okay?
#my github page : https://github.com/LEGEND-SY
#Please download those packages from pip
from colored import fg , bg , attr
import time
import random
import os
import getpass
import wikipedia
import requests
y = {}
y1 = {}
'''
WARNING : IF YOU USING THE PROJECT FROM ANDROID DEVICE DONT CHANGE ANY THING (BUT) IF YOU USING THE PROJECT ON THE OTHER DEVICES LIKE PC/MAC/IOS.....
PLEASE CHANGE THE A FILE PATH.
---EX : IF YOU USING THIS ON WINDOWS
path = "c:/examplepath" + "LegendAssistantUser.txt"
THIS IS A EXAMPLE , YOU CAN CHANGE A PATH TO ANYWHERE
'''
try :
    path = "/sdcard/" + "LegendAssistantUser.txt"
    url = 'https://raw.githubusercontent.com/LEGEND-SY/PYTHON-PROJECTS/master/LEGEND-ASSISTANT/LegendAssistant.txt' 
    r = requests.get(url, allow_redirects=True)
    open('/sdcard/LegendAssistant.txt' , 'wb').    write(r.content)
    open( path , 'a+')
    with open( path ) as v :
              with open("/sdcard/LegendAssistant.txt") as f:
                  for line in f:
                      (key, val) = line.split()
                      key = key.replace('_' , ' ')
                      y[key] = val.replace('_' , ' ')
                  for line2 in v:
                      (key1 , val1) = line2.split()
                      key1 = key1.replace('_' , ' ')
                      y1[key1] = val1.replace('_' , ' ')
except :
    print(fg('red') + "You have a problem with the file path\nplease check the path and try again!" + attr('reset'))
password1 = '5'
red = fg('red') + bg('white')
black = fg('black') + bg('white')
green = fg('green') + bg('white')
blue = fg('blue') + bg('white')
gold = fg('190') + bg('black')
redn = fg('red')
greenn = fg('green')
at = attr('reset')
v =at + '___________________________________________________________________' + at


def self(x) :
	while True :
		for a , b in y.items() :
				if x.lower().strip() == a.lower().strip() :
					point()
					print (black + b)
					print(v)
					time.sleep(0.3)
					AssistantServer(self)
		for a , b in y.items() :
				if x.lower().strip() != a.lower().strip() :
					for a1 , b1 in y1.items() :
					    if x.lower().strip() == a1.lower().strip() :
					        point()
					        print(black + b1)
					        print(v)
					        time.sleep(0.3)
					        AssistantServer(self)
					    elif x.lower().strip() != a1.lower().strip() :
					        point()
					        print(black + "Sorry! , I Don't understand! ")
					        print(v)
					        AssistantServer(self)
					
def search(x) :
		point()
		try :
			attr('reset')
			os.system('clear')
			print('')
			wi = (black + wikipedia.summary(x , sentences = 2) + at)
			wi = wi.replace('.' , '\n')
			print ('Accourding to Wikipedia :')
			print(v)
			print(' ')
			time.sleep(1)
			print(wi)
			print(v)
			time.sleep(0.3)
			AssistantServer(self)
		except :
			os.system('clear')
			print(black +"Sorry I don't understand!" + at)
			time.sleep(2.5)
			os.system('clear')
			AssistantServer(self)
		
					
def Quit(x) :
	print ('Thanks for using MY Assistant')
	quit()
			
			
def self2(x) :
	point()
	print (at + green + 'Welcome To ' + blue + 'LEGEND Assistant Setting ^^' + at)
	print(v)
	x = black + 'Enter Password :' + at
	password = getpass.getpass(x)
	if password == password1 :
		os.system('clear')
		time.sleep(0.3)
		print('Logging in......')
		time.sleep(1.50)
		print(green + 'Correct>>' + at)
		time.sleep(0.5)
	else :
		i = 0
		os.system('clear')
		print('Logging in.....')
		time.sleep(2)
		while i < 100 :
			print (fg('light_red')+ 'Permission denided!!!!'+ at)
			time.sleep(0.008)
			os.system('clear')
			print (fg('red')  + 'ERRRRRRRORRRR!' + attr('reset'))
			time.sleep(0.008)
			i += 1
			if i == 100 :
				Quit(x)
	choose()
		

def choose() :
		os.system('clear')
		time.sleep(0.5)
		print (gold + '1. Change dict')
		time.sleep(0.05)
		print ('2. Change password')
		time.sleep(0.05)
		print ('3. Quit' + at)
		time.sleep(0.05)
		cho()


def choose0():
		return choose()
		
		
def cho() :                  #Apply Setting
		choose = int(input())
		if choose == 1 :
			changedict()
		elif choose == 2 :
			os.system('clear')
			time.sleep(0.05)
			print('Comming Soon!')
			time.sleep(1)
			choose0()
		elif choose == 3 :
			choose3()
			
def return_changedict():
			return changedict()
			
def changedict() :
			os.system('clear')
			time.sleep(0.5)
			print(gold + '1. Show dict')
			time.sleep(0.05)
			print('2. Add new dict')
			time.sleep(0.05)
			print('3. Return' + at)
			di = int(input())
			if di == 1 :
				os.system('clear')
				time.sleep(0.05)
				print ('Your dict is :')
				for a , b in y.items() :
					time.sleep(0.15)
					print (redn + a + at, '===' ,greenn+ b + at)
				for a1 , b1 in y1.items() :
				       time.sleep(0.15)
				       print(redn + a1 + at , '===' , greenn + b1 + at)
				       time.sleep(0.05)
				t = input('Enter to Return!')
				return_changedict()
			elif di == 2 :
				os.system('clear')
				add_dict()
			elif di == 3 :
				os.system('clear')
				choose()
			
def add_dict() :            #Change dict
			print ('Type Done if you finish : ) ')
			time.sleep(0.9)
			while True :
				print(v)
				x1 = input(at +'Enter Key :' + redn)
				if x1.lower() == 'done' :
					choose()
				x2 = input(at + 'Enter Value :' + greenn)
				print(v)
				
				if x2 == '' :
					x2 = 'NoneType'
				try :
					    with open( path , 'a') as r :
					        c = str(x1.replace(' ' , '_'))  +' ' + str(x2.replace(' ' , '_'))
					        r.write( c + '\n')
				except :
					    print(redn + 'You have a problem with the path file on line 191 \n please check the path and try again!')
					    print('1 . Contact us')
					    print('2 . Return' + at)
					    problem = input(':')
					    if problem == '1' :
					           point()
					           contact_us()
					    else :
					       point()
					       AssistantServer(self)
				        
				if x1 == 'Done' :
					print('Dict was changed Sucssefully !!!!!!!!')
					choose()
					break
					
				if x1 == 'q' : 
					print (fg('red')+ 'ERRRRRRRRRRORRRRRRRR!')
					quit()
				
				
def choose3() :
	print ('Done!')
	time.sleep(1)
	os.system('clear')
	AssistantServer(self)
	
def point():
		print(at)
		os.system('clear')
		print(at)
		os.system('clear')
		print(at + black + '.' + at)
		time.sleep(0.3)
		os.system('clear')
		print(black + '..'+ at)
		time.sleep(0.3)
		os.system('clear')
		print(black +'...'+ at)
		time.sleep(0.3)
		os.system('clear')
		
def contact_us() :
	print(redn + 'You can send me your problem in email : ' , greenn + 'Mohamedbabnssi@gmail.com' + at)
	print(redn + 'My GITHUB page :' , greenn + 'https://github.com/LEGEND-SY' + at)
	time.sleep(3)
	print(v)
	print('1 . Return')
	print('2 . Quit')
	x = input(':')
	if x == '1' :
	    point()
	    AssistantServer(self)
	else :
	    point()
	    Quit(self)
	
def AssistantServer(self) :
	#print(v)
	z = input (red + 'How can I help for you?' + at +' ' + black +  '(•‿•)'  + at  +':'  + black)
	
	if z == 'q' :
		#print(v)
		Quit(z)
		
	elif z == 'LEGEND' :
		#print(v)
		self2(z)
		
	elif 'weather' in z.lower() :
	    point()
	    print('comming soon :)')
	    time.sleep(1)
	    print(v)
	    AssistantServer(self)
	    
	elif 'search' in z.lower() :
	    def listToString(s):
	           s.remove('search')
	           try:
	               s.remove('about')
	           except :
	               x = 1
	           str1 = ""
	           for ele in s:  
	               str1 +=' ' + ele
	           return str1
	    s = z.split()
	    listToString(s)
	    search(s)
	    
	else :
		self(z)
			
AssistantServer(self)
