
import random

NOUN = open("noun.txt").read().splitlines()
VERB = open("verb.txt").read().splitlines()
VERBOBJ = open("verbObj.txt").read().splitlines()
ADJ = open("adj.txt").read().splitlines()
DET = open("det.txt").read().splitlines()
ADV = open("adv.txt").read().splitlines()
PREP = open("prep.txt").read().splitlines()
RPNOUN = open("rpnoun.txt").read().splitlines()

def getRanWord(words):
    return random.choice(list(words))

def writeWords(inString, rules):
  bufferStr = ""
  for i in range(0,len(inString),2):
    chars = inString[i] + inString[i+1]
    if chars in rules.keys():
      bufferStr = bufferStr + getRanWord(rules[chars]) + " "
  return bufferStr


def arbitraryText(n, Output, rules): #don't go too high w/ recursion
  i = 0 #counter
  if i == n: #n iterations reacher
    return Output
  else:
    outBuffer = ""
    for char in range(0,len(Output),2):
      char = Output[char] + Output[char+1] #get the character
      if char in rules.keys(): #get transformation
        outBuffer = outBuffer + rules[char] #replce
      else:
        outBuffer = outBuffer + char #retain
    return arbitraryText(n-1, outBuffer, rules) #!!! MUst return



syntaxRules = {
    "np":"dtjpnwrp",
    "jp":"jw",
    "vp":"apvwnp",
    "ap":"aw",
    "pp":"pwdtnp",
    "rp":"rnvp"
    
}

wordReplacements = {
  #"np":NOUN,
  #"jp":ADJ,
  #"dp":DET,
  #"vp":VERBOBJ,
  #"ap":ADV,
  #"pp"

  # -w indicates end of life
  "vw":VERBOBJ,
  "nw":NOUN,
  "jw":ADJ,
  "aw":ADV,
  "dt":DET,
  "pw":PREP,
  "rn":RPNOUN
}

a=arbitraryText(8,"npvp",syntaxRules)
print(a)
print(writeWords(a, wordReplacements))

