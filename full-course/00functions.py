#https://www.youtube.com/watch?v=t8pPdKYpowI

name_of_unit = "hours"
calculation_to_units = 24

def days_to_units (num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "Please enter a postive number above zero"
    else:
        return "Please enter a valid number"


user_input = input("Enter days to convert to hours:  ")

if user_input.isdigit():
    user_input_number = int(user_input) #good
    calculated_value = days_to_units(user_input_number) # better way to check
    print(calculated_value)
else:
    print ("Please enter an integer")
