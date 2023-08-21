 #!/usr/bin/env python3
'''
API Class for interacting with the Contact Book
'''
import re
import os
from contacts import Contact,ContactList
from serializers.serializer import Serializer

class ContactBook(object):
    '''
    Main API access class. How users will interact with the Contact Book
    '''
    def __init__(self):
        self.contactList = ContactList()

    def addContact(self,name = None,address= None,phone = None):
        '''
        Add the contact to the contactList
        :param name: str
        :param address: str
        :param phone: str
        :return: Contact Object
        '''

        contact = Contact(name,address,phone)
        self.contactList.append(contact)
        return contact

    def filterContacts(self,queryString):
        '''
        Filter contacts based on Glob, compliant query
        :param queryString: str
        :return: [Contact]
        '''
        queryList = re.split(r'\,|and|AND|\&|\&\&',queryString)
        queryDict = dict(s.split("=") for s in queryList)
        results = self.contactList
        for key in queryDict.keys():
            print(key,queryDict[key])
            results = results.query(key,queryDict[key])
        return results

    def getContacts(self):
        '''
        Gets a list of Contact objects
        :return: [Contact]
        '''
        return self.contactList

    def exportContacts(self, format,path, contacts=None,filter=None):
        '''
        Serialize the contacts on disk

        :param format: str
        :param path: str
        :param contacts: list
        :param filter: str
        :return: bool
        '''
        if not contacts:
            contacts = self.contactList
        writer = Serializer(format)
        if filter:
            pass
        writer.write(path,contacts)
        if not os.path.exists(path):
            return False
        return True
    def importContacts(self, format, path):
        '''
        Deserialize disk formations to Contact Objects

        :param format: str
        :param path: str
        :return: [Contact]
        '''
        print(format,path)
        loader = Serializer(format)
        self.contactList.extend(loader.decode(path))
        return self.contactList
