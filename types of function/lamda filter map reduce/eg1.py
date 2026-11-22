#lambda function
'''it is the way of writting the function in a one line only by using the syntax:lambda argument:expression
'''
from functools import reduce
# eg for the lambda function
add=lambda a,b:a+b
print(add(10,20))

# map with lamda (it used to apply the lambda function in the every thing in the list) eg:
fruit=["apple","banana","orange"]
res=list(map(lambda fruit:fruit.upper(),fruit))
print(res)

#filter with lambda
num=[1,2,3,5,6,7,88,6]
rese=list(filter(lambda num:num%2==0,num))
print(rese)

# reduce is used to give final single value from the list like give the total
nums=[1,2,3,5,6,7,88,6]
rese=reduce(lambda a,b:a-b,nums)
print(rese)

