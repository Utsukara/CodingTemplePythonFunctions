import re

# 1. The Welcoming Program
# Objective:
# The aim of this assignment is to create a simple program that greets users and responds based on their input.

# Task 1: Code a program that asks for the user's name and prints a personalized greeting.
# Task 2: Modify the program to ask the user how they are feeling today and respond with a comforting message if they're feeling down, or a cheerful one if they're happy.
# Task 3: Add error handling to ensure that the user inputs a string for their name and not a number or special character.

def user_greeting():
    while True:
        name = input("What is your name?")
        if re.match("^[A-Za-z ]+$",name):
            break
        else:
            print("Please enter a valid name(letters and spaces only).")
    greeting = input(f"Hello {name}! How are you doing today?")
    positive_list = ['happy','content','peaceful','grateful','relieved','joyful','optimistic','excited','energized','satisfied','good']
    negative_list = ['sad','anxious','depressed','frustrated','overwhelmed','angry','disappointed','lonely','exhausted','hopeless','bad','sleepy']
    if greeting.lower() in positive_list:
        print("It sounds like you are having a good day. That is great!")
    elif greeting.lower() in negative_list:
        print("That is not good! I hope your day gets better.")
    else:
        print("Your day can always get better!")
    return

user_greeting()

# 2. The Calculator App
# Objective:
# The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.

