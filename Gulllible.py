#short and simple program, you can learn the secret and subtle art of keeping a gullible person busy for hours.

import sys

while True:
    print("Do you want to know how to keep a gullible person busy for hours? Y/N")
    resp=input().lower()

    if resp in 'yes y':
        continue
    elif resp in 'no n':
        print('Ok fine, I will not tell.Thank you.Have a nice day!')
        sys.exit()
    else:
        print(f'"{resp}" is not a valid yes/no response')