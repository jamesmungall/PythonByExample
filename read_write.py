# file = open("Countries.txt", "w")
# file.write("Italy\n")
# file.write("Germany\n")
# file.write("Spain\n")
# file.close()
#
# file = open("Countries.txt", "a")
# file.write("France\n")
# file.close()
#
# file = open("Countries.txt", "r")
# print(file.read())


# Challenge 105
# from random import randint
# file = open("Numbers.txt", "w")
# for i in range(5):
#     file.write(str(randint(1, 10)))
#     if i<4:
#         file.write(",")
# file.close()

# Challenge 106
# file = open("names.txt", "w")
# file.write("Arthur\n")
# file.write("Bert\n")
# file.write("Charles\n")
# file.write("Duke\n")
# file.write("Edsal\n")
# file.close()

# # Challenge 107
# file = open("names.txt", "r")
# print(file.read())
# file.close()

# Challenge 108
# file = open("names.txt", "a")
# new_name = input("Type in a new name: ")
# file.write(new_name)
# file.close()
# file = open("names.txt","r")
# print(file.read())
# file.close()

# Challenge 109
# def j_menu():
#     print("1) Create a new file")
#     print("2) Display the file")
#     print("3) Add a new item to the file")
#     user_input = input("Make a selection 1, 2 or 3: ")
#     return user_input
#
#
# selection = j_menu() # note that selection is a string
# valid_selections = [1, 2, 3]
# # This will throw an error if the selection is not in the valid_selections list
# index = valid_selections.index(int(selection))
#
# print("Thank you. You choose option " + str(selection))
# if selection == "1":
#     school_subject = input("Enter a subject: ")
#     file = open("subject.txt", "w")
#     file.write(school_subject+"\n")
#     file.close()
#
# if selection == "2":
#     file = open("subject.txt", "r")
#     print(file.read())
#     file.close()
#
# if selection == "3":
#     new_subject = input("Enter a new subject: ")
#     file = open("subject.txt", "a")
#     file.write(new_subject+"\n")
#     file.close()
#     file = open("subject.txt", "r")
#     print(file.read())
#     file.close()


# file = open("starts.csv","a")
# name = input("enter name: ")
# age = input("Enter age: ")
# start = input("Enter start: ")
# newRecord = name + ","+age+","+start+"\n"
# file.write(str(newRecord))
# file.close()
import csv

# file = open("starts.csv","r")
# search = input("Enter the data you are searching for: ")
# reader = csv.reader(file)
# for row in file:
#     if search in str(row):
#         print(row)

# file = list(csv.reader(open("starts.csv")))
# tmp = []
# for row in file:
#     tmp.append(row)
#
# file = open("newStarts.csv", "w")
# x = 0
# for row in tmp:
#     newRec = tmp[x][0] + "," + tmp[x][1] + "," + tmp[x][2] + "\n"
#     file.write(newRec)
#     x = x + 1
# file.close()

# Challenge 111, 112
# file = open("books.csv","w")
# file.write("Book, Author, Year Released\n")
# file.write("To Kill a Mockingbird, Harper Lee, 1960\n")
# file.write("A Brief History of Time, Stephen Hawking, 1988\n")
# file.write("The Great Gatsby, F. Scott Fitzgerald, 1922\n")
# file.write("The Man who mistook his wife for a hat, Oliver Sacks, 1985\n")
# file.write("Pride and Prejudice, Jane Austen, 1813\n")
# file.close()
#
# book = input("Enter book: ")
# author = input("Enter author: ")
# year = input("Enter year: ")
# file = open("books.csv", "a")
# newRecord = book + "," + author + "," + year + "\n"
# file.write(newRecord)
# file.close()
#
# books_csv_file = open("books.csv", "r")
# print(books_csv_file.read())

# Challenge 113
number_of_new_records = input("How many records do you want to add?(0 - 10) ")
valid_selections = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# This will throw an error if the selection is not in the valid_selections list
index = valid_selections.index(int(number_of_new_records))
file = open("books.csv", "a")
for i in range(int(number_of_new_records)):
    book = input("Enter book: ")
    author = input("Enter author: ")
    year = input("Enter year: ")
    newRecord = book + "," + author + "," + year + "\n"
    file.write(newRecord)
file.close()

authorSearch = input("Enter the author you are searching for: ")
with open("books.csv", mode="r") as books_csv_file:
    reader = csv.reader(books_csv_file)
    for row in reader:
        if authorSearch.capitalize() in str(row):
            print(row)



