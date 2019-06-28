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

#als je het woord hebt geraden
  while True:
    user = (input(": "))
   
  
    match = re.search(user, woord)
    if user == woord:
      print("Gefeliciteerd " + name + ', je heb het woord ' + '"' + woord + '"' + " geraden!")
      restart = input("Wil je nog een keer spelen? Antwoord alleen met ja of nee alsjeblieft.")
      if restart == "ja" or restart == "Ja" or restart == "JA":
        main()
      else:
        quit("Jammer.")
    
 #als je een letter goed hebt geraden
    elif match:
      print("Goed geraden " + name + "!" " Als je het woord nu weet, type het woord dan in zijn geheel.")
      for i in range(0, lengtewoord):
       if user == woord[i]:
        temp = temp[:i] + user +temp[i+1:]
      print(temp)

  #als je een letter fout hebt geraden met plaatje van galgje   
    else:
      print("Jammer " + name + ", dat is niet goed.")
      counter = counter + 1
      if counter == 1:
        print("""  
      |
      |
      |
      |
      |
  _____|""")
      elif counter == 2:
             print("""  ____
      |
       |
       |
       |
       |
  _____|""")

      elif counter == 3:
        print("""  ____
    | \|
    0  |
    |  |
       |
       |
  _____|""")

      elif counter == 4:
        print("""  ____
    | \|
    0  |
   /|\ |
       |
       |
  _____|""")

      elif counter ==5:
      
        print("""  ____
    | \|
    0  |
   -|- |
   / \ |
       |
  _____|""")
        print("Helaas, je bent dood :(")
     #je bent dood en laten zien wat het woord was
        print('Het woord was ' + '"' + woord + '"')
        break
      else:
       pass

restart = input("Wil je nog een keer spelen? Antwoord alleen met ja of nee alsjeblieft.")
  if restart == "ja" or restart == "Ja" or restart == "JA":
     main() 
  else:
     quit("Jammer.") 
