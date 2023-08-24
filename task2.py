
# Your task is to write a Python program to get the difference between a two given numbers (prompted by user).  
# If the first number is greater than second then calculate double difference between numbers.  
# Otherwise calculate the **absolute** difference between numbers.  
# Print out an appropriate message to the user.


first_number = int(input("First number: "))
second_number = int(input("Second number: "))

if first_number > second_number:
    difference = (first_number - second_number) * 2
    print(difference, "difference")
    print("The result of calculation is", difference)
else:
    difference = abs(first_number - second_number)
    print("The result of calculation is", difference)