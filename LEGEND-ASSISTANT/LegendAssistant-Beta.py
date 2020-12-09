'''
-Hello and welcome to LEGEND ASSISTANT ♡
-First of all it's Beta , okay?
-My Github: https://github.com/LEGEND-SY
-FOR A REAL TERMINAL ONLY! '''


'''Please download this packages from pip'''
try : #PACKAGES
    from colored import fg , bg , attr #colored
    from googletrans import Translator #googletrans
    import time
    import random
    import os
    import wikipedia
    import requests
    import pafy
    import youtube_dl
except:
    print("-You don't downloanded all package \n please download the packages from pip")
    quit()
    
y = {} #Q&A FROM THE SERVER
y1 = {} #Q&A FROM THE USER

def T(z) : #SLEEPING TIME
    time.sleep(z)
def C() : #CLEAR THE SCREEN
    os.system('clear')
def reAssistant2() :
    T(0.1)
    print(v)
    T(0.2)
    Assistant2()

path = str(os.getcwd()) #GET THE PATH
user = path + "/LegendAssistantUser.txt" #NAME OF THE FILE TO SAVE THE Q&A FROM USER

def loading(z , c) : #LOADING SCREEN IN FIRST RUN
    x = fg(c)  + '■' + attr('reset')
    y2 = 0
    y1 =  35
    while True :
        while y2 <= y1 :
            print(z.rjust(37) + '...')
            print(''.rjust(15) , x * y2) #15
            T(0.006)
            C()
            y2 +=1
        break
        C()
    C()


def loading_stop(z) : #LOADING SCREEN WHEN THE LOADING STOPPED TO DOWNLOAD THE FILES FROM THE SERVER
    x = fg('yellow')  + '■' + attr('reset')
    print(z)
    print(''.rjust(15) , x * 35)

	        
def legend_assistant() : #SCRIPT TO DOWNLOAD Q&A FROM THE SERVER AND USER , AND PUT IT TO A FILE TO RECOVERT IT LATER
        loading('loading' , 'green')
        user = path + "/LegendAssistantUser.txt" 
        black = fg('black') + bg('white')
        loading_stop('Connecting'.rjust(37) + '...')
        url = 'https://raw.githubusercontent.com/LEGEND-SY/PYTHON-PROJECTS/master/LEGEND-ASSISTANT/LegendAssistant.txt' 
        r = requests.get(url, allow_redirects=True) #DOWNLOAD THE Q&A FROM THE SERVER
        open(path + '/LegendAssistant.txt' , 'wb').    write(r.content)
        check_if_not_first_start()
        try :
                with open( user ) as vv : # FILTER THE Q&A FROM THE USER AND MAKE IT AS A DICTIONARY Y1
                  for line2 in vv :
                      (key1 , val1) = line2.split()
                      key1 = key1.replace('_' , ' ').lower().replace('?' , '').strip()
                      y1[key1] = val1.replace('_' , ' ')
                      
        except:
             pass               
        with open( path + "/LegendAssistant.txt") as f: #FILTER THE Q&A FROM THE SERVER AND MAKE IT AS A DICTIONARY Y
            for line in f:
                          (key, val) = line.split()
                          key = key.replace('_' , ' ').lower().replace('?' , '').strip()
                          y[key] = val.replace('_' , ' ')
        urls = 'https://raw.githubusercontent.com/LEGEND-SY/PYTHON-PROJECTS/master/LEGEND-ASSISTANT/random.txt' 
        ru = requests.get(urls, allow_redirects=True) #DOWNLOAD THE TIPS
        open(path + '/random.txt' , 'wb').write(ru.content)
        loading('loading' , 'green')
        C()

#_________INFO____
password1 = '5'
red = fg('88') + bg('white')
goldn = fg('19') + bg('3')
black = fg('black') + bg('white')
green = fg('green') + bg('white')
blue = fg('blue') + bg('white')
gold = fg('190') + bg('black')
redn = fg('red')
greenn = fg('green')
at = attr('reset')
v =at + '___________________________________________________________________' + at

def save(s) : #TEST DEF
    z = s
    print(gold +"Tip" + at + ' ' + gold +  "You can type ' Translate it ' if you want translate this " + at)
    if Assistant(self).lower() == 'translate it ' :
        print('translate')
        Assistant2()
        
        
