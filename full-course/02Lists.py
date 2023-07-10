#https://www.youtube.com/watch?v=t8pPdKYpowI
name_of_unit = "hours"
calculation_to_units = 24
user_input = ""

def days_to_units (num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    
    
def validate_and_execute():
    try: 
     
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number) # better way to check
            print(calculated_value)
        elif user_input == 0:
            print("Please enter a number greater than zero")
        else:
            print("your input is invalid!!!")
    except ValueError:
        print ("Something went wrong... did you enter an integer?")



while user_input != "exit": 
    user_input= input("Enter  number of days to convert to units: ")
    # split uses spaces, but you can specify a character you want to use such as a comman/semi-colon
    # we using the comma below
    list_of_days = user_input.split(", ")
    for num_of_days_element in set(list_of_days):
        validate_and_execute()