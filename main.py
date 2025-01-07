#Alarm clock

import pygame   #sound effects
import time     #time module
import datetime #time in strings

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time} ")
    sound_file = "C:/Users/morko/PycharmProjects/pythonProject/Between The Spaces - The Soundlings.mp3"

    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if (current_time == alarm_time):
            print("WAKE UP, ITS THE FIRST OF THE MONTH")
            time.sleep(0.5)
            is_running = False
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the time for the alarm (HH:MM:SS) : ")
    set_alarm(alarm_time)