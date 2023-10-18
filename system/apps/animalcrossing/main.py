import os
import random
import sys
import time

from termcolor import colored

printslowon="true"
def print_slow(str, interval = 0.07):
  if printslowon=="true":
    for letter in str:
        #print(letter, end='')
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(interval)
    print('')
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

fishtiempo = 0
fishtiempocount = 0

size = 0
sizeword = 0
check = 0
dovariation = 0
variationcolor = 0
sizemultiplier = 0

def sizepick():
  global size
  global sizeword
  global check
  global sizemultiplier
  sizemultiplier = 1
  size = random.randint(1, 4)
  if size==1:
    sizeword = "small"
    sizemultiplier=1.00

  if size==2:
    check = random.randint(1,2)
    if check==1:
      sizeword = "medium"
      sizemultiplier=1.50
    else:
      sizepick()
      
  if size==3:
    check = random.randint(1,4)
    if check==1:
      sizeword = "large"
      sizemultiplier=2.00
    else:
      sizepick()
      
  if size==4:
    check = random.randint(1,8)
    if check==1:
      sizeword = "huge"
      sizemultiplier=4.00
    else:
      sizepick()

def shopline():
  check = random.randint(1,5)
  if check==1:
    print_slow(colored("Ankha: Hello! Welcome to the shop!", "yellow"))
  
  if check==2:
    print_slow(colored("Ankha: Hi! Welcome to my shop!", "yellow"))
  
  if check==3:
    print_slow(colored("Ankha: Aloha! Welcome to the shop we have everything from Pineapples to Fishing Lines!", "yellow"))

  if check==4:
    print_slow(colored("Ankha: Hey! Welcome to the shop!", "yellow"))
  
  if check==5:
    print_slow(colored("Ankha: Welcome in!", "yellow"))
  
  if check==6:
    print_slow(colored("Ankha: Howdy!", "yellow"))

  if check==7:
    print_slow(colored("Ankha: Make sure to leave us a review!", "yellow"))
  
  if check==8:
    print_slow(colored("Ankha: Welcome to the store!", "yellow"))
  
  if check==9:
    print_slow(colored("Ankha: Welcome Ankha's Surplus!", "yellow"))
    
  if check==10:
    print_slow(colored("Ankha: Hello! Welcome in!", "yellow"))

