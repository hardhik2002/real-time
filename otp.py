# generating otp numbers
from random import *
x=[randint(1,9),randint(1,9),randint(1,9),randint(1,9)]
def otp():
    print("Your one time password is:",end="")
    for i in x:
        print(i,end="")
otp()




