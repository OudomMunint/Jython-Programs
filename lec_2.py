#Dom
#1/7/2019
#Task
#T1: Pick open a picture file and open it
#T2: Print characters in string using for loop


#T1
#This fuction will allow asue to pick a file
#print the details
def openShowDetails():
   #select file
   file1 = pickAFile()
   #print name and location
   print (file1)
   #make selected file into picture
   pic1 = makePicture(file1)
   #Display picture
   show(pic1)
   #see the XY and RGB of each pixel
   explore(pic1)
   
   
#T2
#This function accepts a string as an argument
#Breaks up character
def partOfString(string):
   for letter in string:
      print letter

#Dom
#24/6/2019
#tasks:
#T1: First function, print word

#T1
def showWords():
   #Print the message
   #Returns a value
   print("Hello world")
   #print("debug: Call from task2")
   return("56")

#T2 Call task1
#Call the function in T1
#Print the return value in T1  

def callTask1():
   x = showWords()
   print x 
   
#T3: Give function parameter to print name

#T3 Pass argument to function to print name
def printName(name):
   #change parameter to string
   print("your Name is: " + str(name))
    
   
