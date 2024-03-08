#client.py
# This file is for asking input from the user. This application is text-based in terminal.
# Sources:
# How to use dictionaries: https://www.w3schools.com/python/python_dictionaries.asp
import xmlrpc.client

def choices(): 
    print("What would you like to do:")
    print("1) Send note to the server")
    print("2) Get notes based on topic from server")
    print("0) End")
    choice = int(input("Your choice: "))
    print()
    return choice

def main(): 
    s = xmlrpc.client.ServerProxy('http://localhost:8000')
    while(True):
        choice = choices()
        if (choice == 1): 
            print("Sending note to server")
            topic = input("Give topic for the note: ")
            noteName = input("Give name for the note: ") 
            text = input("Give text for the note: ")
            timestamp = input("Give timestamp: ")
            print(s.addNote(topic, noteName, text, timestamp))
        elif(choice == 2): 
            print("Receiving the notes from server")
            topicName = input("Give name of topic you want to search for: ")
            notes = s.listNotes(topicName)
            i=1
            if (len(notes) != 0):
                for note in notes:
                    print("Note #" + str(i))
                    print("name: " + note["name"])
                    print("text: " + note["text"])
                    print("timestamp: " + note["timestamp"])
                    print()
                    i = i+1
            else:
                print("No notes found, try other topic!")
        elif(choice == 0):
            print("Closing program, thank you..")
            break
        else:
            print("Unknown choice, choose 0,1 or 2!")


main()