def self(x) : #SCRIPT ... THE CONTROL OF THE ASSISTANT ... IF THE Q IS IN THE SERVER FILE ; THE SCRIPT PUT THE A , IF NOT THEN CHECK THE USER FILE , IF NOT THERE ? , HE PUT SORRY ANSWER 
                x = x.lower().replace('?' , '').strip()
                point()
                try :
                    print (black + y[x] +at)
                    reAssistant2()
                except :
                  try :
                      print (black + y1[x] + at)
                      reAssistant2()
                  except :
                      if y == {} : #THE DICTIONARY IS EMPTY CAUSE HE CAN'T DOWNLOAD THE FILES FROM SERVER WHEN THE PHONE IS OFFLINE !
                              print(black + 'Your phone’s offline , so I can’t help you with that at the moment.' + at)
                              reAssistant2()
                      else :
                          print(black + "Sorry , I don't understant!" + at)
                          reAssistant2()
				    	  
				    	  
def search(x) : #--SCRIPT-- WIKIPEDIA
			point()
			attr('reset')
			C()
			print('')
			wi = (black + wikipedia.summary(x , sentences = 2) + at)
			point()
			wi = wi.replace('.' , '\n')
			print ('Accourding to Wikipedia :')
			print(v)
			print(' ')
			T(1)
			print(wi)
			save(wi) #TEST
			reAssistant2()

					
def Quit(x) : #QUIT THE PROGRAM IF THE USER TYPE 'q'
	point()
	print (black +'Thanks for using LEGEND Assistant')
	T(100)
			
			
def self2(x) : #THE ASSISTANT SETTING FOR SHOW AND ADD THE Q&A 'S FROM THE FILE
	point()
	print (at + green + 'Welcome To ' + blue + 'LEGEND Assistant Setting ^^' + at)
	print(v)
	x = black + 'Enter Password :' + at
	password = input(x)
	if password == password1 : #THE PASSWORD
		C()
		T(0.3)
		print('Logging in......')
		T(1.50)
		print(green + 'Correct>>' + at)
		T(0.5)
	else : #IF THE PASSWORD IS INCORRECT
		i = 0
		C()
		print('Logging in.....')
		T(2)
		while i < 100 :
			print (fg('light_red')+ 'Permission denided!!!!'+ at)
			T(0.008)
			C()
			print (fg('red')  + 'ERRRRRRRORRRR!' + attr('reset'))
			T(0.008)
			i += 1
			if i == 100 :
				Quit(x)
	choose()
		

def choose() : #THE MENU OF SETTING
		C()
		T(0.5)
		print (gold + '1. Change dict')
		T(0.05)
		print ('2. Change password')
		T(0.05)
		print ('3. Quit' + at)
		T(0.05)
		cho()


def choose0(): #RETURN TO CHOOSE()
		return choose()
		
		
def cho() : #APPLY THE SETTING FROM CHOOSE()
		choose = int(input())
		if choose == 1 :
			changedict()
		elif choose == 2 :
			C()
			T(0.05)
			print('Comming Soon!')
			T(1)
			choose0()
		elif choose == 3 :
			choose3()
			

			
						
			
def return_changedict(): #RETURN TO CHANGEDICT()
			return changedict()
			
			
def changedict() : #IF THE USER TYPE (1.CHANGE DICT)
			C()
			T(0.5)
			print(gold + '1. Show dict')
			T(0.05)
			print('2. Add new dict')
			T(0.05)
			print('3. Return' + at)
			di = int(input())
			if di == 1 :
				C()
				T(0.05)
				print ('Your dict is :')
				for a , b in y.items() : #SHOW THE Q&A
					T(0.15)
					print (redn + a + at, '===' ,greenn+ b + at)
				for a1 , b1 in y1.items() :
				       T(0.15)
				       print(redn + a1 + at , '===' , greenn + b1 + at)
				       T(0.05)
				t = input('Enter to Return!')
				return_changedict()
			elif di == 2 :
				C()
				add_dict()
			elif di == 3 :
				C()
				choose()
			
			
