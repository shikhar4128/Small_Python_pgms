# This Python script is used to generate a random password of 8 characters. Each time the program is run, a new password will be generated randomly.
# The passwords generated will be 8 characters long and will have to include the following characters in any order:
#
# 2 uppercase letters from A to Z,
# 2 lowercase letters from a to z,
# 2 digits from 0 to 9,
# 2 punctuation signs such as !, ?, “, # etc.

import random

def shuffle(string):
    temp_list=list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)

upperCase1=chr(random.randint(65,90))
upperCase2=chr(random.randint(65,90))
lowerCase1=chr(random.randint(97,122))
lowerCase2=chr(random.randint(97,122))

digit1=random.randint(0,9)
digit2=random.randint(0,9)
punct=['!', '?', '"', '#']
punc1=random.choice(punct)
punc2=random.choice(punct)

password=upperCase1+upperCase2+lowerCase1+lowerCase2+str(digit1)+str(digit2)+punc1+punc2
print(shuffle(password))