def division(x, y):
    try:
        divide = x // y
        remainder = x % y
        float_divide = x / y
        print(f"When X is divided by Y the answer is: {divide} with remainder: {remainder}\nThis is also equal to: {float_divide}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    return

def multiply(x, y):
    print(f"When X is multiplied by Y the answer is: {x * y}")
    return

def add(x, y):
    print(f"When X and Y are added the answer is: {x + y}")
    return

def subtract(x, y):
    print(f"When Y is subtracted from X the answer is: {x - y}")
    return

def square(x, y):
    print(f"X to the power of Y equals: {x ** y}")
    return

def get_number(input_prompt):
    while True:
        try:
            return float(input(input_prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': division,
    '5': square,
}

while True:
    userX = get_number("Enter a value for X: ")
    userY = get_number("Enter a value for Y: ")
    print("\nChoose an operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square (X^Y)")
    choice = input("Your choice (1/2/3/4/5): ")
    
    operation = operations.get(choice)
    if operation:
        operation(userX, userY)
    else:
        print("Invalid operation choice.")

    if input("Do you want to perform another calculation? (yes/no): ").lower() != 'yes':
        break

# 3. The Temperature Converter
# Objective:
# The aim of this assignment is to write a program that converts temperatures between Fahrenheit and Celsius.

# Task 1: Code a function that converts Celsius to Fahrenheit.
# Task 2: Code a function that converts Fahrenheit to Celsius.
# Task 3: Implement a user interface that asks the user which conversion they want to perform and calls the appropriate function.

def degreeCelToFahr(celsius):
    fahrenheit = ((9/5) * celsius) + 32
    return fahrenheit

def degreeFahrToCel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

while True:
    print(f"\nWould you like to convert:\n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\nOr enter 'exit'")
    user_input = input("Please choose 1 or 2: ")
    if user_input == '1':
        Fahrenheit = float(input("Enter a temperature in fahrenheit to convert: "))
        print(f"Fahrenheit: {Fahrenheit}\nCelsius: {degreeFahrToCel(Fahrenheit):.2f}")
    elif user_input == '2':
        Celsius = float(input("Enter a temperature in celsius to convert: "))
        print(f"Celsius: {Celsius}\nFahrenheit: {degreeCelToFahr(Celsius):.2f}")
    elif user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    else:
        print("Input Invalid. Please enter '1', '2' or 'exit'.")

# 4. The Shopping List Maker
# Objective:
# The aim of this assignment is to create a program that helps users make a shopping list.

def addToShoppingCart(item, cart):
    cart.append(item)
    print(f"'{item}' has been added to your cart.")

def removeFromShoppingCart(item, cart):
    if item in cart:
        cart.remove(item)
        print(f"'{item}' has been removed from your cart.")
    else:
        print(f"'{item}' not found in your cart.")

def printCart(cart):
    if cart:
        print("Your shopping cart contains:")
        for item in cart:
            print(f"- {item}")
    else:
        print("Your shopping cart is empty.")

shoppingCart = []
while True:
    user_input = input("Please enter what you would like to do with your cart:\n1. Add (add item to cart)\n2. Remove (removes item from cart)\n3. View (view items in cart)\n4. Purchase (purchase items in cart)\n5. Exit (leave the store)\nYour choice: ")
    
    if user_input == '1':
        item_to_add = input("Enter the item you would like to add to the cart: ")
        addToShoppingCart(item_to_add, shoppingCart)
    elif user_input == '2':
        item_to_remove = input("Enter the item you would like to remove from the cart: ")
        removeFromShoppingCart(item_to_remove, shoppingCart)
    elif user_input == '3':
        printCart(shoppingCart)
    elif user_input == '4':
        if shoppingCart:
            print("Thank you for your purchase. Here are the items you've bought:")
            printCart(shoppingCart)
            shoppingCart.clear()  # Clear the cart after purchase
            print("Your cart is now empty.")
        else:
            print("Your shopping cart is empty. Nothing to purchase.")
    elif user_input == '5':
        print("Thank you for shopping with us. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number from 1 to 5.")

# 5. The Grade Analyzer
# Objective:
# The aim of this assignment is to analyze a set of grades and provide statistics.

# Task 1: Code a function to calculate the average grade.
# Task 2: Implement a function to find the highest and lowest grade.
# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).

def averageGrade(gradeList):
    average = 0
    for grade in gradeList:
        average += grade
    average /= len(gradeList)
    return average

def highAndLow(gradeList):
    high = gradeList[0]
    low = gradeList[0]
    for grade in gradeList:
        if grade > high:
            high = grade
        elif grade < low:
            low = grade
        else:
            pass
    return [low, high]

def letterGradeCat(gradeList):
    gradeCategories = {'A': [], 'B': [], 'C': [], 'D': [], 'F': []}
    
    for grade in gradeList:
        if grade >= 90:
            gradeCategories['A'].append(grade)
        elif grade >= 80:
            gradeCategories['B'].append(grade)
        elif grade >= 70:
            gradeCategories['C'].append(grade)
        elif grade >= 60:
            gradeCategories['D'].append(grade)
        else:
            gradeCategories['F'].append(grade)
    
    categorizedGradesList = [(category, grades) for category, grades in gradeCategories.items()]
    
    return categorizedGradesList

gradeList = [95, 82, 74, 58, 89, 90, 85, 77, 65, 54, 88]

average_grade = averageGrade(gradeList)
print(f"The class average is: {average_grade:.2f}")

high_low = highAndLow(gradeList)
print(f"The class low is: {high_low[0]}\nThe class high is: {high_low[1]}")

categorizedGrades = letterGradeCat(gradeList)
for category, grades in categorizedGrades:
    print(f"Grades in {category}: {grades}")

# 6. The Daily Planner
# Objective:
# The aim of this assignment is to create a simple daily planner that can add, remove, and display tasks.

# Task 1: Write a function to add a task with a time slot.
# Task 2: Code a function to remove a task.
# Task 3: Implement a display function that shows all tasks in order of time.

def isValidTime(time):
    #Check if the given time is in a valid format (HH:MM AM/PM).
    pattern = r"(1[0-2]|0?[1-9]):[0-5][0-9] (AM|PM)"
    return re.match(pattern, time) is not None

def taskAndTime(task, time, planner):
    if not isValidTime(time):
        print("Invalid time format. Please use 'HH:MM AM/PM' format.")
        return

    if time in planner:
        print(f"Time slot {time} is already taken. Please choose another time.")
    else:
        planner[time] = task
        print(f"Task: '{task}' added at time: {time}")

def removeTask(time, planner):
    if not isValidTime(time):
        print("Invalid time format. Please use 'HH:MM AM/PM' format.")
        return

    if time in planner:
        removed_task = planner.pop(time)
        print(f"Removed '{removed_task}' at time {time}.")
    else:
        print(f"No task found at {time} to remove.")

while True:
    print("\nWhat would you like to do?")
    print("1: Add a task")
    print("2: Remove a task")
    print("3: View schedule")
    print("4: Exit")
    choice = input("Please enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        time = input("Enter the time for the task (e.g., 10:00 AM): ")
        taskAndTime(task, time, dailyPlanner)
    elif choice == '2':
        time = input("Enter the time of the task to remove (e.g., 10:00 AM): ")
        removeTask(time, dailyPlanner)
    elif choice == '3':
        schedule(dailyPlanner)
    elif choice == '4':
        print("Exiting the daily planner.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

# 7. The Quiz Game
# Objective:
# The aim of this assignment is to create a quiz game that asks questions and checks answers.

# Task 1: Develop a list of questions and answers.
# Task 2: Write a function that quizzes the user and takes their answers.
# Task 3: Score the quiz and give the user feedback on their performance.

answerForQuestion = []

def question1(answer):
    return answer.lower() == 'b'

def question2(answer):
    return answer.lower() == 'c'

def question3(answer):
    return answer.lower() == 'c'

def question4(answer):
    return answer.lower() == 'b'

def question5(answer):
    return answer.lower() == 'c'

print('''1. How many planets are there?
   a) 7
   b) 8
   c) 9
   d) 10''')

answerToMC = input("Please enter your answer(a,b,c,d): ")
answerForQuestion.append(question1(answerToMC))

print('''2. What is the third planet from the sun?
   a) Mars
   b) Venus
   c) Earth
   d) Mercury''')

answerToMC = input("Please enter your answer(a,b,c,d): ")
answerForQuestion.append(question2(answerToMC))

print('''3. What is the name of the galaxy we are in?
   a) Andromeda Galaxy
   b) Whirlpool Galaxy
   c) Milky Way Galaxy
   d) Triangulum Galaxy''')

answerToMC = input("Please enter your answer(a,b,c,d): ")
answerForQuestion.append(question3(answerToMC))

print('''4. What is the center of the cell called?
   a) Cytoplasm
   b) Nucleus
   c) Mitochondria
   d) Ribosome''')

answerToMC = input("Please enter your answer(a,b,c,d): ")
answerForQuestion.append(question4(answerToMC))

print('''5. What process makes energy in plants?
   a) Respiration
   b) Fermentation
   c) Photosynthesis
   d) Fission''')

answerToMC = input("Please enter your answer(a,b,c,d): ")
answerForQuestion.append(question5(answerToMC))

correct = 0
for answer in answerForQuestion:
    if answer == True:
        correct += 1

print(f"{correct}/5 correct.")

# 8. The Journey Planner
# Objective:
# The aim of this assignment is to create a program that plans a journey, calculating travel times and stops.

# Task 1: Code a function that calculates travel time based on distance and speed.
# Task 2: Create a feature that suggests stops based on the length of the journey.
# Task 3: Implement user input for starting point, destination, and preferred travel speed.

# 9. The Personal Library Organizer
# Objective:
# The aim of this assignment is to create a system that organizes a personal library of books.

# Task 1: Write a function to add books with title, author, and genre.
# Task 2: Code a search function to find books by title or author.
# Task 3: Implement a way to display books sorted by genre or author.

# 10. The Fitness Tracker
# Objective:
# The aim of this assignment is to create a program that tracks fitness activities and calories burned.

# Task 1: Develop a function to log different fitness activities and their duration.
# Task 2: Write a function that estimates calories burned based on the activity and duration.
# Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.