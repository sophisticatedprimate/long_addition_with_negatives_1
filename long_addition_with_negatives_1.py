"""
Check out the official python docs to learn more about python programming!
https://docs.python.org/3/

Two addends are summed in python by using the addition operator (+) (more on this in long_addition_1.py).
Python (as well as most calculators) has the ability to handle negatives automatically using operator precedence.
Learn more at: https://docs.python.org/3/reference/expressions.html#operator-precedence

When dealing with negative values with calculators, it is useful to know the difference between a bitwise negative number, and the bitwise operation of subtraction.
Examples of negative values:
    -a
    (-a)
    x + (-a)
    x + -a    ~this is effectively the same as subtraction
Examples of subtraction:
    a - b - c - d
    a - -b    ~subtracting a negative is effectively the same as addition
Operations (of the same level) are performed left to right.

The primary thing to understand is that the computer does not understand.
What I mean by that is that the calculator operates on values it has stored blindly, and without consideration for what those values are or any limitations they may have.
The computer does not know that years are not supposed to be negative, that there are only 24 hours in a day, or that you squared a variable and the solution you have may not be real.
That being said, the computer is able to calculate large and obscure values at a moments notice.
Our goal is to reap the clear benefits of using a calculator while eliminating errors from its nuances.
We do that by having a clear understanding of both the theory of math (ie math by hand), and a basic understanding of how the calculator works internally (bitwise operations).
The difference becomes evident if you compare the solution sheet (long_addition_with_negatives_solutions.pdf) with the printout of this program (viewable at https://github.com/sophisticatedprimate/long_addition_1_with_negatives).
The solution manual uses the theory of negative numbers and logic to solve each exercise, while python bitwise logic can be more compared to a number line approach.
This becomes even more apparent in the long_addition_with_decimals_6.py program, in which the decimal ranges of several floats must be extended to include the full answer.

Learn more about bitwise operations at the following links:
    https://www.cs.cornell.edu/~tomf/notes/cps104/twoscomp.html
    https://www.cs.uaf.edu/2015/fall/cs301/lecture/10_05_bitwise.html
    https://faculty.etsu.edu/tarnoff/ntes2150/logic/bitwise.htm
    lookup terms: two's complement, x86 assembly, ARM assembly
    NOTE: you don't need to learn to program in assembly to figure out how a calculator works internally, but bitwise operations are typically explored in these lesson sets

To run the program: 
    1. Open a terminal on a computer with python 3 installed (works with v2 as well)
    2. Navigate to a directory containing this file (long_addition_with_decimals_1.py)
    3. Run the program with the following command: python3 long_addition_with_decimals_1.py
    4. A print out of the sums should appear after the cursor

If error:
    a. make sure python is installed (run: python3 --version)
    b. make sure you have the file installed and in the current directory
    c. if you are still having issues or see any general issues in the programming please report using the contact information at end of file.
"""

# Problem 1 
sum = 652 + -554  
print("{0:<5} + {1:<5} = {2:<6}".format(652,-554,sum)) 

# Problem 2 
sum = -509 + 68  
print("{0:<5} + {1:<5} = {2:<6}".format(-509,68,sum)) 

# Problem 3 
sum = 866 + 687  
print("{0:<5} + {1:<5} = {2:<6}".format(866,687,sum)) 

# Problem 4 
sum = -408 + -572  
print("{0:<5} + {1:<5} = {2:<6}".format(-408,-572,sum)) 

# Problem 5 
sum = 45 + -95  
print("{0:<5} + {1:<5} = {2:<6}".format(45,-95,sum)) 

# Problem 6 
sum = -283 + 503  
print("{0:<5} + {1:<5} = {2:<6}".format(-283,503,sum)) 

# Problem 7 
sum = -129 + -933  
print("{0:<5} + {1:<5} = {2:<6}".format(-129,-933,sum)) 

# Problem 8 
sum = -571 + -118  
print("{0:<5} + {1:<5} = {2:<6}".format(-571,-118,sum)) 

# Problem 9 
sum = -69 + 655  
print("{0:<5} + {1:<5} = {2:<6}".format(-69,655,sum)) 

# Problem 10
sum = -29 + 552  
print("{0:<5} + {1:<5} = {2:<6}".format(-29,552,sum)) 

# Problem 11
sum = -703 + 41  
print("{0:<5} + {1:<5} = {2:<6}".format(-703,41,sum)) 

# Problem 12
sum = -505 + -997  
print("{0:<5} + {1:<5} = {2:<6}".format(-505,-997,sum)) 

# Problem 13
sum = -844 + -142  
print("{0:<5} + {1:<5} = {2:<6}".format(-844,-142,sum)) 

# Problem 14
sum = -367 + -460  
print("{0:<5} + {1:<5} = {2:<6}".format(-367,-460,sum)) 

# Problem 15
sum = 996 + -645  
print("{0:<5} + {1:<5} = {2:<6}".format(996,-645,sum)) 

# Problem 16
sum = 82 + -68  
print("{0:<5} + {1:<5} = {2:<6}".format(82,-68,sum)) 

# Problem 17
sum = -7 + -229  
print("{0:<5} + {1:<5} = {2:<6}".format(-7,-229,sum)) 

# Problem 18
sum = 613 + 195  
print("{0:<5} + {1:<5} = {2:<6}".format(613,195,sum)) 

# Problem 19
sum = -497 + -289  
print("{0:<5} + {1:<5} = {2:<6}".format(-497,-289,sum)) 

# Problem 20
sum = 552 + 729  
print("{0:<5} + {1:<5} = {2:<6}".format(552,729,sum)) 

# Problem 21
sum = 615 + 121  
print("{0:<5} + {1:<5} = {2:<6}".format(615,121,sum)) 

# Problem 22
sum = -142 + 986  
print("{0:<5} + {1:<5} = {2:<6}".format(-142,986,sum)) 

# Problem 23
sum = 53 + -326  
print("{0:<5} + {1:<5} = {2:<6}".format(53,-326,sum)) 

# Problem 24
sum = 639 + -832  
print("{0:<5} + {1:<5} = {2:<6}".format(639,-832,sum)) 

# Problem 25
sum = -962 + 526  
print("{0:<5} + {1:<5} = {2:<6}".format(-962,526,sum)) 

# Problem 26
sum = 57 + -332  
print("{0:<5} + {1:<5} = {2:<6}".format(57,-332,sum)) 

# Problem 27
sum = -334 + -467  
print("{0:<5} + {1:<5} = {2:<6}".format(-334,-467,sum)) 

# Problem 28
sum = -178 + -362  
print("{0:<5} + {1:<5} = {2:<6}".format(-178,-362,sum)) 

"""
Contact information

General Queries: admin@sophisticatedprimate.com
Report errors, bugs, and problems at:
    email:  bug@sophisticatedprimate.com
    github: https://github.com/sophisticatedprimate/long_addition_with_negatives_1/issues
"""
