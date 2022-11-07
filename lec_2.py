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