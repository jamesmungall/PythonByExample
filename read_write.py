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
def j_menu():
    print("1) Create a new file")
    print("2) Display the file")
    print("3) Add a new item to the file")
    user_input = input("Make a selection 1, 2 or 3: ")
    return user_input


selection = j_menu() # note that selection is a string
valid_selections = [1, 2, 3]
# This will throw an error if the selection is not in the valid_selections list
index = valid_selections.index(int(selection))

print("Thank you. You choose option " + str(selection))
if selection == "1":
    school_subject = input("Enter a subject: ")
    file = open("subject.txt", "w")
    file.write(school_subject+"\n")
    file.close()

if selection == "2":
    file = open("subject.txt", "r")
    print(file.read())
    file.close()

if selection == "3":
    new_subject = input("Enter a new subject: ")
    file = open("subject.txt", "a")
    file.write(new_subject+"\n")
    file.close()
    file = open("subject.txt", "r")
    print(file.read())
    file.close()