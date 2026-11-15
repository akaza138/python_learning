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