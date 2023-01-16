from send_message_to_person import *
from send_message_to_group import *

def app():
    while True:
        # Check whether user wants to send message to personal account or group
        group_vs_personal = input("\nWould you like to send a message to a group or to a personal account? "
                          "\nWrite 'G' for group or 'P' for personal account: ")

        if group_vs_personal == "G" or group_vs_personal == "P":
            break
        else:
            print("\nError, please try again!")

    if group_vs_personal == "G":
        return messageToGroup()

    elif group_vs_personal == "P":
        return messageToPerson()


app()