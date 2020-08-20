import math as m

class Point():
    "Represents a point in two-dimensional geometric coordinates"
    
    def __init__(self, x=99, y=99):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    def calculate_distance(self, other_point):
        return m.sqrt(
            (self.x - other_point.x)**2 + (self.y - other_point.y)**2 # pitagoras
            )
    

'''Instead of instantiating a normal list as our class variable, 
we create a new ContactList class that extends the built-in list data type. 
Then, we instantiate this subclass as our all_contacts list. '''

class ContactList(list):
    def search(self, name):
        "Return all contacts that contain the search value in their name"
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact: # basic inheritance
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

'''What if some contacs are also suppliers that we need to order supplies from?
   We could add an *order*, but that would allow people to accidentally order things from contacts'''

class Suppliers(Contact): # Extend class Contact
    def order(self, order):
        print("If this were a real system we would send order {0} to {1}, order {0} again".format(order, self.name))
