#Author: Dom
#Date: 12/08/2019
#Tasks:


def playSound():
   file = pickAFile()
   sound = makeSound(file)
   
def playSound1(sound):
   print(sound)
    
def sampleRate(sound):
   sampleRate = getSamplingRate(sound)
   return(sampleRate)
   
def lengthSound(sound):
   soundLength = getLength(sound)
   return(soundLength)
   
def callFucntions():
  file = pickAFile()
  sound = makeSound(file)
  playSound1(sound)
  print(sampleRate(sound))
  print(lengthSound(sound))
  explore(sound)
 
  
  location = requestInteger("Enter Location")
  newValueLocation = requestInteger("Enter new sound value")
  
  print("Original : " + str(getSampleValueAt(sound, location)))
  setSampleValueAt(sound, location, newValueLocation)
  print("New value at location : " + str(getSampleObjectAt(sound, location)))

  
  