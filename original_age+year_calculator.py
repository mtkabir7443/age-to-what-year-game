import time

play_again_flag = True

while play_again_flag:
    try:
        name = input("What is your name?: ")
        if not all(i.isalpha() or i.isspace() for i in name):
            raise ValueError("Please input only letters. Try again.")

        while True:
            age_str = input("What is your age?: ")
            if age_str.isdigit():
                age = int(age_str)
                break
            else:
                print("Please input only numbers. Try again.")

        while True:
            age_to_be_str = input("Input the age you want to be, in return the year you turn that age will be spit out: ")
            if age_to_be_str.isdigit():
                age_to_be = int(age_to_be_str)
                break
            else:
                print("Please input only numbers. Try again.")

        current_year = time.localtime().tm_year
        dated_year = current_year - age + age_to_be

        print("You will turn",age_to_be,"in the year",dated_year)

        def play_again():
            return input("Would you like to play again?('yes' or 'no'): ")

        while True:
            user_response = play_again()

            if user_response.lower() == "no":
                play_again_flag = False
                break
            elif user_response.lower() == "yes":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    except ValueError as e:
        print(e)

print("Thank you for playing!")