#!/usr/bin/env python3
'''
json child class of the Serializer
'''

import fnmatch

class ContactList(list):
    '''
    Override the default list to include the query method
    '''
    def query(self, attr, query):
        '''
        Queries the Contact objects to filter results. Compliant with glob
        :param attr: str
        :param query: str
        :return: [Contact]
        '''
        matchingContacts = []
        for contact in self:
            if not getattr(contact,attr):
                raise
            if fnmatch.fnmatch(getattr(contact,attr),query):
                matchingContacts.append(contact)

        return matchingContacts


class Contact(object):
    '''
    The base class for the Contact Object.
    '''
    def __init__(self, name = None , address = None, phone = None, **kwargs):
        self.name = name
        self.address = address
        self.phone = phone

    def dictToContact(dct):
        '''
        Helper function to aid in deserialization
        :return: Contact
        '''
        return Contact(**dct)
    def contactToDict(obj):
        '''
        Helper function to aid in serialization
        :return: dict
        '''
        return obj.__dict__

    def __repr__(self):
        '''
        Human Readable representation of the Contact object
        :return: str
        '''
        return self.name


