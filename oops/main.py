def add(**kwargv):
    for key,value in kwargv.items():
        return f"{key}: {value}"
    
print(add(name = "John", age = 30, city = "New York"))