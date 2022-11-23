#T1: Pick open a picture file and open it
#T2: Print characters in string using for loop


#This fuction will allow a user to pick a file
def openShowPicture():
   #select file
   file1 = pickAFile()
   #print name and location
   print (file1)
   #make selected file into picture
   pic1 = makePicture(file1)
   #Display picture
   show(pic1)
   #Shows X and Y the detail of the picture
   explore(pic1)
   #X=0,Y=0 R:7 G:4 B:0
   #X=250, Y=0 R:132 G:176 B:225
   #X=0, Y=250 R:102 G:127 B:44
   

#Breaks up character, use STR
def partOfString(string):
   for letter in string:
      print (letter)
      
#Sums 3 values and display result
def sumThree(a, b, c):
   x = a + b + c
   print("result =" + str(x))

def sumThree2(a, b, c):
   x = a + b + c
   print(str(a)+ "+" +  str(b)+ "+" + str(c) +"=" + str(x))
   
#Devides the number by an input then displays the remainder
def devideBy(top, bottom):
   x = top / bottom
   print (int(x))
   