# If,Elif & Else statements

vacation_days = 1
goals_met = True
if goals_met:
    # all code indented under the if statement is the block of code
    # indented code runs since conditional argument is True
    vacation_days += 1
    print("vacation_days = ", vacation_days)
    print("we incremented vacation days")
# if block ends

vacation_days = 1
goals_met = False
if goals_met:
    # code does not run since conditional argument is False
    vacation_days += 1
    print("vacation_days = ", vacation_days)
    print("we incremented vacation days")
# if block ends
else:
    # else block starts
    print("vacation_days = ", vacation_days)
    print("we did NOT increment vacation days")
# else block ends

vacation_days = 1
goals_met = False
goals_exceeded = True
if goals_met:
    # code does not run since conditional argument is False
    vacation_days += 1
    print("vacation_days = ", vacation_days)
    print("we incremented vacation days")
elif goals_exceeded:
    print("This means that we exceeded our goals this quarter")
    print("We will increase our vacation days by two")
    vacation_days += 2
    print("vacation_days = ", vacation_days)
else:
    print("vacation_days = ", vacation_days)
    print("we did NOT increment vacation days")

# 0 , [] , '' = False

number_of_days = 3
if number_of_days > 5:
    print("#disruptive")
elif number_of_days < 3:
    print("#minimal")
else:
    print("#average")    