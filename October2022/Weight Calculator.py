weight = int(input("Insert Weight here: "))
print("Kg or Pounds?")
answer = str(input())
answer = answer.lower()
print("Message made to low: " + answer + "\n")
if answer.find("k" or "g" or "kg"):
    weight = weight * 2.2
    weightFormat = "{:.2f}".format(weight)
    print("Weight in Pounds is: " + weightFormat)
elif answer.find("p" or "pounds"):
    weight = weight // 2.2
    weightFormat = "{:.2f}".format(weight)
    print("Weight in Kg is: " + weightFormat)
else:
    print("What did you even choose...")
