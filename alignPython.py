#Ross Rhone
# Used to find the highest line of DNA that matches with the user's desired input
# out of all the strains of DNA. 

import copy


fileIn = open("seq.txt")


source = input("SOURCE : ")



score = 0
maxScore = 0                                    #used to score against subwords in same sequence
maxMatchScore = 0;                              #used to score against sequences against other sequences
matchScore = 0;
sourceLen = len(source)
entryLen = sourceLen * 3                        #how many diff combo of sub words can be made
i = 10
subcount = 0
bestMatch = []                                  #stores the highest score pairing
subWordCalc = []                                #used for caluclations
bestLine = []                                   #ID of matching Sequence
firstWord = 1
bestSeq = []                                    #matching Sequence


def writeSource():
    k = 0
    c = 0

    for aChar in line:

         if(k == int(bestMatch[c]) and bestMatch[c+2] == 't'):
             print(bestMatch[c+1], end='')
             c += 3
         elif(k == int(bestMatch[c]) and bestMatch[c+2] == 'f'):
             print(bestMatch[c+1], end='')
             c += 3
         else:
             print(" ", end='')

         if(c == entryLen):
             print("\n", end='')
             break


         k += 1

def writeGaps():
 k = 0
 c = 0

 for aChar in line:

      if(k == int(bestMatch[c]) and bestMatch[c+2] == 't'):
          print("|", end='')
          c += 3
      elif(k == int(bestMatch[c]) and bestMatch[c+2] == 'f'):
          print(" ", end='')
          c += 3
      else:
          print(" ", end='')

      if(c == entryLen):
          print("\n", end='')
          break


      k += 1

def writeSequence():

 for aChar in bestSeq[10:]:
      print(aChar, end='')



def blast(i,lineLen, sourceLen, entryLen):          #blasts the sequence for the most accurate solution based off of score!
    global subcount
    global j
    global score
    global maxscore
    global subWordCalc
    global firstWord
    global maxMatchScore
    global bestMatch
    global bestLine
    global bestSeq

    for aChar in line[i:i+sourceLen] :              #Begin searching through the sequence for matching chars

      if (j > lineLen):                             #When it has reached the end of the list return
        return

      if (aChar == source[subcount]):               #There is a match! (subWordCalc, char, t/f)

          subWordCalc.append(str(j-10))
          subWordCalc.append(source[subcount])
          subWordCalc.append("t")
          score += 5

      else:
         score -= 3
         subWordCalc.append(str(j-10))
         subWordCalc.append(source[subcount])
         subWordCalc.append("f")

      subcount += 1


      if (subcount == sourceLen):                   #Once a sub word has finished check if it has a greater score than others
          i -= sourceLen-2
          j -= sourceLen-2
          subcount = 0

          if(firstWord == 0 and maxscore <= score):     #delete data in front for new scoring sub word
              maxscore = score
              del subWordCalc[0:entryLen]
          if(maxscore <= score and firstWord == 1 ):    #no need to dele since there will be nothin in the list yet
              maxscore = score
              firstWord = 0
          else:
              del subWordCalc[entryLen:]
          if(maxMatchScore <= maxscore ):               #update score against other sequences
              maxMatchScore = maxscore
              bestMatch = copy.deepcopy(subWordCalc)
              bestLine = line[0:8]
              bestSeq = line[10:]


          score = 0
          blast(i, lineLen, sourceLen, entryLen)        #continue to call until full sequence's best match as been calced

      j += 1
      i += 1

for line in fileIn:

   lineLen = len(line[9:])

   subcount = 0
   maxscore = 0
   score = 0
   j = 0
   firstWord = 0

   blast(10,lineLen,sourceLen, entryLen)


print("Highest score : " + str(maxMatchScore))
print("Best match line : " + str(bestLine))

writeSource()
writeGaps()
writeSequence()
