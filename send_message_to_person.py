import pywhatkit
from random_sentence import random_sentence
from current_time import *


def messageToPerson():
    while True:
        # Get phone number of receiver
        phone_number = input("\nPlease enter phone number: ")
        if (phone_number[1:]).isdigit():
            break
        else:
            print("\nError, please try again!")


    while True:
        # Check whether user wants to send a personalized message or random
        personal_vs_general = input("\nWould you like to send write the message yourself or randomly send a kind sentence from our dataset?"
                                    "\nWrite 'W' to write the message or 'R' to randomly send a kind sentence: ")

        if personal_vs_general == "W":
            # Get message
            message = input("\nPlease write message: ")
            if len(message) > 0:
                break
            else:
                print("\nError, please try again!")

        elif personal_vs_general == "R":
            # Get receiver's name (to make message more personalized)
            name = input("\nPlease enter your friend's name: ")
            message = random_sentence().replace("NAME", name)
            if len(name) > 0:
                break
            else:
                print("\nError, please try again!")

        else:
            print("\nError, please try again!")


    while True:
        # Check whether user wants to send message now or at another time
        now_vs_then = input("\nWould you like to send your message now or at another time?"
                            "\nWrite 'N' for now or 'O' for another time: ")

        if now_vs_then == "N" or now_vs_then == "O":
            break
        else:
            print("\nError, please try again!")


    if now_vs_then == "N":
        hour = get_hour()
        if hour > 24:
            hour -= 24

        minute = get_minute() + 1
        if minute > 60:
            minute -= 60


    elif now_vs_then == "O":
        # Get time (hour)
        while True:
            hour = input("\nPlease enter hour as a number in the 24-format: ")
            if hour.isdigit() and len(hour) <= 2:
                if int(hour) >= 0 and int(hour) < 24:
                    break
                else:
                    print("\nError, please try again!")
            else:
                print("\nError, please try again!")

        # Get time (minute)
        while True:
            minute = input("\nPlease enter minute: ")
            if minute.isdigit() and len(minute) <= 2:
                if int(minute) >= 0 and int(minute) < 60:
                    break
                else:
                    print("\nError, please try again!")
            else:
                print("\nError, please try again!")



    pywhatkit.sendwhatmsg(phone_number, message, int(hour), int(minute), 7, True, 1)

