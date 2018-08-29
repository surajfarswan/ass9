#ques1--name:-ZeroDivisionError

a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError as message:
    print(message)

#ques2
    
try:
    l=[1,2,3]
    print(l[3])
except IndexError as message:
    print(message)

#que3
    
An exception
NameError:Hi there

#que4

-5.0 
a/b result in 0 

#que5
    
print("PROGRAM FOR ImportError:")
import sys
try:
    from exception import myexception
except Exception as e:
    print(e)
print()

print("PROGRAM FOR ValueError:")
try:
    x=int(input("enter a number"))
    print(x)
except ValueError as message:
    print(message)
print()

print("PROGRAM FOR IndexError:")
try:
    l=[1,2,3]
    print(l[3])
except IndexError as message:
    print(message)
print()
