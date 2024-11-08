# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x=1
x+=3


# TODO: Multiply y by 2 using the *= operator
y=1
y*=2

# TODO: Divide x by y and store the result in a variable called 'result'
x=1
y=2
result= x/y

# TODO: Print the value of 'result'
print(result)

#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a=2
b=3
if a>b :
    print ("a is greater than b")
else:
    print("a is not greater than b")
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
a=2
b=3
modulus= b%2
modulus==0

# TODO: Create a condition that checks if c is less than or equal to a
a=2
c=4
a<=c

# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
a=2
b=3
c=4
final_condition=(a>b) or (modulus==0) and (c<=a)

# TODO: Print the value of 'final_condition'
print(final_condition)

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
print("Hey user, Can you please provide your test score:")
score= print

# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60:
x=70

if x >90:
    print("Graded A")
elif x==80:
    print("Graded B")
elif x==70:
    print("Graded C")
elif x==60:
    print("Graded D")
else:
    print("Failed")


#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1= input("Enter first number:")
num2= input("Enter second number:")

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Enter an operation( +, - ,*, /:")

# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "+":
    result = num1+num2
elif operation == "-":
    result = num1-num2
elif operation == "*":
    result = num1*num2
elif operation == "/":
    if num2 == 0 and operation=="/":
        print("Division by zero is not allowed ")
else:
       result = num1/num2


# TODO: Handle the case of division by zero
# TODO: Print the result of the operation
if num2 !=0:
    print("Result:", result)