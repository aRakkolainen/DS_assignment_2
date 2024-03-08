from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xml.etree.ElementTree as ET
# This handles the server side of the application and is based on this website: https://docs.python.org/3/library/xmlrpc.server.html#simplexmlrpcserver-example
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Based on: https://www.w3schools.com/python/python_classes.asp
class Note():
    def __init__(self, name, text, timestamp):
        self.name = name
        self.text = text
        self.timestamp = timestamp

# Here is created the server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    # Function for adding notes to database
    def addNote(topicName, noteName, text, timestamp):
        try: 
            tree = ET.parse('db.xml')
            root = tree.getroot()
            topicFound = False
            # Checking if topic already exists
            for topic in root:
                if (topic.get('name') == topicName):
                    print("This topic already exists!")
                    newNote = ET.SubElement(topic, 'note')
                    newNote.set('name', noteName)
                    newNoteText = ET.SubElement(newNote, 'text')
                    newNoteText.text = text
                    newNoteTimestamp = ET.SubElement(newNote, 'timestamp')
                    newNoteTimestamp.text = timestamp
                    topicFound = True
            if (topicFound == False):
                print("This topic doesn't exist yet so adding new one!")
                newTopic = ET.SubElement(root, 'topic')
                newNote = ET.SubElement(newTopic, 'note')
                newNote.set('name', noteName)
                newNoteText = ET.SubElement(newNote, 'text')
                newNoteText.text = text
                newNoteTimestamp = ET.SubElement(newNote, 'timestamp')
                newNoteTimestamp.text = timestamp
                newTopic.set('name', topicName)
            tree.write("db.xml")
            return "Note saved successfully"
        except:
            print("Error occurred")
            return "Saving note failed!"
    server.register_function(addNote, 'addNote')
    # Function for listing notes within specific topic, this simply prints them because it was complicated to return all notes
    def listNotes(topicName):
        tree = ET.parse('db.xml')
        root = tree.getroot()
        notes = []
        #print(root.find('topic'))
        for topic in root.findall('topic'):
            if(topic.get('name') == topicName):
                print("Topic found, listing notes related to this")
                for note in topic.iter('note'):
                    name = note.get('name')
                    text = note.find('text').text
                    timestamp = note.find('timestamp').text
                    if(len(name) != 0 and len(text) != 0 and len(timestamp) != 0):
                        note = Note(name, text.strip(), timestamp.strip())
                        notes.append(note)
        return notes
    server.register_function(listNotes, 'listNotes')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        exit(0)
