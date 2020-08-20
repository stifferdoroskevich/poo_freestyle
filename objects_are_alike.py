from poo import Contact, Suppliers

a = Contact("Lando Norris", "lando.n@gmail.com")
print(a.name, a.email)

b = Suppliers("Michael Schumacher", "michael@ferrari.com")
print(b.name, b.email)
b.order(88)

for contact in a.all_contacts:
    print(contact.name)