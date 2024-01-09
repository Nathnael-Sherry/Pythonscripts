# # Function- A block of code that you can package together with a name and does something.
# def print_kevin():
#     text = "Nathan is cool"
#     print(text)
#     print(text)
#     print(text)
# print_kevin()

# If statement with a function
def school_age_calculator(age,name):
    if age < 5:
        print("Enjoy the time!", name, "is only",age)
    elif age == 5:
        print("Enjoy Kindergarten", name)
    else:
        print("They grow up so fast!")

school_age_calculator(5,"Nath")