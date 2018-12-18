# author : taukir ahmed
# this program is about to take a break after 2 hours repeatidly


import webbrowser
import time
def take_break():

    total_time = 3
    break_time = 0

    print("this program ")

    while break_time < total_time:
        time.sleep(3)
        webbrowser.open('https://www.youtube.com/')
        break_time = break_time + 1

take_break()