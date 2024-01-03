import time

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Try again.")

def play_again():
    while True:
        user_response = input("Would you like to play again? ('yes' or 'no'): ").lower()
        if user_response in ('yes', 'no'):
            return user_response == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

play_again_flag = True

while play_again_flag:
    try:
        name = get_valid_input("What is your name?: ", lambda x: all(i.isalpha() or i.isspace() for i in x))

        age_str = get_valid_input("What is your age?: ", str.isdigit)
        age = int(age_str)

        age_to_be_str = get_valid_input("Input the age you want to be, in return the year you turn that age will be spit out: ", str.isdigit)
        age_to_be = int(age_to_be_str)

        current_year = time.localtime().tm_year
        dated_year = current_year - age + age_to_be

        print("You will turn", age_to_be, "in the year", dated_year)

        if not play_again():
            break

    except ValueError as e:
        print(e)

print("Thank you for playing!")