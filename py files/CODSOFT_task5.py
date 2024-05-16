#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone_number = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"

    
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contacts(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, name, updated_contact):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone_number = updated_contact.phone_number
                contact.email = updated_contact.email
                contact.address = updated_contact.address
                print(f"Contact '{name}' updated successfully.")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")

        
def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        select = int(input("Enter your choice: "))

        if select == 1:
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
            print("Contact added successfully.")
            
            
        elif select == 2:
            contact_book.view_contacts()
            
            
        elif select == 3:
            keyword = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contacts(keyword)
            if found_contacts:
                print("Search results:")
                for contact in found_contacts:
                    print(contact)
            else:
                print("No matching contacts found.")
                
                
        elif select == 4:
            name = input("Enter name of contact to update: ")
            updated_phone = input("Enter updated phone : ")
            updated_email = input("Enter updated email: ")
            updated_address = input("Enter updated address: ")
            updated_contact = Contact(name, updated_phone, updated_email, updated_address)
            contact_book.update_contact(name, updated_contact)
        elif select == 5:
            
            
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        elif select == 6:
            
            
            print("Program Terminated.")
            break
        else:
            print("Invalid Input!!!")

main()
        


# In[ ]:




