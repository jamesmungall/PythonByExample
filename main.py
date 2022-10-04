# Challenge 001, 002
# firstname = input("Enter your first name: ")
# surname = input("Enter your second name: ")
# print("your name is ", firstname, surname)
import math
import random
import turtle

# Challenge 003
# print("What do you call a bear with no teeth?\nA gummy bear!")

# Challenge 004
# num1 = int(input("Enter a number "))
# num2 = int(input("Enter another number "))
# print("The sum of these number is", num1, " + ", num2, " = ", num1 + num2)

# Challenge 005
# num1 = int(input("Enter 1st number "))
# num2 = int(input("Enter 2nd number "))
# num3 = int(input("Enter 3rd number "))
# print("(", num1, "+", num2, ")*", num3, "=", (num1+num2)*num3)

# Challenge 008
# bill = int(input("What is the price of the bill?"))
# numberOfPeople = int(input("How many people are there?"))
# print("Each person needs to pay", bill, "/", numberOfPeople, "=", bill/numberOfPeople)

# Challenge 011
# num1 = int(input("Enter a number over 100: "))
# num2 = int(input("Enter a number less than 10: "))
# wholeNumberDivision = num1//num2
# print(num2, "fits into", num1, wholeNumberDivision, "times, with a remainder of", num1 % num2)

# Challenge 012
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# if num1 > num2:
#     print(num2, num1)
# else:
#     print(num1, num2)

# Challenge 018
# num1 = int(input("Enter a number: "))
# if num1 < 10:
#     print("Too low")
# elif 10 <= num1 <= 20:
#     print("Correct")
# else:
#     print("Too high")

# Challenge 019
# num1 = int(input("Enter 1, 2 or 3: "))
# if num1 == 1:
#     print("thank you")
# elif num1 == 2:
#     print("well done")
# elif num1 == 3:
#     print("correct")
# else:
#     print("error")

# Challenge 020
# name: str = input("enter your name: ")
# print("your name has", len(name), "letters")

# Challenge 021
# firstname: str = input("enter your firstname: ")
# surname: str = input("enter your surname: ")
# print(firstname + surname, len(firstname + surname))


# Challenge 022
# firstname: str = input("enter your firstname: ")
# surname: str = input("enter your surname: ")
# print(firstname.title(), surname.title())

# Challenge 023
# line_of_text = input("input a line of text: ")
# startNum = int(input("start number"))
# endNum = int(input("end number"))
# print(line_of_text[startNum:endNum])

# Challenge 025
# firstname: str = input("enter your firstname: ")
# if len(firstname) < 5:
#     surname: str = input("enter your surname: ")
#     output = firstname+surname
#     print(output.upper())
# else:
#     print(firstname.lower())

# Challenge 026
# textInput: str = input("input a word: ")
# textInput = textInput.lower()
# first_letter = textInput[0]
# if first_letter == "a" or first_letter == "e" or first_letter == "i" or first_letter == "o" or first_letter == "u":
#     is_first_a_vowel = True
# else:
#     is_first_a_vowel = False
# if is_first_a_vowel:
#     print(textInput+"way")
# else:
#     start = 1
#     end = len(textInput)
#     new_word = textInput[start:end]
#     print(new_word+first_letter+"ay")

# Challenge 028
# num1 = float(input("Enter a decimal: "))
# print(round(num1, 2))

# Challenge 029
# num1 = float(input("Enter a number greater than 500: "))
# output = math.sqrt(num1)
# output = round(output, 2)
# print(output)

# Challenge 030
# print(round(math.pi, 5))

# Challenge 031
# num1 = float(input("Enter radius: "))
# output = math.pi * num1**2
# print(round(output, 2))

# Challenge 034
# print("1) Square\n2) Triangle")
# num = int(input("Choose a number: "))
# if num == 1:
#     side_length = int(input("Sidelength: "))
#     print("area is:", side_length**2)
# else:
#     base = int(input("base: "))
#     height = int(input("height: "))
#     print("area is: ", height * base * 0.5)

# Challenge 035
# name = input("enter your name: ")
# for i in range(1, 3):
#     print(i, name)

# Challenge 036
# name = input("enter your name: ")
# num = int(input("number of repeats: "))
# for i in range(1, num+1):
#     print(i, name)

# Challenge 037
# name = input("enter your name: ")
# for i in range(0, len(name)):
#     print(name[i])

# Challenge 039
# num = int(input("enter a number: "))
# for i in range(1, 11):
#     print(num * i)

# Challenge 040
# num = int(input("enter a number above 50: "))
# for i in range(num, 49, -1):
#     print(i)

# Challenge 042
# total = 0
# for i in range(0, 5):
#     num = int(input("number: "))
#     include = int(input("include this number? (1 = Yes or 0 = No): "))
#     if include == 1:
#         total = total + num
# print(total)

# Challenge 043
# up_or_down = int(input("Up (1) or down(0)? "))
# if up_or_down == 1:
#     top_number = int(input("Input top number: "))
#     for i in range(1, top_number+1):
#         print(i)
# elif up_or_down == 0:
#     bottom_number = int(input("choose a number less than 20: "))
#     for i in range(20, bottom_number-1, -1):
#         print(i)
# else:
#     print("I don't understand")

