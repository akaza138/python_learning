'''
COMPOSED FUNCTION :
THE COMPOSED FUNCTION IS WHEN THE OUTPUT OF THE ONE FUNCTION BECOMAR THE INPUT OF THE ANOTHER FUNCTION
LIKE F(G(X))
'''
def add(x):
    return x+2
def mul(x):
    return x*2
def combine(x):
    return add(mul(x))

print(combine(2))