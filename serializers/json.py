import json
import os
from serializers.serializer import Serializer
#!/usr/bin/env python3
'''
json child class of the Serializer
'''

class jsonSerializer(Serializer):
    '''
    Subclass of the Serializer for json
    '''
    _format = "json"

    def decode(self,data):
        '''
        Reads file path on disk and decodes to Contact objects
        :param path: str
        :return: [Contact]
        '''
        if os.path.exists(data):
            data = self.read(data)
        from contacts import Contact
        results = json.loads(data,object_hook=Contact.dictToContact)
        self.close()
        return results


    def encode(self,data):
        '''
        Encodes Contact object
        :param data: dict
        :return: json
        '''
        from contacts import Contact
        return json.dumps(data,default=Contact.contactToDict)