# Challenge 045
# total = 0
# while(total<50):
#     num = int(input("input a number: "))
#     total += num
# print(total)

# Challenge 049
# comp_num = random.randint(1, 100)
# print(comp_num)
# guess = int(input("Guess the number: "))
# while guess != comp_num:
#     if guess < comp_num:
#         print("Your guess is too low.")
#     else:
#         print("Your guess is too high.")
#     guess = int(input("Try again: "))
# print("You've got it!")

# Challenge 52
# print(random.randrange(1, 100))

# Challenge 53
# print(random.choice(["apple", "banana", "orange"]))

# Challenge 54
# heads_or_tails = random.choice(["h", "t"])
# guess = input("Guess heads or tails (h or t): ")
# if heads_or_tails == guess:
#     print("You win")
# else:
#     print("You lose")
# print("The computer selected", heads_or_tails)

# Challenge 60
# Cannot get turtle to work in PyCharm

# Challenge 069
# countries = ("UK", "Fr", "Nd", "Deu", "Es")
# print(countries)

# Challenge 070
# countries = ("UK", "Fr", "Nd", "Deu", "Es")
# print(countries)
# choice = int(input("Choose a country (1-5): "))
# print(countries[choice-1])

# Challenge 071
# sports = ["golf", "tennis"]
# new_sport = input("Type a sport: ")
# sports.append(new_sport)
# sports.append("squash")
# print(sports)

# Challenge 072
# subjects = ["French", "English", "Maths"]
# print(subjects)
# choice = input("Type a subject to delete: ")
# subjects.remove(choice)
# print(subjects)

# subjects = ["French", "English", "Maths"]
# print(subjects)
# choice = int(input("Choose a subject to delete(1, 2 or 3): "))
# subjects.pop(choice-1)
# print(subjects)

# Challenge 073
# foods = {1: "bread", 2: "milk", 3: "honey"}
# print(foods)
# new_food = input("Add a new food: ")
# foods.update({4: new_food})
# print(foods)
# choice = int(input("choose an element to remove (1, 2, 3 or 4): "))
# foods.pop(choice)
# print(foods)

# Challenge 074
# colours = ["red", "green", "blue", "yellow", "cyan", "magenta", "black", "white", "brown", "grey"]
# start = int(input("start (1 - 5): "))
# end = int(input("start (6 - 10): "))
# print(colours[start-1:end])

# Challenge 075
# numbers = []
# for i in range(1, 3+1):
#     new_number = random.randrange(100, 1000)
#     print(new_number)
#     numbers.append(new_number)
# choice = int(input("choose a number: "))
# if choice in numbers:
#     number_index = numbers.index(choice)
#     print(number_index)
# else:
#     print("not found")

# Challenge 076, 077
# invites = ["andrew", "bob", "carly"]
# print(invites)
# add_new = input("Do you want to add anyone else? (y / n): ")
# while add_new == 'y':
#     new_invite = input("New person: ")
#     invites.append(new_invite)
#     add_new = input("Do you want to add anyone else? (y / n): ")
# print(invites)
# name_choice = input("Type a name from the list: ")
# print("Index of", name_choice, "is", invites.index(name_choice))
# remove_invite = input("Do you want to remove them? (y / n): ")
# if remove_invite == 'y':
#     invites.remove(name_choice)
# print(invites)

# Challenge 078
# tv_shows = ["a", "b", "c", "d"]
# for i in range(len(tv_shows)):
#     print(tv_shows[i])
# new_show = input("Type in a new show: ")
# question_text = "Insert position. Type 0 for beginning of list and ", len(tv_shows), " for end of list: "
# position = int(input(question_text))
# tv_shows.insert(position, new_show)
# print(tv_shows)

# Challenge 079
# nums = []
# for i in range(3):
#     new_number = int(input("input a number: "))
#     nums.append(new_number)
#     print(nums)
# delete_last = input("Do you want to delete last number? (y/n): ")
# if delete_last == 'y':
#     nums.remove(new_number)
# print(nums)

# Challenge 080
# firstname = input("Type first name: ")
# print("length is: ", len(firstname))
# surname = input("Type surname: ")
# print("length is: ", len(surname))
# whole_name = firstname+" " + surname
# print(whole_name, len(whole_name))

# Challenge 081
# subject = input("type a subject: ")
# for letter in subject:
#     print(letter, end="-")

# Challenge 082
# poem = "Twas brillig"
# print(poem)
# print("There are ", len(poem), "letters in this string.")
# print("Indices run from 0 to", len(poem) - 1, ".")
# print("However, to get the last value you have to end at", len(poem))
# print("because when you give python a range in the format a:b, ")
# print("it runs from a to b-1")
# start = int(input("start: "))
# end = int(input("end: "))
# print(poem[start:end])

# Challenge 85
# name = input("type in your name: ")
# name_upper = name.upper()
# number_of_vowels = 0
# for i in range(len(name_upper)):
#     if name_upper[i] in ["A", "E", "I", "O", "U"]:
#         number_of_vowels += 1
# print("number of vowels is", number_of_vowels)

# Challenge 86
# pwd1 = input("type a password: ")
# pwd2 = input("retype password: ")
# if pwd1 == pwd2:
#     print("the passwords match")
# else:
#     print("the passwords do not match")
#     if pwd1.upper() == pwd2.upper():
#         print("they must be in the same case")

