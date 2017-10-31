import json
import hashlib

class Block(object):

    '''
     A class which handles a block while a node is running; 
    '''

    def __init__(self, dictX):

        ''' 
        header: {index; timestamp; data; previous_hash; nonce;}  
        '''

        for element in dictX.values():
            # first making sure dictX is a dictionary:
            if isinstance(element, dictX):
                for key, val in dictX.items():
                    setattr(self, key, val)

                if not hasattr(self, 'nonce'):
                    self.nonce = 'None'

                if not hasattr(self, 'hash'):
                    self.hash = self.create_hash_self()

    def create_hash_self(self):
        sha = hashlib.sha256()
        sha.update(self.header_string())
        return sha.hexdigest()

    def header(self):
        return str(self.index) + self.previous_hash + self.data + str(self.timestamp) + str(self.nonce)

    def save_self(self):
        chaindata_dir = 'chaindata'
        index_string = str(self.index).zfill(6)
        filename = '%s/%s.json' % (chaindata_dir, index_string)
        with open(filename, 'w') as block_file:
            json.dump(self.__dict__(), block_file)



