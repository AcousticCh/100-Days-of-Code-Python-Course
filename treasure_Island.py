print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("You awaken in the woods, its midday and with the sun directly above you you cannot differentiate north from south or east from west")
print("Would you rather wait until the sun can offer direction or walk in search of help?")
option1 = input("wait or walk?: ").lower()
if option1 == "wait":
  print("You fall back asleep watching the sun fall slowly. A few hours later your eyes spring open and growls are heard around you, the wolves have you surrounded. It is game over.")
  exit()
else:
  print("You stumble aimlessly through brush and leaves although now you can see a human made structure in the distance.")

print("Would you rather go to the building in search of help or continue walking")
option2 = input("go or walk").lower()

if option2 == "go":
  print("As you step closer you hear a party, final people. In hopes of finding help you join the crowd only to find unwelcoming looks all around.")
  print("The building is a nest of bandits, upon realizing you try to run but one catches the back of your head with a club. You were never heard from again")
  exit()
else:
  print("You wonder if those people back there could have saved you but know its too late now")

print("Darkness begins to swell over the trees you know it will be dangerous if you are stuck here through the night and have to decide on a plan")
print("There is a river you decide to follow, it looks a little grimy.")
print("Would you rather follow the river upstream or downstream")
option3 = input("upstream or downstream").lower()
if option3 == "downstream":
  print("You follow the waters flow to the edge of what you see now to be an island with nothing in sight across ocean")
  print("You think about shelter for the night but you are too hungry to walk any further. Your legs give up and you lay there hungry")
  print("Yur have starved to death, Game Over")
  exit()
else:
  print("you follow the mucky water uphill until you see a giant grate from which the water is coming from, thinking these might be your final moments you climb the grate wall to lay on top and rest, but in front of you a safe town presents itself, you are a survivor")