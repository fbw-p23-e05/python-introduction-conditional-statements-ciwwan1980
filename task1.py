# Your task is to write a Python program to calculate the sum of three integers given (prompted) by user.  
# If the values are equal then calculate triple value of their sum.  
# Print out an appropriate message to the user.

# - Some of your results could look like this:


sum=0

for _ in range(3):
    number1= int(input("enter the firs number: "))
    number2=int(input("enter the second number: "))
    number3= int(input("enter the third number: "))
    sum=number1+number2+number3
    print(sum, "sum is here")
    break



