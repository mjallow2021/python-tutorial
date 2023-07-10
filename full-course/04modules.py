from nanafullcourse_mymodule import validate_and_execute #better use of modules
#import nanafullcourse_mymodule #works but not recommended
#https://www.youtube.com/watch?v=t8pPdKYpowI

 
user_input = ""

while user_input != "exit": 
    user_input= input("Enter days, and conversion units [eg: 10:hours] ")
    # split uses spaces, but you can specify a character you want to use such as a comman/semi-colon
    # we using the comma below
     #print(days_and_units)
    days_and_units = user_input.split(":")
    days_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1] }
    for num_of_days_element in set(days_and_units_dictionary):
        validate_and_execute(days_and_units_dictionary)

   