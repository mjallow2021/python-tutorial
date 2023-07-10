
def days_to_units (num_of_days, conversion_unit):
    if conversion_unit == "hours":    
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":    
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    elif conversion_unit == "seconds":    
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60 } seconds"
    else:
        return "unit supplied unsupported at the moment"
    

def validate_and_execute(days_and_units_dictionary):
    try:
        user_input_number = int(days_and_units_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_units_dictionary["units"]) # better way to check
            print(calculated_value)
        elif user_input_number == 0:
            print("Please enter a number greater than zero")
        else:
            print("your input is invalid!!!")
    except ValueError:
        print ("Something went wrong... did you enter an integer?")
