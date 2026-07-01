import json
import os


def load_contacts():
    if not os.path.exists("contacts.json"):
        return {}

    with open("contacts.json", "r") as file:
        contacts = json.load(file)

    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):

    name = input("Enter contact name: ").strip().lower()

    if name in contacts:
        print("This contact already exists.")
        return

    phone = input("Enter phone number: ").strip()

    contacts[name] = phone
    save_contacts(contacts)
    print("Contact added successfully.")


def show_contacts(contacts) :

    if not contacts :
        print("you dont have any contact")
    else :
        for name, phone in contacts.items():
            print(name, phone)

def search_contact(contacts):
    print("\nSearch by:")
    print("1. Phone Number")
    print("2. Name")

    choice = input("Choose: ").strip().lower()

    if choice in ["2", "name"]:
        name = input("Enter name: ").strip().lower()

        if name in contacts:
            print(f"{name} -> {contacts[name]}")
        else:
            print("contact not found.")

    elif choice in ["1", "phone", "phone number"]:
        phone = input("Enter phone number: ").strip()

        found = False

        for name, number in contacts.items():
            if number == phone:
                print(f"{name} -> {number}")
                found = True
                break

        if not found:
            print("Phone number not found.")

    else:
        print("Invalid choice.")       


def remove_contacts(contacts) :

    print("they are your contacts : ")
    for name, phone in contacts.items():
        print(name,":" , phone)

    name = input("\nwhat is contact name ?? ").strip().lower()
    if name not in contacts :
        print("name not found")
    else :
        contacts.pop(name)
        save_contacts(contacts)
        print(f"{name} has removed")

def edit_contact(contacts):

    if not contacts:
        print("No contacts found.")
        return

    print("\nContacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

    current_name = input("\nWhich contact do you want to edit? ").strip().lower()

    if current_name not in contacts:
        print("Contact not found.")
        return

    print("\n1. Edit Name")
    print("2. Edit Phone")

    choice = input("Choose: ").strip()

    if choice == "1":

        new_name = input("New name: ").strip().lower()

        if new_name in contacts:
            print("This name already exists.")
            return

        contacts[new_name] = contacts.pop(current_name)

        print("Name updated successfully.")

    elif choice == "2":

        new_phone = input("New phone number: ").strip()

        contacts[current_name] = new_phone
        save_contacts(contacts)

        print("Phone updated successfully.")

    else:
        print("Invalid choice.")


contacts = load_contacts()


while True :

    print("====== Contact manager ======")
    print("1. show contacts .")
    print("2. add a contact .")
    print("3. remove a contact .")
    print("4. edit a contact .") 
    print("5. search contact .")
    print("6. exit .")


    choice = input("Select your option : ").lower().strip()

    if choice not in ["show" , "remove" , "add" , "edit" , "search" , "6" "exit" , "1" , "2" , "3" , "4" , "5"] :
        print("invalid choice !")
        continue

    if choice == "add" or choice == "2" :
        add_contact(contacts)

    elif choice == "show" or choice == "1" :
        show_contacts(contacts)
    
    elif choice == "remove" or choice == "3" :
        remove_contacts(contacts)

    elif choice == "edit" or choice == "4" :
        edit_contact(contacts)

    else:
        print("GOODBYE !")
        print("--" * 20)
        break