def add_dict() :  #ADD NEW Q&A
			print ('Type Done if you finish : ) ')
			T(0.9)
			while True :
				print(v)
				x1 = input(at +'Enter Question :' + redn)
				if x1.lower() == 'done' :
					choose()
				x2 = input(at + 'Enter Answer :' + greenn)
				print(v)
				
				if x2 == '' :
					x2 = 'NoneType'
				try :
					    with open( user , 'a') as r : #PUT THE NEW Q&A TO THE USER FILE 
					        c = str(x1.replace(' ' , '_'))  +' ' + str(x2.replace(' ' , '_'))
					        r.write( c + '\n')
				except :
					    print(black + 'ERROR' + at)
					    T(1)
					    Assistant2()
				        
				if x1 == 'Done' : #IF THE USER IS FINISHED
					print('Dict was changed Sucssefully !!!!!!!!')
					choose()
					break
					
				if x1 == 'q' : 
					print (fg('red')+ 'ERRRRRRRRRRORRRRRRRR!')
					Quit()
				
				
def choose3() : #RETURN TO ASSISTANT
	print ('Done!')
	T(1)
	C()
	Assistant2()
	
def point(): #LOADING WHILE THE USER TYPE THE Q
		print(at)
		C()
		print(at)
		C()
		print(at + black + '.' + at)
		T(0.2)
		C()
		print(black + '..'+ at)
		T(0.2)
		C()
		print(black +'...'+ at)
		T(0.2)
		C()
		
def calculator() : #--SCRIPT-- CALCULATOR WHEN THE USER TYPE 'CALCULATOR'
	print('Welcome to calculator ' + greenn + 'BETA' + at)
	T(1)
	print("Type 'Done' when you finish")
	T(0.5)
	print(v)
	y = input(black)
	while True :
	    if '+' in y :
	    	y = y.split('+')
	    	try :
	    	      z = int(y[0]) + int(y[1])
	    	except :
	    	      z = 0
	    elif '-' in y :
	    	y = y.split('-')
	    	try :
	    	    z = int(y[0]) - int(y[1])
	    	except :
	    	    z = 0
	    elif '*' in y :
	    	y = y.split('*')
	    	try :
	    	    z = int(y[0]) * int(y[1])
	    	except :
	    	    z = 0
	    elif '/' in y :
	    	y = y.split('/')
	    	try :
	    	       z = float(y[0]) / float(y[1])
	    	except :
	    	       if y[1] == '0' :
	    	           print('Genius but not with me' + greenn + ' ᕦ(ò_óˇ)ᕤ ')
	    	           z = 0
	    	       else :
	    	           z = 0
	    elif 'done' in y.lower() :
	        print('Done')
	        break
	        Assistant2()
	    else :
	    	print ('An error has detectied please try again')
	    	z = 0
	    print( at + '__________________' + black)
	    xx = input(z)
	    y = ''.join(str(z)+xx)
	    
def rps(): #--SCRIPT-- THE ROCK , PAPER AND SCISSORS GAME FROM THE GAME CENTER WHEN THE USER TYPE 'GAME'
	point()
	print('There was a')
	T(0.5)
	rock = (fg('yellow')+ "    _________\n---'     ____)\n        (_____)\n        (_____)         Rock\n        (____)\n---.____(___)\n" + attr('reset'))
	print(rock)
	T(0.5)
	print( '\n')
	T(0.5)
	paper = (fg('yellow') + "    ________ \n---'    ____)_____\n         _________)\n          _________)    Paper\n         _________)\n---.____________)\n" + attr('reset'))
	print(paper)
	T(0.5)
	print('\n')
	T(0.5)
	scissors = (fg('yellow') + "    ________ \n---'     ___)_____\n            ______)\n         __________)    Scissors\n        (____)\n---.____(___)\n")
	print(scissors + attr('reset'))
	T(0.5)
	print('\n')
	y = ['rock' , 'paper' , 'scissors']
	T(1)
	print('Type quit or cancel when you finish')
	while True :
	       x = input ('- Your choose : ').lower()
	       if x.lower() == 'rock' :
	           T(1)
	           print(rock)
	       elif x.lower() == 'paper' :
	           T(1)
	           print(paper)
	       elif x.lower() == 'scissors' :
	           T(1)
	           print(scissors)
	       if x in y :
	           yy = y[random.randrange(3)]
	           T(2)
	           print('- My choose is : ')
	           if yy == 'rock' :
	               T(2)
	               print(rock)
	           elif yy == 'paper' :
	               T(2)
	               print(paper)
	           elif yy == 'scissors' :
	               T(2)
	               print(scissors)
	           if x == yy :
	               T(1)
	               print('WE TIED! ^_^')
	           elif x == 'rock' and yy == 'scissors' :
	               T(1)
	               print(fg('green') + 'YOU WIN! D:' + attr('reset'))
	           elif x == 'paper' and yy == 'rock' :
	               T(1)
	               print(fg('green') + 'YOU WIN! D:' + attr('reset'))
	           elif x == 'scissors' and yy == 'paper' :
	               T(1)
	               print(fg('green') + 'YOU WIN! D:' + attr('reset'))
	           else :
	               T(1)
	               print(fg('red') + 'YOU LOSE! :D' + attr('reset'))
	       elif x.lower() == 'quit' or x.lower() == 'cancel' :
	           point()
	           chooseServer('game')
	       else :
	           print('Error ,Try again')
	       T(1)
		
