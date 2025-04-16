15. The Cyclone

height= int(input("How tall are you in centimeters?"))  #Answer determines height value
credits= int(input("How many credits do you have?")) #Answer determines amount of credits

if height > 136 and credits > 9:
  print("Enjoy the ride!")
elif height >136 and credits < 10:
  print("You do not have enough credits.")
elif height < 137 and credits > 9:
  print("You are not tall enough.")
else:
  print("You have not met either requirement")