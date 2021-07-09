# The Collatz sequence is a sequence of numbers produced from a starting
# number n, following three rules:
# 1.If n is even, the next number n is n / 2.
# 2.If n is odd, the next number n is n * 3 + 1.
# 3.If n is 1, stop. Otherwise, repeat.

import sys

while True:
    print("Enter the number: ")
    resp=input()

    if not resp.isdecimal() or resp =='0':
        cont=input("Entered number should be greater than zero. Press 'y' to continue or quit with any key \n")
        if cont=='y':
            continue
        else:
            print("Good bye!")
            sys.exit()
    else:
        break

num=int(resp)
print(num,end=',')
while num > 1:
    if num % 2==0:
        num=num//2
    else:
        num=(num*3) +1
    print(num, end=',')




