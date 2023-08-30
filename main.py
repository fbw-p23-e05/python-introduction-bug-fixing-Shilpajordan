### Task 1 - fix the FizzBuzz

""" three_mul = 'fizz'
five_mul = 'buzz'
mul_three_five ='fizzBuzz'
num1 = 3
num2 = 5 
max_num = 100
   
for i in range(1,max_num):
    # % or modulo division gives you the remainder 
    
    if i%num1 == 0 and i%num2 == 0:
        print(i, mul_three_five)
    elif i%num2 == 0:
        print(i, five_mul)
    elif i%num1 == 0 :
         print(i, three_mul) """
   

### :heavy_plus_sign: Task 2 - summing integers

""" n = 5
number = 1
sum = 0
while number <= 5:
    sum = sum + number
    number = number + 1
print("Sum =", sum) """

### :heavy_plus_sign: Task 3 - summing integers with range()

""" n = 5
sum = 0
i = 1
for i in range(n):
    i = i + 1
    sum = sum + i
print("Sum =", sum) """


### :heavy_plus_sign: Task 4 - printing in loops
# Program no. 1 with the bug:
""" for x in range(3):
    print(x)
 """
#Program no. 2 with the bug:    

""" for j in range(5):
    print("This is loop number",j) """

#Program no. 3 with the bug:

""" x = 10
while x > 0:
    print(x)
    x -= 1 """

#Program no. 4 with the bug:

""" countdown = 5
while countdown:
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!") """


### :heavy_plus_sign: Task 5 - summing three integers

""" x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))
result = 0
if x == y or y == z or x == z:
    print("Calculated sum is ", result)
else:
    result = x + y + z
    
    print("Calculated sum is ", result)
 """


 ### :heavy_plus_sign: Task 6 - summing two integers

""" x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y

if result >= 15 and result <= 20:
    sum = 20
    print("Calculated sum is ", sum)  
else:
    print("Calculated sum is ", result) """


### :heavy_plus_sign: Task 7 - swapping variables
""" 
a = input("First value: ")
b = input("Second value: ")

print("Before swapping: a =", a, " b = ",b)

temp = a
a = b
b = temp

print("After swapping: a = ", a, ", b =,", b) """

### :heavy_plus_sign: Task 8 - max and min values

""" x = input("First number: ")
y = input("Second number: ")
z = input("Third number: ")

print("The maximum value is ", float(max((x, y ,z))))
print("The minimum value is ", float(min((x, y ,z)))) """


### :heavy_plus_sign: Task 9 - conversion

""" x = input("Type your value 0 or 1 or a word: " )
if x .isdigit() and x == 0:
    conversion_x = int(x)
    print('Your entered value is now False')
elif x .isdigit() and x == 1:  
    conversion_x = int(x)
    print('Your entered value is now True')
elif x.isdigit != True:
     print('Your entered value is now ',x)     """  

#---------------------------------------another method--------------------------------------------------------------------------
x = input("Type your value: ")

if x == '0':
    x = False
elif x == '1':
    x = True
else:
    pass

print("Your entered value is now ", x)


### :heavy_plus_sign: Task 10 - divisible number
""" 
x = int(input("First number: "))
y = int(input("Second number: "))

if x % y == 0:
    print("First number is divisible by second number, result =", float(x // y))
elif y % x == 0:
    print("Second number is divisible by first number, result =", float(y // x))
else:
    print("Numbers are non-divisible!") """