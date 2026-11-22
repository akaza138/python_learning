#closure function means that an inner function can refer the outer function 

#eg
def outer(meg):#outer function
    def inner():#inner function
        print(f"vanakam {meg} bro")

    return inner

po3w = outer("vishal")

po3w()