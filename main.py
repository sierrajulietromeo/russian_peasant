numberList1 = []
numberList2 = []
grandTotal = 0


def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 


print("The Russian peasant algorithm")
print()

number1 = inputNumber("Enter number 1: ")
number2 = inputNumber("Enter number 2: ")

numberList1.append(number1)
numberList2.append(number2)

while number1 != 1:

  number1 = number1 // 2
  number2 = number2 * 2
  numberList1.append(number1)
  numberList2.append(number2)

for i in range(len(numberList1)):

  if numberList1[i] % 2 != 0:
    grandTotal = grandTotal + numberList2[i]
    print("{} (plus {}) ".format(grandTotal, numberList2[i]))

print()    
print(numberList1[0], "multiplied by", numberList2[0], "is", grandTotal)
