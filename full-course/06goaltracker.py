from datetime import datetime

user_input = input("Enter goal and date sepatated by colon: ")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

#print(datetime.datetime.strptime(deadline,"%d.%m.%Y"))
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")

# get days till deadline
today_date = datetime.today()
days_to_go = deadline_date - today_date


# lean python:31.12.2023
print(f"Dear user! You have {days_to_go.days} days to reach your goal:  {goal}")