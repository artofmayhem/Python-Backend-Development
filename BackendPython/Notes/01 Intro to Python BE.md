# Python 101 - Introduction to Python chart

## Functions 
abs() => absolute value ex -5 => 5
sort() => sort a list in ascending order ex [1,3,2,4] => [1,2,3,4]
len() => length of a list ex [1,2,3,4] => 4
max() => maximum value in a list ex [1,2,3,4] => 4
min() => minimum value in a list ex [1,2,3,4] => 1
sum() => sum of all values in a list ex [1,2,3,4] => 10
range() => range of values in a list ex range(1,10) => [1,2,3,4,5,6,7,8,9] 
print(20%6) => 2   % represents modulus it is used to find remainder
other python functions are: 
obj() => object of a class ex obj = class()
dir() => list of all attributes and methods of a class ex dir(obj)
str() => converts a number to string ex str(5) => '5'
bin() => converts a number to binary string ex bin(5) => '101'
del list[0]=> deletes the first element in a list ex [1,2,3,4] => [2,3,4]
num = int(input("Enter a number: ")) => takes input from user and converts it to integer ex num = int(input("Enter a number: ")) => num = 5


## Data Types
[] => list
{} => dictionary
() => tuple
a list is a collection of values ex [1,2,3,4]
a dict = {'name':'John','age':'27','salary':'50000'} is a dictionary
    - a dict is a collection of key-value pairs like an object in javascript
    - a tuple is used to store a sequence of immutable values ex (1,2,3,4) or ("John","Doe", 1,2,3,4)
    - a tuple is a sequence of immutable values

## Imports from python math module
import math * => import all functions from math module
math.sqrt(25) => 5 square root of 25
math.factorial(5) => 120 factorial of 5 is 120
math.pow(2,3) => 8 power of 2 to the power of 3 is 8
math.pi => 3.141592653589793 returns the value of pi
math.e => 2.718281828459045 returns the value of e (natural logarithm base)
math.log(100,10) => 2.0 returns the logarithm of 100 to the base of 10 
math.log10(100) => 2.0 returns the logarithm of 100 to the base of 10
math.exp(2) => 7.38905609893065 returns the value of e to the power of 2
math.sin(math.pi/2) => 1.0 returns the sine of 90 degrees
math.cos(math.pi/2) => -1.0 returns the cosine of 90 degrees
math.tan(math.pi/4) => 1.0 returns the tangent of 45 degrees
math.asin(1) => 1.5707963267948966 returns the arcsine of 1
math.acos(1) => 0.0 returns the arccosine of 1
math.atan(1) => 0.7853981633974483 returns the arctangent of 1
math.degrees(math.pi/2) => 90.0 returns the angle in degrees of pi/2
math.radians(90) => 1.5707963267948966 returns the angle in radians of 90
math.ceil(2.1) => 3.0 returns the smallest integer greater than or equal to 2.1
math.floor(2.9) => 2.0 returns the largest integer less than or equal to 2.9
math.fabs(-2.9) => 2.0 returns the absolute value of -2.9

## other Python modules
import random
random.randint(1,10) => returns a random integer between 1 and 10
random.choice(['a','b','c','d']) => returns a random element from the list
random.shuffle(['a','b','c','d']) => shuffles the list
random.sample(['a','b','c','d'],2) => returns a list of 2 random elements from the list
random.uniform(1,10) => returns a random float between 1 and 10

import datetime
datetime.datetime.now() => returns the current date and time
datetime.datetime.today() => returns the current date
datetime.datetime.fromtimestamp(time.time()) => returns the current date and time from the time in seconds
datetime.datetime.strptime(date_string, format) => returns a datetime object from a string and a format
datetime.datetime.strftime(date_object, format) => returns a string from a datetime object and a format

import time
time.time() => returns the current time in seconds
time.sleep(5) => sleeps for 5 seconds

import os
os.getcwd() => returns the current working directory
os.chdir(path) => changes the current working directory to the specified path
os.listdir(path) => returns a list of files and folders in the specified path
os.path.exists(path) => returns true if the specified path exists
os.path.isfile(path) => returns true if the specified path is a file
os.path.isdir(path) => returns true if the specified path is a directory
os.path.getsize(path) => returns the size of the specified path in bytes
os.path.getmtime(path) => returns the last modified time of the specified path in seconds
os.path.getatime(path) => returns the last accessed time of the specified path in seconds
os.path.getctime(path) => returns the creation time of the specified path in seconds
os.path.join(path1, path2) => returns the path of path1 and path2 joined together
os.path.split(path) => returns a tuple of the path and the file name
os.path.splitext(path) => returns a tuple of the path and the file extension
os.path.basename(path) => returns the file name of the specified path
os.path.dirname(path) => returns the directory of the specified path
os.path.normpath(path) => returns the normalized path
os.path.abspath(path) => returns the absolute path
os.path.relpath(path) => returns the relative path
os.path.normcase(path) => returns the normalized path with case
os.path.expanduser(path) => returns the expanded path
os.path.expandvars(path) => returns the expanded path
os.path.dirname(path) => returns the directory of the specified path
os.path.basename(path) => returns the file name of the specified path
os.path.exists(path) => returns true if the specified path exists
os.path.isfile(path) => returns true if the specified path is a file
os.path.isdir(path) => returns true if the specified path is a directory
os.path.getsize(path) => returns the size of the specified path in bytes

import sys
sys.argv => returns the command line arguments
sys.exit(0) => exits the program with a status code of 0
sys.stdout.write('Hello World') => writes Hello World to the standard output
sys.stdout.flush() => flushes the standard output buffer
sys.stdin.readline() => reads a line from the standard input
sys.stdin.read() => reads all the data from the standard input
sys.stdin.readlines() => reads all the lines from the standard input
sys.stdin.fileno() => returns the file descriptor of the standard input
sys.stdout.fileno() => returns the file descriptor of the standard output
