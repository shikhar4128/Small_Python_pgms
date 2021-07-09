def getMode():
    while True:
        print("Please select the mode encrypt (e) or decrypt (d)")
        mode=input().lower()

        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print("Please select either 'encrypt or e' or 'decrypt or d'")

def getMessage():
    print("Please enter the message")
    return input()

def getKey():
    print("Please enter the key: ")
    key=int(input())

    if (key >=1 and key <=26):
        return key
    else:
        print("Please enter a valid key between 1 and 26")

def translatedMsg(mode,message,key):
    if mode[0]=='d':
        key= -key

    translated=''

    for letter in message:
        if letter.isalpha():
            num=ord(letter)
            num+=key

            if letter.isupper():
                if num > ord('Z'):
                    num-=26
                elif num < ord('A'):
                    num+=26
            elif letter.islower():
                if num > ord('z'):
                    num-=26
                elif num < ord('a'):
                    num+=26

            translated+=chr(num)
        else:
            translated+=letter

    return translated

mode=getMode()
message=getMessage()
key=getKey()

print("Your translated message is: ")
print(translatedMsg(mode, message, key))