def imblue():
  print_slow(colored("Yo, listen up here's a story", "blue"))
  print_slow(colored("About a little guy", "blue"))
  print_slow(colored("That lives in a blue world", "blue"))
  print_slow(colored("And all day and all night", "blue"))
  print_slow(colored("And everything he sees is just blue", "blue"))
  print_slow(colored("Like him inside and outside", "blue"))
  print_slow(colored("Blue his house", "blue"))
  print_slow(colored("With a blue little window", "blue"))
  print_slow(colored("And a blue corvette", "blue"))
  print_slow(colored("And everything is blue for him", "blue"))
  print_slow(colored("And himself and everybody around", "blue"))
  print_slow(colored("Cause he ain't got nobody to listen to", "blue"))
  print_slow(colored("I'm blue", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("I'm blue", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("I have a blue house", "blue"))
  print_slow(colored("With a blue window", "blue"))
  print_slow(colored("Blue is the colour of all that I wear", "blue"))
  print_slow(colored("Blue are the streets", "blue"))
  print_slow(colored("And all the trees are too", "blue"))
  print_slow(colored("I have a girlfriend and she is so blue", "blue"))
  print_slow(colored("Blue are the people here", "blue"))
  print_slow(colored("That walk around", "blue"))
  print_slow(colored("Blue like my corvette its in and outside", "blue"))
  print_slow(colored("Blue are the words I say", "blue"))
  print_slow(colored("And what I think", "blue"))
  print_slow(colored("Blue are the feelings", "blue"))
  print_slow(colored("That live inside me", "blue"))
  print_slow(colored("I'm blue", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("I'm blue", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("I have a blue house"), "blue")
  print_slow(colored("With a blue window", "blue"))
  print_slow(colored("Blue is the colour of all that I wear", "blue"))
  print_slow(colored("Blue are the streets", "blue"))
  print_slow(colored("And all the trees are too", "blue"))
  print_slow(colored("I have a girlfriend and she is so blue", "blue"))
  print_slow(colored("Blue are the people here", "blue"))
  print_slow(colored("That walk around", "blue"))
  print_slow(colored("Blue like my corvette, its in and outside", "blue"))
  print_slow(colored("Blue are the words I say", "blue"))
  print_slow(colored("And what I think", "blue"))
  print_slow(colored("Blue are the feelings", "blue"))
  print_slow(colored("That live inside me", "blue"))
  print_slow(colored("I'm blue", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("I'm blue", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))
  print_slow(colored("Da ba dee da ba di", "blue"))

tempbells = 0
buginventory=["No bugs"]
foodlist=["PB&J"]
def bugpick():
  sizepick()
  global tempbells
  check = buginventory.count("No bugs")
  if check == "No Bugs":  
    buginventory.remove("No bugs")
    
  if check==1:
      bug = (colored("Ant", "green"))
      tempbells=tempbells+(2*sizemultiplier)
      buginventory.append(" Ant")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==2:
      bug = (colored("Beetle", "green"))
      tempbells=tempbells+(3*sizemultiplier)
      buginventory.append(" Beetle")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==3:
      bug = (colored("Flea","green"))
      tempbells=tempbells+(2*sizemultiplier)
      buginventory.append(" Flea")
      print_slow("You caught a " + bug)
      exploreagain()
  
  if check==4:
      bug = (colored("Moth", "blue"))
      tempbells=tempbells+(3*sizemultiplier)
      buginventory.append(" Moth")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==5:
      bug = (colored("Dragonfly", "yellow"))
      tempbells=tempbells+(5*sizemultiplier)
      buginventory.append(" Dragonfly")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==6:
      bug = (colored("Wasp","magenta"))
      tempbells=tempbells+(3*sizemultiplier)
      buginventory.append(" Wasp")
      print_slow("You caught a " + bug)
      exploreagain()
  
  if check==7:
      bug = (colored("Cockroach", "yellow"))
      tempbells=tempbells+(1.5*sizemultiplier)
      buginventory.append(" Cockroach")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==8:
      bug = (colored("Lice", "yellow"))
      tempbells=tempbells+(1*sizemultiplier)
      buginventory.append(" Lice")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==9:
      bug = (colored("Cricket", "blue"))
      tempbells=tempbells+(5*sizemultiplier)
      buginventory.append(" Cricket")
      print_slow("You caught a " + bug)
      exploreagain()
  
  if check==10:
      bug = (colored("Termite", "red"))
      tempbells=tempbells+(3*sizemultiplier)
      buginventory.append(" Termite")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==11:
      bug = (colored("Fly", "green"))
      tempbells=tempbells+(1*sizemultiplier)
      buginventory.append(" Fly")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==12:
      bug = (colored("Spider", "red"))
      tempbells=tempbells+(3*sizemultiplier)
      buginventory.append(" Spider")
      print_slow("You caught a " + bug)
      exploreagain()
  
  if check==13:
      bug = (colored("Bee", "red"))
      tempbells=tempbells+(5*sizemultiplier)
      buginventory.append(" Bee")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==14:
      bug = (colored("Firefly", "blue"))
      tempbells=tempbells+(0.5*sizemultiplier)
      buginventory.append(" Firefly")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==15:
      bug = (colored("Grasshopper", "red"))
      tempbells=tempbells+(5*sizemultiplier)
      buginventory.append(" Grasshopper")
      print_slow("You caught a " + bug)
      exploreagain()
  
  if check==16:
      bug = (colored("Stickbug", "blue"))
      tempbells=tempbells+(2.5*sizemultiplier)
      buginventory.append(" Stickbug")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==17:
      bug = (colored("Earwig", "blue"))
      tempbells=tempbells+(2.5*sizemultiplier)
      buginventory.append(" Earwig")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==18:
      bug = (colored("Waterbug", "red"))
      tempbells=tempbells+(4*sizemultiplier)
      buginventory.append(" Waterbug")
      print_slow("You caught a " + bug)
      exploreagain()
  
  if check==19:
      bug = (colored("Praying Mantis",  "red"))
      tempbells=tempbells+(4*sizemultiplier)
      buginventory.append(" Praying Mantis")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==20:
      bug = (colored("Butterfly", "red"))
      tempbells=tempbells+(2*sizemultiplier)
      buginventory.append(" Butterfly")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==21:
      bug = (colored("Centipede", "green"))
      tempbells=tempbells+(2*sizemultiplier)
      buginventory.append(" Centipede")
      print_slow("You caught a " + bug)
      exploreagain()
  
  if check==22:
      bug = (colored("Mosquitoe", "green"))
      tempbells=tempbells+(1.5*sizemultiplier)
      buginventory.append(" Mosquitoe")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==23:
      bug = (colored("Locust", "green"))
      tempbells=tempbells+(3*sizemultiplier)
      buginventory.append(" Locust")
      print_slow("You caught a " + bug)
      exploreagain()
    
  if check==24:
      bug = (colored("Gnat", "blue"))
      tempbells=tempbells+(2*sizemultiplier)
      buginventory.append(" Gnat")
      print_slow("You caught a " + bug)
      exploreagain()
    
check=0

def exploreagain():
  print_slow("Would you like to keep exploring? [Y/N]")
  check=input("")
  if check=="y" or check=="Y" or check=="yes" or check=="Yes":
    time.sleep(1)
    screen_clear()
    explore()
  if check=="n" or check=="N" or check=="no" or check=="No":
    time.sleep(1)
    screen_clear()
    options()
    
def foodpick():
  check=random.randint(1, 20)
  
  if check==1:
    foodlist.append(" Apple")
    print_slow("You found an apple!")
    exploreagain()

  if check==2:
    foodlist.append(" Pear")
    print_slow("You found an pear!")
    exploreagain()

  if check==3:
    foodlist.append(" Carrot")
    print_slow("You found an carrot!")
    exploreagain()

  if check==4:
    foodlist.append(" Beetroot")
    print_slow("You found an beetroot!")
    exploreagain()

  if check==6:
    foodlist.append(" Orange")
    print_slow("You found an orange!")
    exploreagain()

  if check==7:
    foodlist.append(" Lemon")
    print_slow("You found a lemon!")
    exploreagain()

  if check==8:
    foodlist.append(" Blackberry")
    print_slow("You found a blackberry!")
    exploreagain()

  if check==9:
    foodlist.append(" Raspberry")
    print_slow("You found a raspberry!")
    exploreagain()

  if check==10:
    foodlist.append(" Lychee")
    print_slow("You found an Lychee!")
    exploreagain()

  if check==11:
    foodlist.append(" Apricot")
    print_slow("You found an apricot!")
    exploreagain()

  if check==12:
    foodlist.append(" Blueberry")
    print_slow("You found a blueberry!")
    exploreagain()

  if check==13:
    foodlist.append(" Cacao")
    print_slow("You found a Cacao!")
    exploreagain()

  if check==14:
    foodlist.append(" Dragonfruit")
    print_slow("You found a dragonfruit!")
    exploreagain()

  if check==15:
    foodlist.append(" Fig")
    print_slow("You found a fig!")
    exploreagain()

  if check==16:
    foodlist.append(" Carrot")
    print_slow("You found an carrot!")
    exploreagain()

  if check==17:
    foodlist.append(" Guava")
    print_slow("You found a guava!")
    exploreagain()

  if check==18:
    foodlist.append(" Strawberry")
    print_slow("You found a strawberry!")
    exploreagain()

  if check==19:
    foodlist.append(" Pineapple")
    print_slow("You found a pineapple!")
    exploreagain()

  if check==20:
    foodlist.append(" Passionfruit")
    print_slow("You found a passionfruit!")
    exploreagain()
    
name="filler"
check=0
exploring=0
fishtiempo = random.randint(1, 10)
def explore():
  screen_clear()
  check=0
  exploring=0
  fishtiempo = random.randint(1, 10)
  caught="false"
  while caught=="false":
    fishtiempocount = 0
    if int(fishtiempocount)>=int(fishtiempo):
      caught="true"
    else:
      screen_clear()
      print_slow("Exploring.")
      time.sleep(1)
      fishtiempocount = int(fishtiempocount) + 1
      screen_clear()  

    check=random.randint(1,2)
    if check==1:
      bugpick()
    if check==2:
      foodpick()
  

isvariation="false"
variationmultiplier=0

def variation():
  global dovariation
  global variationcolor
  global isvariation
  global variationmultiplier
  dovariation=random.randint(1,20)
  if dovariation==1:
    isvariation="true"
    variationcolor = random.randint(1,10)

    if variationcolor==1:
      variationcolor = "red"
      
    if variationcolor==2:
      variationcolor = "magenta"
      
    if variationcolor==3:
      variationcolor = "yellow"
      
    if variationcolor==4:
      variationcolor = "green"
      
    if variationcolor==5:
      variationcolor = "blue"
      
    if variationcolor==6:
      variationcolor = "pruple"
      
    if variationcolor==7:
      variationcolor = "slimy"
      
    if variationcolor==8:
      variationcolor = "three eyed"
        
    if variationcolor==9:
      variationcolor = "bloated"
      
    if variationcolor==10:
      variationcolor = "talking"

  else:
    isvariation="false"

def fishpick():
  sizepick()
  variation()

speechline="0"

def speechlines():
  check=random.randint(1,8)
  global speechline
  
  if check==1:
    speechline=(name + ": I will lower the taxes!")

  if check==2:
    speechline=(name + ": Today we will be watching the  world renound Bee movie. But first I have a question. You like jazz?")

  if check==3:
    speechline=(name + ": Hello, villagers! Today I will be legalizing tax evasion!")

  if check==4:
    speechline=(name + ": TWIGS FOR EVERYONE")

  if check==5:
    speechline=(name + ": I like pizza")

  if check==6:
    speechline=(name + ":")

  if check==7:
    speechline=(name + ":")

  if check==8:
    speechline=(name + ":")
    
name="0"
donatebells=0
bells=5.00

def villagerspeech():
  global donatebells
  global bells
  speechlines()
  print_slow(speechline)
  print_slow(colored("Villagers: *CHEERING*", "blue"))
  print_slow(colored("The Villagers love you!", "blue"))
  check=random.randint(1,8)
  donatebells=random.randint(1,50)
  if check==1:
    print_slow(colored("One of them even gave you " + str(donatebells) + " dollars! They must really love you", "blue"))
    bells = bells + donatebells
  check=random.randint(1,4)
  if check==1:
    print_slow("As you walk off stage, you still hear them cheering and chanting your name.")
    print_slow("More content, you go back to your mayor-ly duties.")
  time.sleep(1)
  screen_clear()
  options()

basicrod = "1. Basic Rod 100 Bells"
avgrod = "2. Average Rod 500 Bells"
goodrod = "3. Good Rod 2000 Bells"
bestrod = "4. Best Rod 4000 Bells"

fishspeed=1

basicrodpurchase = "false"
avgrodpurchase = "false"
goodrodpurchase = "false"
bestrodpurchase = "false"
rodpurchase=0
shopitem=0

def shop():
  global bells
  global basicrod
  global avgrod
  global goodrod
  global bestrod
  global basicrodpurchase
  global avgrodpurchase
  global goodrodpurchase
  global bestrodpurchase
  global rodpurchase
  global fishspeed
  global shopitem
  screen_clear()
  print_slow("bells: $" + str(bells))
  print_slow("\n")
  shopline()
  print_slow(colored("Ankha: What are you shopping for? Just tell me with numbers 1. Fishing Rods or 2. Food", "yellow"))
  print_slow(colored("Ankha: or type 'exit' to leave the shop.", "yellow"))
  shopitem=input("")
  if shopitem=="1":
    print_slow("\n")
    print_slow(basicrod + " | " + avgrod + " | " + goodrod + "|" + bestrod + " |")
    print_slow(colored("Ankha: Type the number of what you would like to purchase.", "yellow"))
    print_slow(colored("Ankha: Or type 'exit' to do something else.", "yellow"))
    rodpurchase = input("")
    
    if rodpurchase=="1":
      if basicrodpurchase=="false":
        if int(bells)>=100:
          bells = int(bells) - 100
          basicrod = "1. Basic Rod (OWNED)"
          basicrodpurchase="true"
          print_slow(colored("Ankha: Good choice for a beginner! Here you go!", "yellow"))
          time.sleep(1)
          screen_clear()
          shop()
          fishspeed=0.75
        else:
          print_slow(colored("Ankha: You don't have enough Bells!", "yellow"))
          time.sleep(1)
          shop()
      else:
        print_slow(colored("Ankha: You already own this rod!", "yellow"))
        time.sleep(1)
        screen_clear()
        shop()
  
      
    if rodpurchase=="2":
      if avgrodpurchase=="false":
        if int(bells)>=500:
          bells = int(bells) - 500
          avgrod = "2. Average Rod (OWNED)"
          avgrodpurchase="true"
          print_slow(colored("Ankha: Here's the Average Rod!", "yellow"))
          time.sleep(1)
          screen_clear()
          shop()
          fishspeed=0.5
        else:
          print_slow(colored("Ankha: You don't have enough Bells!", "yellow"))
          time.sleep(1)
          shop()
      else:
        print_slow(colored("Ankha: You already own this rod!", "yellow"))
        screen_clear()
        time.sleep(1)
        shop()
  
      
    if rodpurchase=="3":
      if goodrodpurchase=="false":
        if int(bells)>=2000:
          bells = int(bells) - 2000
          goodrod = "3. Good Rod (OWNED)"
          goodrodpurchase="true"
          print_slow(colored("Ankha: Ooooh As the name suggests, it is a Good Rod!", "yellow"))
          time.sleep(1)
          screen_clear()
          shop()
          fishspeed=0.25
        else:
          print_slow(colored("Ankha: You don't have enough Bells!", "yellow"))
          time.sleep(1)
          shop()
      else:
        print_slow(colored("Ankha: You already own this rod!", "yellow"))
        time.sleep(1)
        screen_clear()
        shop()
  
      
    if rodpurchase=="4":
      if bestrodpurchase=="false":
        if int(bells)>=4000:
          bells = int(bells) - 4000
          bestrod = "4. Best Rod (OWNED)"
          bestrodpurchase="true"
          print_slow(colored("Ankha: This one is the absolute best for fishing. You can take the one in the case over there.", "yellow"))
          time.sleep(1)
          screen_clear()
          shop()
          fishspeed=0.1
        else:
          print_slow(colored("Ankha: You don't have enough Bells!", "yellow"))
          time.sleep(1)
          shop()
      else:
        print_slow(colored("Ankha: You already own this rod!", "yellow"))
        time.sleep(1)
        screen_clear()
        shop()
  
    if rodpurchase=="exit":
      print_slow(colored("Ankha: See you next time!", "yellow"))
      screen_clear()
      options()
  
    else:
      print_slow(colored("Ankha: Sorry I didn't get that. Tell me again please.", "yellow"))
      shop()

  if shopitem=="2":
    print_slow(colored("Ankha: Yeah, I'm hungry too.", "yellow"))
    print_slow("1. Donut 2 Bells | 2. Pizza 10 Bells | 3. Pineapple 8 Bells| 4. PB&J 3 Bells |")
    print_slow(colored("Ankha: What would you like? (Type the number)", "yellow"))
    print_slow(colored("Ankha: Or type 'exit' to exit the shop.", "yellow"))
    check=input("")
    if check=="1":
      if bells >= 2:
        bells=bells-2
        print_slow(colored("Ankha: Enjoy!", "yellow"))
        foodlist.append(" Donut")
        time.sleep(1)
        screen_clear()
        shop()

      if bells < 2:
        print_slow(colored("Ankha: You don't have enough Bells!", "yellow"))
        time.sleep(1)
        shop()

    if check=="2":
      if bells >= 10:
        bells=bells-10
        print_slow(colored("Ankha: Mmmm...I love pizza!", "yellow"))
        foodlist.append(" Pizza")
        time.sleep(1)
        screen_clear()
        shop()

      if bells < 10:
        print_slow(colored("Ankha: You don't have enough Bells!", "yellow"))
        time.sleep(1)
        screen_clear()
        shop()
      

    if check=="3":
      if bells >= 8:
        bells=bells=8
        print_slow(colored("Ankha: To be honest, pineapple hurts my mouth.", "yellow"))
        foodlist.append(" Pineapple")
        time.sleep(1)
        screen_clear()
        shop()

      if bells < 8:
        print_slow(colored("Ankha: You don't have enough Bells!", "yellow"))
        time.sleep(1)
        screen_clear()
        shop()

    if check=="4":
      if bells >= 3:
        bells=bells-3
        print_slow(colored("Ankha: I love PB&Js!", "yellow"))
        foodlist.append(" PB&J")
        time.sleep(1)
        screen_clear()
        shop()

      if bells < 3:
        print_slow(colored("Ankha: You don't have enough Bells!", "yellow"))
        time.sleep(1)
        screen_clear()
        shop()

  if shopitem=="exit":
    print_slow(colored("Ankha: See you next time!", "yellow"))
    time.sleep(1)
    screen_clear()
    options()
    
  else:
      print_slow(colored("Ankha: Sorry I didn't get that. Tell me again please.", "yellow"))
      time.sleep(1)
      screen_clear()
      shop()
      
ifnotaction1="1"
ifnotaction2="2"
ifnotaction3="3"
ifnotaction4="4"
ifnotaction5="5"
ifnotaction6="6"
ifnotaction7="7"
ifnotaction8="8"
ifnotaction9="9"
ifnotaction10="10"
fish="filler"
fishnum=0

#when done duplicate game but make print fast

fishinventory=["No Fish"]
def options():
  global fishtiempo
  global fishtiempocount
  global caught
  global tempbells
  global bells
  global fishnum
  print_slow("Type the number of what you would like to do.")
  print_slow(colored("1. Go fishing", "blue"))
  print_slow(colored("2. Sell your fish and bugs", "green"))
  print_slow(colored("3. Go to the shop", "yellow"))
  print_slow(colored("4. Talk to villagers", "blue"))
  print_slow(colored("5. Eat lunch", "red"))
  print_slow(colored("6. View your inventory", "magenta"))
  print_slow(colored("7. Go to K.K Slider's Concert", "green"))
  print_slow(colored("8. Go exploring", "blue"))
  print_slow(colored("9. Settings BROKEN", "black"))
  action = input("")
  if action=="1":
    fishing()
  if  action=="2":
    print_slow("Sold!")
    bells=bells+tempbells
    print_slow("You now have $" + str(bells))
    fishinventory.clear()
    time.sleep(1)
    screen_clear()
    tempbells=0
    fishinventory.append("No Fish")
    buginventory.append("No Bugs")
    options()

  if action=="3":
    shop()

  if action=="4":
    villagerspeech()

  if action=="5":
    screen_clear()
    if 'PB&J' in foodlist:
      print_slow("Luckily, Mom packed you a PB&J!")
      print_slow("You chow down...mmmm...It was super good!")
      foodlist.remove("PB&J")
      time.sleep(1)
      screen_clear()
      options()

    if not bool(foodlist):
      print_slow("You have no food to eat!")
      time.sleep(1)
      screen_clear()
      options()

    else:
      foodeat = random.choice(foodlist)
      print_slow("You have a " + str(foodeat))
      print_slow("Yum. It was SO good!")
      foodlist.remove(foodeat)
      time.sleep(1)
      screen_clear()
      options()

    if not bool(foodlist):
      print_slow("You don't have any food!.")
      time.sleep(1)
      screen_clear()
      options()

  if action=="6":
    screen_clear()
    foodininventory="true"
    fishininventory="true"
    bugsininventory="true"

    if foodininventory=="true":
      for i in foodlist:  
  
        print("Food:" + i, end=" ")

    if fishininventory=="true":
      for i in fishinventory:  
  
        print("\nFish:" + i, end=" ")

    
    if bugsininventory=="true":
      for i in buginventory:  
  
        print("\nBugs:" + i, end=" ")
      

    check=input("\nType 'exit' to leave.\n")
    if check=="exit" or check=="Exit":
      screen_clear()
      options()
    else:
      print_slow("Sorry, I didn't get that. I'll assume you want to leave.")
      time.sleep(1)
      screen_clear()
      options()

  if action=="7":
    screen_clear()
    print_slow(colored("K.K Slider: Let's get this concert started!", "white"))
    print_slow(colored("K.K Slider: I'll be playing 'I'm Blue'!\n", "white"))
    imblue()
    print_slow("")
    print_slow("Type 'exit' when you're ready to leave.")
    check=input("")
    if check=="exit" or check=="Exit":
      time.sleep(1)
      screen_clear()
      options()

  if action=="8":
    screen_clear()
    print_slow("You begin your exploration of the island")
    time.sleep(1)
    explore()
    
    
  if action=="9":
    print_slow("Hey! I said it was broken! Now go away >:(")
    time.sleep(1)
    screen_clear()
    options()
    
  if not ifnotaction1 and ifnotaction2 and ifnotaction3 and ifnotaction4 and ifnotaction5 and ifnotaction6 and ifnotaction7 and ifnotaction8 and ifnotaction9 and ifnotaction10:
    print_slow("Sorry, invalid input. Try again")
    time.sleep(1)
    screen_clear()
    options()

def fishing():
  global tempbells
  check = fishinventory.count("No fish")
  if check == "No fish":  
    fishinventory.remove("No Fish")
    

  check=random.randint(1,8)
  if check==1:
    print_slow("It's Winter! The water is frozen over, so you can't go fishing!")
    time.sleep(1)
    screen_clear()
    options()

  fishtiempo = random.randint(1, (10 * int(fishspeed)))
  fishtiempocount = 0
  caught="false"
  while caught=="false":
    if int(fishtiempocount)>=int(fishtiempo):
      caught="true"
    else:
      screen_clear()
      print_slow("Fishing.")
      time.sleep(1)
      fishtiempocount = int(fishtiempocount) + 1
      screen_clear()  
      
  if caught=="true":
    fishnum = random.randint(1, 24)
    sizepick()
    variation()
  
    if fishnum==1:
      fish = (colored("Sardine", "green"))
      tempbells=tempbells+(2*sizemultiplier)
      fishinventory.append(" Sardine")
    
    if fishnum==2:
      fish = (colored("Tuna", "green"))
      tempbells=tempbells+(3*sizemultiplier)
      fishinventory.append(" Tuna")
    
    if fishnum==3:
      fish = (colored("Trout","green"))
      tempbells=tempbells+(2*sizemultiplier)
      fishinventory.append(" Trout")
  
    if fishnum==4:
      fish = (colored("Salmon", "blue"))
      tempbells=tempbells+(3*sizemultiplier)
      fishinventory.append(" Salmon")
    
    if fishnum==5:
      fish = (colored("Lionfish", "yellow"))
      tempbells=tempbells+(5*sizemultiplier)
      fishinventory.append(" Lionfish")
    
    if fishnum==6:
      fish = (colored("Blobfish","magenta"))
      tempbells=tempbells+(7*sizemultiplier)
      fishinventory.append(" Blobfish")
  
    if fishnum==7:
      fish = (colored("Hammerhead Shark", "yellow"))
      tempbells=tempbells+(20*sizemultiplier)
      fishinventory.append(" Hammerhead Shark")
    
    if fishnum==8:
      fish = (colored("Great White Shark", "yellow"))
      tempbells=tempbells+(30*sizemultiplier)
      fishinventory.append(" Great White Shark")
    
    if fishnum==9:
      fish = (colored("Catfish", "blue"))
      tempbells=tempbells+(5*sizemultiplier)
      fishinventory.append(" Catfish")
  
    if fishnum==10:
      fish = (colored("Pirhannah", "red"))
      tempbells=tempbells+(3*sizemultiplier)
      fishinventory.append(" Pirhannah")
    
    if fishnum==11:
      fish = (colored("Goldfish", "green"))
      tempbells=tempbells+(1*sizemultiplier)
      fishinventory.append(" Goldfish")
    
    if fishnum==12:
      fish = (colored("Swordfish", "red"))
      tempbells=tempbells+(7*sizemultiplier)
      fishinventory.append(" Swordfish")
  
    if fishnum==13:
      fish = (colored("Pufferfish", "red"))
      tempbells=tempbells+(5*sizemultiplier)
      fishinventory.append(" Pufferfish")
    
    if fishnum==14:
      fish = (colored("Tuna", "blue"))
      tempbells=tempbells+(0.5*sizemultiplier)
      fishinventory.append(" Tuna")
    
    if fishnum==15:
      fish = (colored("Otter", "red"))
      tempbells=tempbells+(10*sizemultiplier)
      fishinventory.append(" Otter")
  
    if fishnum==16:
      fish = (colored("Turtle", "blue"))
      tempbells=tempbells+(25*sizemultiplier)
      fishinventory.append(" Turtle")
    
    if fishnum==17:
      fish = (colored("Seal", "blue"))
      tempbells=tempbells+(18*sizemultiplier)
      fishinventory.append(" Seal")
    
    if fishnum==18:
      fish = (colored("Penguin", "red"))
      tempbells=tempbells+(4*sizemultiplier)
      fishinventory.append(" Penguin")
  
    if fishnum==19:
      fish = (colored("Sea Lion",  "red"))
      tempbells=tempbells+(7*sizemultiplier)
      fishinventory.append(" Sea Lion")
    
    if fishnum==20:
      fish = (colored("Walrus", "red"))
      tempbells=tempbells+(20*sizemultiplier)
      fishinventory.append(" Walrus")
    
    if fishnum==21:
      fish = (colored("Crab", "green"))
      tempbells=tempbells+(2*sizemultiplier)
      fishinventory.append(" Crab")
  
    if fishnum==22:
      fish = (colored("Chunk Of Coral", "green"))
      tempbells=tempbells+(1.5*sizemultiplier)
      fishinventory.append(" Chunk Of Coral")
    
    if fishnum==23:
      fish = (colored("Lobster", "green"))
      tempbells=tempbells+(3*sizemultiplier)
      fishinventory.append(" Lobster")
    
    if fishnum==24:
      fish = (colored("Bass", "blue"))
      tempbells=tempbells+(8*sizemultiplier)
      fishinventory.append(" Bass")
      
  fishpick()
  
  if isvariation=="true":
    print_slow("You caught a " + str(sizeword) + " " + str(variationcolor) + " " + str(fish) + "!")
  
  if isvariation=="false":
    print_slow("You caught a " + str(sizeword) + " " + str(fish) + "!")

  print_slow("Would you like to fish again? [Y/N]")
  again = input("")
  if again=="Y" or again=="y" or again=="Yes" or again=="yes":
    fishing()
  
  if again=="N" or again=="n" or again=="No" or again=="no":
    screen_clear()
    options()

  else:
    print_slow("Sorry, I didn't get that. I'll assume you want to fish again")
    time.sleep(1)
    screen_clear()
    options()

screen_clear()
print_slow(colored("Uknown Person: Hello, and welcome to Animal Crossing!", "black"))
print_slow(colored("Uknown Person: Oh! Sorry, I forgot to introduce my self. Im Tom Nook. A resident of this island.", "black"))
print_slow(colored("Tom Nook: I see you're new here. What's your name?", "black"))
name=input("")
check=random.randint(1,5)
if check==1:
  print_slow(colored("Tom Nook: Cool name, " + name + "!", "black"))

if check==2:
  print_slow(colored("Tom Nook: I've never heard that name before! " + name + "..." + name + "... Well in any case, cool name!", "black"))

if check==3:
  print_slow(colored("Tom Nook: Well that's an odd name!", "black"))

if check==4:
  print_slow(colored("Tom Nook: Wow! I like the name " + name, "black"))

if check==5:
  print_slow(colored("Tom Nook: Well, hello, " + name, "black"))

print_slow(colored("Tom Nook: Well, since you're mayor now, what should the island be named?", "black"))
islandname=input("")
print_slow(colored("Tom Nook: Wow! I think everyone will love the name '" + islandname + "'!", "black"))
print_slow(colored("Tom Nook: Well, I'll leave you to it. Bye!", "black"))
options()  

#add crafting and cutting down trees and stuff
#add homes
#grow plants
#surfing(maybe)
#dodo airlines to go to other islands to get other fish
#musuem for rarest stuff collected owned by blathers
#archeology
#merchants
#cooking
'''
Donating 5 unique fish and insects to Tom Nook will unlock the ability to place Blathers' tent. Once Blathers' tent is unlocked, he will give the player a Vaulting Pole to find more creatures and a shovel to excavate Fossils. Donating 15 more unique creatures and appraised fossils to Blathers will unlock the ability to place his museum, at which the player can donate and assess multiple things at a time. To unlock more tools, the player will need to pay off their tent, help Tom Nook build Nook's Cranny, build one bridge, and start three additional housing plots for animal villagers.
'''