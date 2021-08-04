#Python script that creates an alarm clock
from datetime import datetime
from pygame import mixer


alarm_time = input("Please enter the alarm time to be set: HH:MM:SS\n")
alarm_hr=alarm_time[0:2]
alarm_min=alarm_time[3:5]
alarm_sec=alarm_time[6:8]
alarm_period=alarm_time[9:11]

print("Setting up alarm..")
now=datetime.now()
print(f'Current time is {now}')

key=1
while key:
    now=datetime.now()
    current_hr=now.strftime("%I")
    current_min=now.strftime("%M")
    current_sec=now.strftime("%S")
    current_period=now.strftime("%p")

    if (alarm_period==current_period):
        if (alarm_hr==current_hr):
            if (alarm_min==current_min):
                if (alarm_sec==current_sec):
                    print("Wake up!!")
                    mixer.init()  # initiate the mixer instance
                    mixer.music.load('alarm_sound.wav')  # loads the music, can be also mp3 file.
                    mixer.music.play()  # plays the music
                    key=input("Press the <Enter> key to stop the alarm.")


