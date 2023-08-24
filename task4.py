# Your task is to write a Python program which accepts (prompts) the **float** radius of a circle from the user and compute its [area](https://www.mathsisfun.com/geometry/circle-area.html).  
# Round the result to two decimals!  
# Print out an appropriate message to the user.

# >Hint: You can import `pi` number from `math` module for convenience!


import math

radius=float(input(" Enter the radius: ")) 
area = math.pi * radius ** 2
print (area, "area")
rounded_area = round(area, 2)

print("The area of the circle is:", rounded_area)
