#https://www.youtube.com/watch?v=t8pPdKYpowI
name_of_unit = "hours"
calculation_to_units = 24

def days_to_units (num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    
    
def validate_and_execute(user_input):
    try: 
        user_input = int(user_input) #good
        if user_input.isdigit():
            
            if user_input > 0:
                calculated_value = days_to_units(user_input) # better way to check
                print(calculated_value)
            elif user_input == 0:
                print("Please enter a postive number above zero")
    except:
        print ("Please enter an integer")


user_input = ""
while user_input != "exit": 
    user_input = input("Enter days to convert to hours:  ")
    validate_and_execute(user_input)