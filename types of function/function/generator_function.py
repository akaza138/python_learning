'''
GENERATOR FUNCTION USING THE YEILD:
IT IS THE SPECIAL FUNCTION THAT USES THE YEILD KEWORD , TO RETURN THE VALUE ONE BY ONE INSTEAD OF ALL AT ONCE
'''
def get_num(n):
    for i in range(n):
        yield i

for num in get_num(234):
    print(num)
