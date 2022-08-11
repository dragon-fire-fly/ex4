########### Exercise 4 #############
#---- Task 1 ----#

from cmath import sqrt

round = 1

while round < 4:
    num1 = int(input("Enter first whole number: "))
    num2 = int(input("Enter second whole number: "))
    num1_big = False
    num2_big = False
    big_numbers = False
    round += 1
    if num1 > num2:
        print(f"{num1} is bigger than {num2}")
        print("Numbers are not equal")
    elif num1 < num2:
        print(f"{num2} is bigger than {num1}")
        print("Numbers are not equal")
    elif num1 == num2:
        print(f"{num1} is the same as {num2}")
        print("Numbers are equal")
    if num1 > 1000:
        num1_big = True
        print("Number 1 is big")
    if num2 > 1000:
        num2_big = True
        print("Number 2 is big")
    if num1_big == True and num2_big == True:
        big_numbers = True
        print("Both numbers are big!")
        print(f"big_numbers is set to {big_numbers}")
    if num1 < 0:
        print(f"{num1} is a negative number")
    if num2 < 0:
        print(f"{num2} is a negative number")
    print(f"{num1} is a big number: {num1_big}")
    print(f"{num2} is a big number: {num2_big}")
    if sqrt(num1) == num2:
        print(f"{num2} is the square root of {num1}")
    elif sqrt(num2) == num1:
        print(f"{num1} is the square root of {num2}")
    if num1 % num2 == 0:
        print(f"{num1} is cleanly divisible by {num2}")
    else:
        print(f"{num1} is not cleanly divisible by {num2}. The remainder is {num1%num2}")
    if num2 % num1 == 0:
        print(f"{num2} is cleanly divisible by {num1}")
    else:
        print(f"{num2} is not cleanly divisible by {num1}. The remainder is {num2%num1}")
    

    

# #---- Task 2 ----#

#### if/elif/else version ####

user_month = input("Choose a month: ").capitalize()

if user_month == "January" or user_month == "Jan" or user_month == "Januar":
    print(f"{user_month} has 31 days")
elif user_month == "February" or user_month == "Feb" or user_month == "Februar":
    print(f"{user_month} has 28 days")
elif user_month == "March" or user_month == "Mar" or user_month == "März":
    print(f"{user_month} has 31 days")
elif user_month == "April" or user_month == "Apr":
    print(f"{user_month} has 30 days")
elif user_month == "May" or user_month == "Mai":
    print(f"{user_month} has 31 days")
elif user_month == "June" or user_month == "Jun" or user_month == "Juni":
    print(f"{user_month} has 30 days")
elif user_month == "July" or user_month == "Jul" or user_month == "Juli":
    print(f"{user_month} has 31 days")
elif user_month == "August" or user_month == "Aug":
    print(f"{user_month} has 31 days")
elif user_month == "September" or user_month == "Sep":
    print(f"{user_month} has 30 days")
elif user_month == "October" or user_month == "Oct" or user_month == "Oktober":
    print(f"{user_month} has 31 days")
elif user_month == "November" or user_month == "Nov":
    print(f"{user_month} has 30 days")
elif user_month == "December" or user_month == "Dec" or user_month == "Dezember":
    print(f"{user_month} has 31 days")



#### Dictionary version ####

months_dict = {
    "January": 31,
    "February": 28,
    "March": 31, 
    "April": 30, 
    "May": 31, 
    "June": 30, 
    "July": 31, 
    "August": 31, 
    "September": 30, 
    "October": 31, 
    "November": 30,
    "December":31,
}

user_month = input("Choose a month: ").capitalize()

print(f"{user_month} has {months_dict[user_month]} days")



#### List version ####
months = [
    "January", 
    "February", 
    "March", 
    "April", 
    "May", 
    "June", 
    "July", 
    "August", 
    "September", 
    "October", 
    "November",
    "December"]

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

user_month = input("Choose a month: ").capitalize()

for indexnum, month in enumerate(months): # enumerate gives the index number (need 2 variables (variable unpacking))
    if month == user_month:
        print(days[indexnum])


print(f"{user_month} has {days[indexnum]} days")