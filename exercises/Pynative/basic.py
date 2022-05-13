# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is greater than 1000, else return their sum.
def calculation(number1, number2):
        #calculate the product of two numbers
    product = number1 * number2
        #check if product is greater than 1000
    if product >= 1000:
        return product
    else:
        #return sum if the product is less than 1000
        return number1 + number2

result = calculation(40,30)
print(result)

result = calculation(20,30)
print(result)

# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
print("Printing current and prev number and their sum in a range (10)")
previous_num = 0

# loop 1 to 10
for i in range(1,11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, "Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i

# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
def get_characters_even_index(string1):
    print("Original string is ", string1)
    print("Printing only even index chars")
    size = len(string1)
    for i in range(0,size-1):
        if i%2 == 0:
            print(string1[i])

result = get_characters_even_index("pynative")
print(result)

