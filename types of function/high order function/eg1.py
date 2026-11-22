# higer order function 
# normal function
'''
def gmail_creation(uname,domain):
    if domain == "gmail":
        return f"{uname}@{domain}"
    elif domain == "yahoo":
        return f"{uname}@{domain}"
    elif domain == "hotmail":
        return f"{uname}@{domain}"
    elif domain == "company":
        return f"{uname}@{domain}"
    else:
        return "invaild"

print(gmail_creation("vishal","gmail"))

#by using the hof

instead of add the company i want in the condition and in this we create the function for each and 
by not touching tne code 
'''
'''
# giving the function as input or argument for the another function 1
def  g_mail(uname,domain="gmail.com"):
    return f"{uname}@{domain}"

def y_mail(uname,domain="yahoo.com"):
    return f"{uname}@{domain}"

def build_email(uname,email_func):
    return email_func(uname)

print(build_email("vishal",g_mail))
'''
#return function as the output
def email (domain):
    def build_email(uname):
        return f"{uname}@{domain}"
    return build_email
# prebound logic
gmail=email("gmail.com")
yahoo=email("yahoo.com")

print(gmail("vishal"))
print(yahoo("vasanth"))