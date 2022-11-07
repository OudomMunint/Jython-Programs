# Lecture 8 demo functions
# Simon, August 2012

def upVolume():
   file = pickAFile()
   sound = makeSound(file)
   sample = getSamples(sound)
   getSampleValue(sample) * 10 / 100
   play(sound)
    
def adjustVolume(aSound, multiplier):
  # Adjust the amplitude of a sound by a specified multiplier
  for sample in getSamples(aSound):
    setSampleValue(sample, getSampleValue(sample) * multiplier)

def normalise(aSound):
  # Increase the amplitude of aSound as much as possible without clipping
  # First we have to find the biggest (positive or negative) value
  
  # Start with a copy of the sound, to avoid unwanted side-effects
  newSound = duplicateSound(aSound)
  biggest = 0 # The biggest is surely going to be bigger than this!
  for samp in getSamples(newSound):
    if abs(getSampleValue(samp)) > biggest: # Remember absolute value?
      biggest = abs(getSampleValue(samp))
  
  # After that loop, biggest is the biggest (positive or negative) amplitude
  # Multiplier will multiply it up to the maximum amplitude of 32767
  multiplier = float(32767) / biggest
  # It's a fraction; if we didn't make it a float, it would lose lots of precision!
  
  # In the next loop, we multiply every sample value by the same multiplier
  for samp in getSamples(newSound):
    setSampleValue(samp, multiplier * getSampleValue(samp))
  
  # That's it - newSound has been normalised; now return it
  return(newSound)
  # End of normalise (this comment is because the end is so far from the start)

def adjustAmp(aSound, multiplier, startIndex, endIndex):
  # Adjust the amplitude of aSound by multipler in the samples from startIndex to endIndex
  # First we duplicate the sound and get the array of samples
  newSound = duplicateSound(aSound)
  samples = getSamples(newSound)
  # Now we can select the samples that need adjusting and adjust them
  for index in range(startIndex, endIndex):
     setSampleValue(samples[index], multiplier * getSampleValue(samples[index]))
  # And return the new sound
  return(newSound)

def boostThreeBits(aSound, mult, startA, endA, startB, endB, startC, endC):
  # A highly specific function to boost the amplitude by multiplier just in three specific ranges
  # adjustAmpt returns a new sound, so we progressively assign it to new sound variables
  sound1 = adjustAmp(aSound, mult, startA, endA)
  sound2 = adjustAmp(sound1, mult, startB, endB)
  return(adjustAmp(sound2, mult, startC, endC))