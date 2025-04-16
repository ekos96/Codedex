#The Sorting Hat 

# This is a simple program that sorts you into one of the four Hogwarts houses based on your answers to a few questions.
# The houses are Gryffindor, Slytherin, Hufflepuff, and Ravenclaw.
# Each house has its own characteristics and values, and the Sorting Hat will determine which house suits you best.
# The program will ask you a series of questions and based on your answers, it will calculate your score for each house.
# At the end, it will tell you which house you belong to.
# The program uses if-elif statements to determine the house based on the answers given.
# The program also includes error handling for invalid inputs.


Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("The Sorting Hat will now ask some questions to determine your house!")

Q1= int(input("Q1) Do you like Dawn or Dusk? \n    1)Dawn \n    2)Dusk \n    Answer:"))

if Q1 == 1: 
  Gryffindor = Gryffindor +1
  Ravenclaw = Ravenclaw +1
elif Q1 == 2:
  Hufflepuff = Hufflepuff +1
  Slytherin = Slytherin +1
else:
  print("Wrong input.")

Q2= int(input("Q2) When I´m dead, i want people to remember me as: \n    1) The Good \n    2)The Great \n    3) The Wise \n    4) The Bold \n    Answer:"))

if Q2 == 1:
  Hufflepuff = Hufflepuff +2
elif Q2 == 2:
  Slytherin = Slytherin +2
elif Q2 == 3:
  Ravenclaw = Ravenclaw +2
elif Q2 == 4:
  Gryffindor = Gryffindor +2
else:
  print("Wrong input.)")

Q3= int(input("Q3) Which kind of instrument most pleases your ear? \n    1) The violin \n    2) The trumpet \n    3) The piano \n    4) The drum \n    Answer:"))

if Q3 == 1:
  Slytherin = Slytherin +4
elif Q3 == 2:
  Hufflepuff = Hufflepuff +4
elif Q3 == 3:
  Ravenclaw = Ravenclaw +4
elif Q3 == 4:
  Gryffindor = Gryffindor +4
else:
  print("Wrong input." + "\n" ) 


print("Gryffindor: " + str(Gryffindor) + "\n")  #"\n" für Zeilensprünge; str(Gryffindor) wandelt in string um --> nennt sich "casten"; statt "str" geht auch "int()" um eine Zahl zu erstellen
print("Ravenclaw: " + str(Ravenclaw) + "\n") 
print("Hufflepuff: " + str(Hufflepuff) + "\n")
print("Slytherin: " + str(Slytherin) + "\n")

if (Gryffindor > Slytherin) and (Gryffindor > Hufflepuff) and (Gryffindor > Ravenclaw) :
  print("You belong in ... Gryffindor!")
elif (Slytherin > Gryffindor) and (Slytherin > Hufflepuff) and (Slytherin > Ravenclaw) :
  print("You belong in ... Slytherin!")
elif (Hufflepuff > Slytherin) and (Hufflepuff > Gryffindor) and (Hufflepuff > Ravenclaw) :
  print:("You belong in ... Hufflepuff!")
elif (Ravenclaw > Gryffindor) and (Ravenclaw > Slytherin) and (Ravenclaw > Hufflepuff):
  print("You belong in ... Ravenclaw!")
