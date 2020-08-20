import datetime

# Store the next available id for all new notes
last_id = 0
print("imported app module")

class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note'''
    
    def __init__(self, memo, tags=''):
        "Initialize a note. Set automatically a Unique Id and date"
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        "Determines if this note matches the filter. Case sensitive"
        return filter in self.memo or filter in self.tags

class Notebook:
    "Represent a collecion of notes"

    def __init__(self):
        "Initialize a notebook with an empty list"
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def  _find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
    
    def modify_memo(self, note_id, memo):
        self._find_note(note_id).memo = memo # refactored as _find_note

    def mofify_tags(self, note_id, tags):
        for note in self.notes: #leaved as example
            if note.id == note_id:
                note.tags = tags
                break
    
    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]



"""
Notes are short memos stored in a notebook
Each note should record the day it was written.
Each note can have tags added for easy querying.
It should be possible to modify notes.
We also need to be able to search for notes.

Note
-id
-memo
-tags
-creation_date
.match

Notebook
.add
.modify
.search
.list_all_notes
"""
