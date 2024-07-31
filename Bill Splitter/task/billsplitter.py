# Importing required modules
import random

# Taking user input
number_of_friends = int(input("Enter the number of friends joining (including you): "))

# Handling invalid number of people (zero or negative)
if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    # Creating empty list to store input
    friends_list = []
    # Taking user input
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_friends):
        friends_list.append(input())

    # Taking user input
    total_bill = int(input("Enter the total bill value: "))

    # Asking if the user wants the feature
    is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')

    if is_lucky.lower() == "no":
        print("No one is going to be lucky")
        # Splitting the bill
        equal_value = round(total_bill / number_of_friends, 2)
        # Creating the dictionary
        friends_dictionary = {key: equal_value for key in friends_list}
        print(friends_dictionary)
    else:
        lucky_person = random.choice(friends_list)
        print(f"{lucky_person} is the lucky one!")
        # Splitting the bill among the rest
        equal_value = round(total_bill / (number_of_friends - 1), 2)
        # Creating the dictionary with the lucky person set to 0
        friends_dictionary = {key: (0 if key == lucky_person else equal_value) for key in friends_list}
        print(friends_dictionary)