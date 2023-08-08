#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
num_str = str(number)
print("Last digit of " + num_str + " is " + num_str[-1]+ " and" , end=" ")
if int(num_str[-1]) > 5:
    print("is greater than 5")
elif int(num_str[-1]) == 0:
    print("is 0")
elif int(num_str[-1]) < 6 and not 0:
    print("is less than 6 and not 0")
