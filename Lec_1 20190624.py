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
    
   
