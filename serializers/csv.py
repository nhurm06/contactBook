#!/usr/bin/env python3
'''
csv child class of the Serializer
'''
import csv
from serializers.serializer import Serializer


class csvSerializer(Serializer):
    '''
    Subclass of the Serializer for csv
    '''
    _format = "csv"
    def decode(self,path):
        '''
        Reads file path on disk and decodes to Contact objects
        :param path: str
        :return: [Contact]
        '''
        reader = csv.DictReader(self.open(path))
        from contacts import Contact
        results = [Contact.dictToContact(line) for line in reader]
        self.close()
        return results
    def encode(self,data):
        '''
        Encodes Contact object
        :param data: [Contact]
        :return: dict
        '''
        from contacts import Contact
        return [Contact.contactToDict(x) for x in data]
    def write(self,path,data):
        '''
        Overriding the Base write function due to how CSV files are written
        :param path: str
        :param data: dict
        :return: None
        '''
        header = ["name", "address", "phone"] ##Will need updating if more fields are added
        with open(path,"w",newline="") as f:
            writer = csv.DictWriter(f,fieldnames=header)
            writer.writeheader()
            writer.writerows(self.encode(data))