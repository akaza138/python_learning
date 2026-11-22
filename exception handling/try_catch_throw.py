# In python there are three things in exception handling which is try ,throw,except and finally
#in this example we are going to see how to use try and except in python
inp = input("enter any thing")
try:
    inp2=int(inp)
    print("sucessfully conerted")
except Exception:
    print("Cannot convert to int")
# you can enter multiple except
# finally block always exceute
finally:
    print("Error handled or output is arrived")
'''
Exception	Cause
ZeroDivisionError	Dividing by zero
ValueError	Right type, wrong value (int("abc"))
TypeError	Wrong type ("a" + 1)
IndexError	List index out of range
KeyError	Missing dictionary key
FileNotFoundError	File doesn’t exist
AttributeError	Object has no such attribute
NameError
'''