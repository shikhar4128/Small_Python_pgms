# This program tests your reaction speed: When you see "DRAW", you have 0.3 seconds to press Enter. But careful, though. Press it before DRAW appears,
# and you lose. Are you the fastest keyboard in the west?
import random
import time,sys

print('Time to test your reflexes and see if you are the fastest')
print()
print('When you see "DRAW", you have 0.3 seconds to press Enter.')
print('But you lose if you press Enter before "DRAW" appears.')
print()
print('Press Enter to begin')

while True:
    print()
    print("It is high noon...")
    time.sleep(random.randint(20,50) / 10)
    print("DRAW")
    drawTime=time.time()
    print(f'Draw time is - {time.ctime(drawTime)}')
    input()
    timeElapsed=time.time() - drawTime

    if timeElapsed < 0.01:
        print('You drew before "DRAW" appeared! You lose.')
    elif timeElapsed > 0.5:
        timeElapsed=round(timeElapsed,4)
        print(f'You took {timeElapsed} seconds to draw. Too slow !')
    else:
        timeElapsed=round(timeElapsed,4)
        print(f'Woah!! You took {timeElapsed} seconds to draw')
        print('You are the fastest.You Win!!')

    print('Enter QUIT to stop, or press any key to play again')
    resp=input().upper()
    if resp=='QUIT':
        print('Thanks for playing!')
        sys.exit()

