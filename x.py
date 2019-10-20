def InsertionSort(userInput):

  print("Initial Input:",userInput)
  for x in range(1, len(userInput)):
    if userInput[x] < userInput[x - 1]:
      userInput[x], userInput[x - 1] = userInput[x - 1], userInput[x]
    else:
      keyIndex = x
      for y in range(len(userInput)):
        print(userInput[y])

    
    
  return userInput
    



test1 = [2, 3, 14, 50, 5]
print("Return Output:",InsertionSort(test1))  