
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(List)
choice = input('''Choose an action:
     1. Remove number
     2. Add number into the list
     3. Insert a number into the list depending on index
     4. Check if number is actually inside list
     5. Check length of list
     6. C1ear list
    
     Select your choice: ''')

def remove_number():
        number = int(input("Insert the number you would like to remove: "))
        List.remove(number)
        print(List)

def add_number():
        number = int(input("Choose number: "))
        List.append(number)
        print(List)

def add_number_by_index():
        number1 = int(input("Add index number: "))
        number2 = int(input("Choose number: "))
        List.insert(number1, number2)
        print(List)

def check_number():
        number = int(input("Add number to check number: "))
        if number in List:
            print("Number " + str(number) + " is in List")
        else:
            print("Number "+ str(number) + " is not in list")

def check_length():
        length = str(len(List))
        print("The length of the list is " + length)

def clear_list():
        print(List.clear())

def run_choice():
    if choice == "1":
        remove_number()
    if choice == "2":
        add_number()
    if choice == "3":
         add_number_by_index()
    if choice == "4":
        check_number()
    if choice == "5":
        check_length()
    if choice == "6":
        clear_list()

run_choice()

