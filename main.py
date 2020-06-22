def checkMultiple(num, multiple):
  return num % multiple == 0

def checkMultiples(num, biggestMultiple):
  for i in range(3, biggestMultiple):
    if checkMultiple(num, i) == False:
      return False
  return True

def getMultiples(multiple):
  i = 1
  multiply = multiple * (multiple -1 ) * (multiple -2 )
  while not(checkMultiples(multiply * i, multiple)):
    i += 1
  return multiply * i

print(getMultiples(27))