def randgame() : #--SCRIPT-- THE RANDOM NUMBER GAME FROM THE GAME CENTER WHEN THE USER TYPE 'GAME'
       def animation():
	       x = ('Let me see :')
	       rock = (fg('yellow')+ "    _________\n---'     ____)\n        (_____)\n        (_____)         \n        (____)\n---.____(___)\n" + attr('reset'))
	       paper = (fg('yellow') + "    ________ \n---'    ____)_____\n         _________)\n          _________)    \n         _________)\n---.____________)\n" + attr('reset'))
	       C()
	       print(x)
	       print(rock)
	       T(0.7)
	       C()
	       print(x)
	       print(paper)
	       T(0.7)
	       C()
	       print(x)
	       print(rock)
	       T(0.7)
       def testgame():
           print('I have a number on my hand , can you guess it?')
           T(2)
           print('\nyou have ● ● ● ● tries')
           T(0.5)
           print(v)
           yy = 'No' , '●' , '● ●' , '● ● ●'
           x = random.randrange(1 ,10)
           y = 4
           while y != 0 :
               inp = input(':')
               if str(x) == inp :
                   animation()
                   xx = 'You so smart!' , 'NICE!!!' , 'Oh my god!' , 'Nice try , Correct!' , 'Correct!'
                   print(fg('green') + xx[random.randrange(4)] + attr('reset'))
                   break
               elif 'quit' in inp.lower() or 'cancel' in inp.lower():
                   chooseServer('game')
               elif x != inp :
                   y -= 1
                   animation()
                   xx = 'NO NO NO ' , 'Sorry :(' , 'sooo , No' , 'ooops , wrong!' , 'Wrong!'
                   print(fg('red') + xx[random.randrange(4)] + attr('reset'))
                   print('You have' , yy[y] , 'tries' )
           trys = input('Try again? :')
           if 'y' in trys.lower() :
               testgame_return()
           elif 'n' in trys.lower() :
               chooseServer('game')
           else :
               print("I think its yes , let's trying again")
               T(3)
               testgame_return()	        
       def testgame_return():
               C()
               testgame()
       testgame()
		
def contact_us() : #CONTACT ME 
	print(redn + 'You can send me your problem in email : ' , greenn + 'Mohamedbabnssi@gmail.com' + at)
	print(redn + 'My GITHUB page :' , greenn + 'https://github.com/LEGEND-SY' + at)
	os._exit(1)


def random_choices() : #THE TIPS 
    with open(path + '/random.txt') as f :
        for i in f :
                print (gold + 'Tips :' + at + goldn +  i.split('-')[random.randrange(0 , 4)] + at , goldn + i.split('-')[random.randrange(5 , 8)] + at )
                print('\n')


def Assistant1() : #ASSISTANT SCREEN WITH THE USER NAME
    try :
        with open(path + '/Info.txt' , 'r') as r :
	               for line in r :
	                   line = line.split()
    except :
        pass
    C()
    news()
    random_choices()
    z = input (red + 'Hi ' + black + line[0]  + red + ', How can I help for you?' + at + '' + black + ' (•‿•) ' + at + ':' + black.rjust(0))
    chooseServer(z)


