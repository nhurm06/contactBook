#!/usr/bin/env python3
'''
Interactive CLI for address book

Usage: main.py

@author Nicholas Hurm
'''

from os import system
import os.path
from api import ContactBook
from serializers.serializer import Serializer

def viewContacts(contacts):
    '''
    View selected Contacts
    :param contacts:
    :return:
    '''
    print("\nContacts\n")
    print(f'{"Name":25} {"Address":30} {"Phone":15}')
    print("-----------------------------------------------------------")
    for contact in contacts:
       print(f'{contact.name:20} {contact.address:25} {contact.phone:15}')

def filterContacts(contactBook):
    '''
    Uses the Contact.query method to search and filter the contacts
    :param contactBook:
    :return:
    '''
    print("\nFilter Contacts\n")
    queryString = input("> query: ")
    contacts = contactBook.filterContacts(queryString)
    viewContacts(contacts)

def loadContacts(contactBook):
    '''
    Interactive loop that loads contacts from file
    :param contactBook:
    :return: None
    '''
    while True:
        print("\nSelect file format to load")
        formats = Serializer.queryFormats()
        num =[]
        for i,format in enumerate(formats):
            num.append(i)
            print(f'{i})  {format}')

        choice = int(input("\nEnter your choice: "))
        if choice not in num:
            print("Choice is not valid")
            if input("\nDo you want to try again (y/n) ?: ").lower() == 'y':
                continue
            else:
                break
        format = formats[choice]
        path = input("> path to file: ")

        if not os.path.exists(path):
            print("File does Not exist")
            if input("\nDo you want to try again (y/n) ?: ").lower() == 'y':
                continue

        break

    contacts = (contactBook.importContacts(format,path))
    print(f'\nSuccessfully added {len(contacts)} contacts.\n')


def saveContacts(contactBook):
    '''
    Interactive loop that writes contacts out to file
    :param contactBook:
    :return: None
    '''
    while True:
        print("\nSelect file format to save")
        formats = Serializer.queryFormats()

        for i,format in enumerate(formats):

            print(f'{i})  {format}')
        choice = int(input("\nEnter your choice: "))
        if choice not in num:
            print("Choice is not valid")
            if input("\nDo you want to try again (y/n) ?: ").lower() == 'y':
                continue
            else:
                break
        format = formats[choice]
        path = input("> path to file: ")
        contactBook.exportContacts(format,path)
        if not os.path.exists(path):
            print("\nFile not written.")
        else:
            print("\n File written successfully")
        break



def addContact(contactBook):
    '''
    Add contact loop.
    :param contactBook:
    :return: None
    '''
    while True:
        print("\nPlease enter the following details: ")
        name = input("> Name: ")
        if not name:
            print("Name cannot be empty. Please try again.")
            name = input("> Name: ")
        address = input("> Address: ")
        phone = input("> Phone number: ")
        contact = contactBook.addContact(name = name, address = address, phone = phone)
        print("\n Contact information for {name} added successfully!".format(name=contact))
        print(contactBook.getContacts())

        if input("\nDo you want to add another Contact again (y/n) ?: ").lower() == 'y':
            continue
        else:
            break
def mainMenu(cb):
    '''
    Dynamically scale the main menu options
    :param cb: ContactBook
    :return: list
    '''
    choices = []
    choices.append(dict(tooltip="Add Contact",exec='addContact(cb)'))
    choices.append(dict(tooltip="View All Contacts", exec='viewContacts(cb.getContacts())'))
    choices.append(dict(tooltip="Filter Contacts", exec='filterContacts(cb)'))
    choices.append(dict(tooltip="Load Contacts", exec='loadContacts(cb)'))
    choices.append(dict(tooltip="Save Contacts", exec='saveContacts(cb)'))
    choices.append(dict(tooltip="Exit", exec='sys.exit(0)'))

    return choices

def main():
    '''
    Main loop
    :return: None
    '''
    cb = ContactBook()
    while True:
        system('cls')  # clears the console after every iteration

        print("------------ Contact Book ------------")
        print("")
        num = []
        menu = mainMenu(cb)
        for i,view in enumerate(menu):
            num.append(i)
            print(f'{i})   {view["tooltip"]}')

        choice = int(input("\nEnter your choice: "))
        if choice not in num:
            print(choice,num)
            print("Invalid Choice. Please Try Again.")
            continue
        eval(menu[choice]['exec'])


if __name__ == '__main__':
    main()