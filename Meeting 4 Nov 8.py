"""
We will be attempting an introductory J1 problem to show you the different STATUS your code might recieve after submitting.
J1 problems are the easiest problems on the CCC Junior.
"""

"""
STATUS: ACCEPTED(AC)
Usually shown as green or checkmark. Green is the best colour in CP cause it means your code is correct.
For this problem, the youngest, middle, and largest child creates an arithmetic sequence. Let the numbers be y,m,l.
We then have m - y = l - m. In order to find the age of the largest child, we have l = 2m - y = m + (m-y).
After inputting m and y using input(), we let the difference be m-y( subtraction is an arithmetic operators in python), so l = m + difference.
After this we print it out using print()

CODE:
"""
youngest = int(input()) # takes in an integer input and store this input in a variable "youngest"
middle = int(input()) # takes in int input and store in var "middle"
difference = middle - youngest # calculate the difference using subtraction operator in python
print(middle + difference) # print the sum of middle and difference using addition operator


"""
STATUS: WRONG ANSWER(WA)
Usually shown in red or just Wrong Answer. This means your code printed the incorrect output(something that is different to the answer)
Note that sometimes your code might print the correct output for SOME CASES while printing the incorrect output for other cases.
If we just print 18, we will get the first sample case since the answer is 18, but will probably fail all other cases since the input 
is different each time which means the output will probably be different.

CODE:
"""
print(18)


""" 
STATUS: COMPILATION ERROR(CE)
This occurs when your code doesn't run because you don't know how to code or you mistyped something. Anyways, it means that there is an error 
in your syntax.
If we just say "losa hardstuck silver" or some random stuff, Python wouldn't know what we are trying to do since this is not a valid line of code. 
Thus, we would get CE.

CODE:
"""

losa nosa hardstuck silver OTZ 


"""
STATUS: TIME LIMIT EXCEEDED(TLE)
This shows up when your program is too slow. Usually for easier problems like J1-3, you don't really need to worry about this. Basically, they are
telling us that our code is not optimized enough, meaning we are probably checking more things than we should. To get past TLE, we must reduce our
time complexity. This is measured using Big O Notation, which we will revisit once we can all solve J1-3.
For this problem, you actually have to TRY to get TLE in order to get TLE. Lets use a for loop that loops over a very large number. This will take 
Python a long time to run since we are checking a lot of numbers, thus getting TLE.

CODE:
"""
youngest = int(input())
middle = int(input())
for i in range(696696996043898395832): # we are checking over this huge number, which will take Python a long time
    middle = middle +1
difference = middle - youngest
print(middle + difference)

"""
STATUS: Memory Limit Exceeded(MLE)
This happens when your program used up too much memory. MLE is probably the rarest out of all of these and will probably not appear until harder
problems like hard J5/S2 to medium S3/S4. So you shouldn't really worry about this right now.
For this problem, I would argue that it is harder to come up with a code that MLEs than AC. We first create a list, then insert a lot of numbers
into the list, then insert this list into a bigger list and do this many times. This will use up a lot of memory since the bigger list is storing
a lot of stuff, causing MLE.

CODE:
"""
youngest = int(input())
middle = int(input())

diff = middle - youngest 
osa = middle + 0

L = [] # bigger list
for i in range(10000):
    arr = [] # list
    for j in range(100069):
        arr.append(0) # add number 0 to arr
    L.append(arr)
    
print(osa)

"""
If you don't know what some of these programs are doing, there are many online resources like the online Python tutorials posted on classroom. We
will probably go over most of these things later.
"""

