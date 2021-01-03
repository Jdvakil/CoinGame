# This program is written to collect data values of coins and add them up to find see is the total amount of coins will match upto a
# dollar or be less than a dollar or exceed a dollar.
print("Please enter as a whole number")
# input section ...here we will collect data from the customer to proceed to the proccessing and output
number_of_pennies = int(input("How many pennies do you have? : "))
# this step converts the total number of pennies to its monetary value
number_of_pennies = float(number_of_pennies * 0.01)

number_of_nickels = int(input("How many nickels do you have? : "))
# this step converts the total number of nickels to its monetary value
number_of_nickels = float(number_of_nickels * 0.05)

number_of_dimes = int(input("How many dimes do you have? : "))
# this step converts the total number of dimes to its monetary value
number_of_dimes = float(number_of_dimes * 0.10)

number_of_quarters = int(input("How many quarters do you have? : "))
# this step converts the total number of quarters to its monetary value
number_of_quarters = float(number_of_quarters * 0.25)

# process section ... here we will total up the input values to see if the total amount of coins will match upto a dollar or be less than a dollar or exceed a dollar.
total = float(number_of_pennies + number_of_nickels +
              number_of_dimes + number_of_quarters)

# output section ... here we will see if the total amount of coins will match upto a dollar or be less than a dollar or exceed a dollar.
if total == 1:
    print("Congratulations your total was exactly $1, therefore you've won the game!!")
elif total < 1:
    print("Sorry, your total was", total, ", which is less than a dollar")
else:
    # sets the value that the user was off by and rounds it to the second decimal .
    remain = total - 1
    print("Sorry, your total was", total,
          ", which is", round(remain, 1), "more than a dollar")
