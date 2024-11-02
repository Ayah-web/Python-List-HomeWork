# python list homework

# exercise one: list of favorite fruits
fav_fruits = ["pomegranate","peach","pineapple","lychee","watermelon"]

# printing list
print(fav_fruits)

# exercise two: given list of colors
colors = ['red', 'blue', 'green', 'yellow', 'purple']

# print first colour
print(colors[0])

# print third colour
print(colors[2])

# print last colour
print(colors[-1])

# exercise three: list of numbers
numbers = [10, 20, 30, 40, 50]

# changing second element to 25
numbers[1] = 25

# adding 60 to end of the list
numbers.append(60)

# print final list of numbers
print(numbers)

# exercise four: given list of names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']

# new list including first three names
subset = names[0:3]

# print new list
print(subset)

# exercise five: list of 1-10
num = [1,2,3,4,5,6,7,8,9,10]

# loop to print each number squared
for num in num:
    print(num ** 2)
    
# exercise six: empty list
shopping_cart = []

# adding elements in list using .append()
shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("eggs")
 
# using .extend() function
shopping_cart.extend(['butter', 'cheese'])

# printing final list
print(shopping_cart)

# exercise seven: finding max nd min in list
numbers = [45, 22, 88, 56, 92, 33]

# max in list
print("max in this list is:", max(numbers))

# min in list
print("min in this list is ", min(numbers))

# exercise eight: given list of letters
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']

# count of a
print("the count of the letter a in this list is:", letters.count("a"))

# exercise nine: list of numbers one to ten
zero_to_ten = [1,2,3,4,5,6,7,8,9,10]

# list of even numbers being squared
even_squares = [zero_to_ten ** 2 for zero_to_ten in zero_to_ten if zero_to_ten % 2 == 0]

# print squares of even numbers
print(even_squares)

# exercise ten: given list, remove duplicates
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# empty list for unique num
unique_numbers = []

# loop for each num in list
for num in nums:
    # if-else statement for duplicates
    if nums.count(num) == 1 or num not in unique_numbers:
        unique_numbers.append(num)
        
# print list
print(unique_numbers)

# another solution
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# for loop and if statement to remove duplicates
for num in nums[:]:
    if nums.count(num) > 1:
        nums.remove(num)
        
# print unique numbers
print(nums)