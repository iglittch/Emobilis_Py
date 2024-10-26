# # Lists
# days = ["Sunday","Monday","Tuesday","Wednesday","Thurday","Friday","Saturday"]
# print(len(days))

# print("The last element on the list is {}".format(days[-1]))
# # print(f"The last element on the list is {}")

# # Range
# print(f"The weekdays is {days[1:6]}")

# if "Monday" in days: 
#     print("It is a day of the week")
# else:
#     print("Its not a day of the week")

# Append,Insert
to_do_list = ["Cook","Shop","Homework"]
print(f"Initial Todo list: {to_do_list}")
to_do_list[1] = "Grocery Shopping"
print(f"Altered Todo list: {to_do_list}")

to_do_list.insert(0 ,"Go to Pharmacy")
print(to_do_list)
to_do_list.append("Clean")
print(to_do_list)

# Remove
to_do_list.remove("Cook")
print(to_do_list)
to_do_list.pop(0)
print(to_do_list)

