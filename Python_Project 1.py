Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#1
from math import pi
r = float(input ("Input the radius of the circle : 1.1"))
Input the radius of the circle : 1.1
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    r = float(input ("Input the radius of the circle : 1.1"))
ValueError: could not convert string to float: ''
print ("The area of the circle with radius " + str(1.1) + " is: " + str(pi * 1.1**2))
The area of the circle with radius 1.1 is: 3.8013271108436504
#2
fn= input("Enter Filename:Python")
Enter Filename:Python
f = fn.split("Python")
print ("Extension of the file is : .py" + f[-1])
Extension of the file is : .py