'''_________TOOOOOOLLLLLLLS___________'''
def chooseServer(z) : #THE COMMAND ANSWER
  
    with open (path + '/Info.txt' , 'r') as r :
        for line in r :
            line = line.split()
    if z == 'q' :
        Quit(z)
        
    elif z == 'LEGEND' :
        self2(z)
		
    elif 'say' in z.lower() : #SAY COMMAND
        z1 = z.replace('say' , '')
        point()
        print(black + z1 , ':)' + at)
        reAssistant2()

    elif 'weather' in z.lower() : #--SCRIPT-- WEATHER
        point()
        url = 'http://api.openweathermap.org/data/2.5/weather?q='+ line[4] + '&APPID=0c42f7f6b53b244c78a418f4f181282a&units=metric'
        r = requests.get(url, allow_redirects=True)
        open( path + '/weather.txt' , 'wb').write(r.content) #PUT THE WEATHER INFORMATION TO A FILE
        with open(path + '/weather.txt') as y :
            for i in y :
               i = eval(i) #FILTER THE INFORMATION
               print('Accourding to openWeatherMap :')
               print(v)
               print('In' , i['name'] , '-' , i['sys']['country'])
               print('- The Temperature :' , int(i['main']['temp']) , 'C°')
               print('- Feels like :' , int(i['main']['feels_like']) , 'C°')
               print('- Description :' , i['weather'][0]['description'])
               print('- Humidity :' , i['main']['humidity'] , '%')
               reAssistant2()
	    
    elif 'search' in z.lower() : #WIKIPEDIA COMMAND
            def listToString(s):
                try:
                    s.remove('search')
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
            
            
    elif 'contact' in z.lower() : # CONTACT COMMMAND
        point()
        contact_us()
        reAssistant2()
	      
    elif 'calculator' in z.lower() : #CALCULATOR COMMAND
        point()
        calculator()
        reAssistant2()
    
    elif 'settings' in z.lower() : #TEST
        point()
        print('Comming Soon...')
        reAssistant2()
        
    elif 'youtu' in z.lower() : #--SCRIPT-- YOUTUBE DOWNLOADER
        point()
        try :
            video = pafy.new(z)
            audiostreams = video.audiostreams #AUDIO TYPE
            point()
            print('The file is begin downloading...')
            print(v)
            audiostreams[2].download() #DOWNLOAD THE AUDIO
        except :
            pass
            point()
            print(black + 'An error was detected with your url , please try again!  v_v')
            reAssistant2()
        C()
        print(greenn + 'Download Sucsess! └|∵|┐ ' + at)
        T(1)
        print('Your file is saved in' ,redn + path + at)
        T(5)
        reAssistant2()
    
    elif 'game' in z.lower() : #GAME CENTER COMMAND , CHOOSE THE GAME
       # rps() , randgame()
       point()
       print('Welcome to game center'.rjust(44))
       print('__________________________________________'.rjust(54))
       T(1)
       print(blue + '\n1. randgame\n')
       print('2. Rock Paper Scissors\n')
       print('3. Quit')
       print(v)
       choose = input(red + '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ' + at + ' : ' + black)
       if choose == '1' :
           point()
           randgame()
       elif choose == '2' :
           point()
           rps()
       elif choose == '3' :
           point()
           Assistant2()
       else :
           point()
           print('Wrong choose , try again')
           reAssistant2()
    
    elif 'translate' in z.lower() : #--SCRIPT-- TRANSLATE
        point()
        z = z.lower()
        z1 = z.split()
        z2 = z1[-1] #Language
        z3 = z1[-2] #Before the Language letter (in / to)
        
        def listToString(s):
            s.remove('translate')
            s.remove(z2)
            if 'to' in z3.lower() or 'in' in z3.lower() :
                s.remove(z3)
            str1 = ""
            for ele in s:  
                str1 +=' ' + ele
            return str1 
        s = z.split()
        translator = Translator()
        try :
            translations = translator.translate([listToString(s)], dest=z2)
            for translation in translations:
                print(black + translation.text + at)
            reAssistant2()
        except :
            print('An error has detected please try again!')
            T(0.5)
            print(gold + 'Tip : you should write "translate" then the words you want to translate then the language , EX : translate i love cheess in german ')
            reAssistant2()
            
    elif 'restart' in z.lower() :
        print(at)
        C()
        loading('restart' , 'red')
        T(3)
        C()
        T(1)
        Go()
        
    else : #Q&A COMMAND
        self(z)
        
        
