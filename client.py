#client.py
# This file is for asking input from the user. This application is text-based in terminal.
# Sources:
# How to communicate with server: https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client
# And the same tutorial as with server side: https://docs.python.org/3/library/xmlrpc.server.html#simplexmlrpcserver-example
# How to use dictionaries: https://www.w3schools.com/python/python_dictionaries.asp
# 
import xmlrpc.client

def choices(): 
    print("What would you like to do:")
    print("1) Send a note to server")
    print("2) Get the notes about specific topic from the server")
    print("0) End program")
    choice = int(input("Your choice: "))
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
            confirm = input("Send request (yes/no): ")
            if (confirm == "yes" or confirm == "Yes"):
                print(s.addNote(topic, noteName, text, timestamp))
            else:
                topic = input("Give topic for the note: ")
                noteName = input("Give name for the note: ") 
                text = input("Give text for the note: ")
                timestamp = input("Give timestamp for the note: ")
        elif(choice == 2): 
            print("Receiving the notes from server")
            topicName = input("Give name of topic you want to search for: ")
            notes = s.listNotes(topicName)
            i = 1
            if (len(notes) == 0):
                print("No notes found")
            if (len(notes) != 0):
                for note in notes:
                    print("Note #" + str(i))
                    print("name: " + note["name"])
                    print("text: " + note["text"])
                    print("timestamp: " + note["timestamp"])
                    i = i + 1
        elif(choice == 0):
            print("Closing program, thank you..")
            break
        else:
            print("Unknown choice, choose 0,1 or 2!")


main()
