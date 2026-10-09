#Write a function called check_age(age) with these rules:
#If age is not an integer, return "Age should be an integer".
#If age is less than 0, return "Invalid age".
#If age is less than 18, return "Minor".
#Otherwise, return "Adult".
def check_age(age):
    if not isinstance(age , (int)):
        return "Age should be an integer"
    if age<0:
        return "Invalid age"
    if age <18 :
        return "Minor"
    else:
        return "Adult"
check_age()