def Assistant2() : #ASSISTANT SCREEN WITHOUT THE USER NAME
     x = ['⊂•⊃_⊂•⊃ ' , '(⊙_◎) ' , '(″･ิ_･ิ)っ ' , '●_● ' , '(◕‿◕✿) ' , '( ･_･)♡ ' , '(◠﹏◠✿) ' , 'ヽ(‘ ∇‘ )ノ ' , '≧◡≦ ' , '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ' , '◕ ◡ ◕ ' , '(¬‿¬) ' , '(^з^)-☆ ' , '(⌒o⌒) ' , '^‿^ ' ]
     random_choices()
     z = input(fg(random.randrange(2)) + bg('white') + x[random.randrange(14)] + at + black +' : ')
     chooseServer(z)


def check_if_not_first_start() :
    try :
        with open( user , 'r') as ru :
    	        if True :
    	            first_start()
    except:
    	with open(user , 'a+') as rus :
            c = str('StartUp') + ' ' + str('StartUp\n')
            rus.write( c )
		     
					        
def news() :
	        greenn = fg('green')
	        at = attr('reset')
	        url = "https://raw.githubusercontent.com/LEGEND-SY/PYTHON-PROJECTS/master/LEGEND-ASSISTANT/News.txt"
	        try :
	            loading_stop('Verification'.rjust(37)+'...')
	            r = requests.get(url, allow_redirects=True)
	            open(path + '/News.txt' , 'wb').write(r.content)
	        except :
	            C()
	            #os._exit(1)
	        C()
	        #loading()
	        with open(path + '/News.txt') as f :
	            for i in f :
	                print(greenn + i.rjust(1) + at)
					        
					        
def Info() :
    x = 15
    y = 5
    while x < 344 :
        string =fg(int(x / 5)) + bg(int(x / 5)) + 'dffyysdx' + attr('reset')
        print(string.rjust(x + y))
        print(string.rjust(x + y))
        print(string.rjust(x + y))
        print(string.rjust(x + y))
        print(string.rjust(x + y))
        print(string.rjust(x + y))
        print(string.rjust(x + y))
        print(string.rjust(x + y))
        print(string.rjust(x + y))
        print(string.rjust(x + y))
        print(string.rjust(x + y))
        print(string.rjust(x + y))
        C()
        x += 1
        y += 5
    xx = fg('black') + bg('white') + 'WELCOME TO LEGEND ASSISTANT'
    xxx = 20
    print('\n' *20 , xx.rjust(64) + attr('reset'))
    T(4)
    C()
    while True :
        print('\n' *xxx , xx.rjust(64) + attr('reset'))
        T(0.005)
        C()
        xxx += -1
        if xxx == 0 :
            break        
    u = '__________________________________________'.rjust(54)
    def Assist(self) :
        ix = 232
        while ix < 255 :   
            print('\n' *xxx , xx.rjust(64) + attr('reset'))
            print(u)
            print(fg(232) +bg(ix) + '\n' + self + attr('reset'))
            T(0.005)
            C()
            ix +=1
            if ix == 255 :
                uu = print('\n' *xxx , xx.rjust(64) + attr('reset'))
                print(u)
                x = input(fg(232) +bg(255) + '\n' + self)
                print(attr('reset'))
                C()
                with open(path + '/Info.txt' , 'a') as f :
                    f.write(x + ' , ')
    
    Assist('Your first name :')
    Assist('Your last name :')
    Assist('Your country :')
    C()


def first_start() :
    with open (user , 'r') as o :
        for line in o :
            if 'StartUp' in line :
                try :
                    open(path + '/Info.txt' , 'r')
                except:
                    Info()
        
def Go() :
    try :
        legend_assistant()
    except :
             C()
             loading_stop('OFFLINE MODE!'.rjust(40))
             T(3)
             loading('loading' , 'yellow')
             C()
             try :
                 Assistant1()
             except :
                     chooseServer('.')
                     
    first_start()
    check_if_not_first_start()
    try :
        Assistant1()
    except :
        point()
        print (redn +"An error was detected !  v_v")
        T(2)
        print( "The system is now trying to Find the error...")
        T(5)
        point()
        print (black + "Please do not use this question at this time" + at)
        T(2)
        reAssistant2()
        
Go()
