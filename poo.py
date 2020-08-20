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
    
class Contact: # basic inheritance
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

'''What if some contacs are also suppliers that we need to order supplies from?
   We could add an *order*, but that would allow people to accidentally order things from contacts'''

class Suppliers(Contact):
    def order(self, order):
        print("If this were a real system we would send order {0} to {1}, order {0} again".format(order, self.name))
