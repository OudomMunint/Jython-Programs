#Dev: Oudom munint
#Date: 2020/28/06
#Task: Workout the escape velocity to exit the earths atmosphere then Workout the time it takes to fall in seconds

#Displays the results
def printMsg():
   print("Get(results)")
   

#Call function with an argument
def showName(yourName):
   print(yourName)

#Values of G, M, R, V
#uses these values to compute the escape velocity
def escapeVelocity():
   G = 6.67384E-11
   M = 5.9736E24
   R = 6371000
   V = (2 * G * M)/R
   result = sqrt(V)
   print ("Escape velocity:")
   print (result)

#Time it takes to land 
#value of height per story and total height of building
#Gravity = 9.81m/s
def timeToLand():
   #Variables
   HeightInStories = 3
   feetPerStory = 10
   metersPerfoot = 0.3048
   gravity = 9.81
   
   # Calculates the height in feet
   HeightInFeet = HeightInStories * feetPerStory
   
   # Calculate  the height in meters
   heightInMeters = HeightInFeet * metersPerfoot
   
   # Calculate the time to hit the ground
   timeToFall = sqrt((2*heightInMeters)/gravity)
   
   # Shows the time to fall in seconds
   print("Time ti fall (seconds):")
   print(timeToFall)

#Time it takes to land 
#value of height per story and total height of building
#Gravity = 9.81m/s
#Need input from users of numbers of floor
def timeToLandUserInput():
   #Variables
   HeightInStories = requestInteger("Number of floors")
   feetPerStory = 10
   metersPerfoot = 0.3048
   gravity = 9.81
   
   # Calculates the height in feet
   HeightInFeet = HeightInStories * feetPerStory
   
   # Calculate  the height in meters
   heightInMeters = HeightInFeet * metersPerfoot
   
   # Calculate the time to hit the ground
   timeToFall = sqrt((2*heightInMeters)/gravity)
   
   # Shows the time to fall in seconds
   print("Time ti fall (seconds):")
   print(timeToFall) 