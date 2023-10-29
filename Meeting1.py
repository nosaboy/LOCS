"""
The solutions will be in python.
It is best to familiarize yourselves with the following:
- variables
- input output
- math operators
- if statements
- for loops
Better explanations can be found with a quick google search. As always, feel free to email me if you are confused with something. 
"""

"""
Exercise 1 Add 2 numbers

input is what the user/people sends into the program.
output is what the program gives out as a response to the input
We need to build a program that can take two inputs that are numbers, and output their sum
"""

a = int(input()) # stores the input in a variable( a container used to store data)
b = int(input()) # we need to convert the input to integer, so we use int()

answer = a + b # you can use basic arithmetic operators in python. For example, "+" adds two numbers, "-" subtracts two numbers, "*" multiplication, "/" division
print(answer) # to output something, we use print() and place the output inside the brackets

"""
POTW
The number of Lonnies you have is an integer a. The number of Toonies you have is an integer b.
Given a and b, output the smallest positive integer amount that you cannot pay without change or pay at all using all of your coins.

Test data:
Input first number a: 1
Input second number b: 1
Expected output: 4
Explanation: 
You have 1 Lonnie and 1 Tonnie.
You can pay 1 dollar without change
	By paying with your Lonnie
You can pay 2 dollars without change
	By paying with your Tonnie
You can pay 3 dollars without change
By paying with your Lonnie and your Tonnie
You cannot pay 4 dollars since the maximum you can pay is 1+2 = 3 dollars.

Problem Link: https://codeforces.com/problemset/problem/1660/A

Explanation:
Let there be x Toonies. If there are 0 Loonies, we cannot pay 1 dollar since we only have Toonies. Thus we output 1.
If there is 1 Loonie, we can pay every value from 1 to 2x + 1. 
- For an even number 2c smaller or equal to 2x, we know that c < x, so we can always pay with c Toonies.
- For an odd number 2c + 1 where 2c + 1 <= 2x + 1, we know that c < x, so we can pay c Toonies + 1 Loonie.
If there is more than 1 Loonie, we know that we can already pay all values up to and including 2x + 1. After this, we can just keep going up until we run out.
Thus if there are y Loonies, we can pay up to 2x + y, so the answer must be one above that = 2x + y + 1.
"""

testcases = int(input()) # we first have to input the number of test cases we are given. Test cases are designed so that we can check multiple cases( run our program multiple times) in one file.
for i in range(testcases): # a for loop is a loop that repeats the program inside of it( indented code below). The number of times the loop repeats is the number of testcases. 
  Loonies,Toonies = input().split() # The input format in the problem are seperated by whitespaces. Thus, we must split the 2 numbers in the input using the .split() function.
  Loonies = int(Loonies) # we must now convert the input from string to integer
  Toonies = int(Toonies) # since the default input takes in things as a string
  
  if(Loonies == 0): # an if statement is used to implement a condition. Here, we want to say if there are 0 loonies, then we output 1
      print(1)
  else: # otherwise if Loonies does not equal 0
    print(2 * Toonies + Loonies + 1)



### --- A BRIEF EXPLANATION FOR PRACTICE PROBLEMS ON THE LAST SIDE --- ###

"""
Missing Number: https://cses.fi/problemset/task/1083
"""
  
