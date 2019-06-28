def main ():

  import re
  import random
  import time

#dit zijn de woorden
  counter = 0
  woorden = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]


  print("Laten we beginnen!")
#naam invoegen
  name = input("Hoi, hoe heet je?\n")


#het woord wordt random uit de woordenlijst gehaald 
  woord = random.choice(woorden)
  lengtewoord = len(woord)
  temp = "-" * lengtewoord


  if name == "Thanos" or name == "thanos": 

    print(name + ": I am inevitable.")
    time.sleep(2)
    print("*Snaps fingers*")
    time.sleep(2)
    quit()

#of je wel galgje wilt spelen of niet
  while True:
    choice = input("Wil je galgje spelen?\n")

    if choice == "JA" or choice == "Ja" or choice == "ja":
      break      
    elif choice == "NEE" or choice == "Nee" or choice == "nee":
            quit("Jammer.")
    else:
        print("Antwoord alsjeblieft alleen met ja of nee :)")
        continue

#introductie       
  print("Hallo " + name + ", we spelen het spel galgje, raad letters één voor één en als je het woord weet kan je het als geheel typen! Gebruik alleen kleine letter :)")
  time.sleep(1)
  print("Je hebt 5 levens!")
  print("het woord heeft " + str(lengtewoord) + " letters")
