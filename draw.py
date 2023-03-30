import turtle
t = turtle.Turtle()
t.down()
t.speed(0/2)
rules = {
  "a":"b-a+a+",
  "b":"aa"
}

#just generating text:
def arbitraryText(n, Output, rules): #don't go too high w/ recursion
  i = 0 #counter
  
  if i == n: #n iterations reacher
    return Output
  
  else:
    outBuffer = ""
    
    for char in range(len(Output)):
      char = Output[char] #get the character
      
      if char in rules.keys(): #get transformation
        outBuffer = outBuffer + rules[char] #replce
      else:
        outBuffer = outBuffer + char #retain
      
    return arbitraryText(n-1, outBuffer, rules) #!!! MUst return
    
      
drawRules = {
  "a": (t.fd, 10),
  "b": (t.bk,10),
  "+": (t.rt,25),
  "-": (t.lt,25)
}
instructions = arbitraryText(6,"a-b",rules)
print(instructions)
for char in range(len(instructions)):
  char = instructions[char]
  if char in drawRules.keys():
    drawRules[char][0](drawRules[char][1])
  

