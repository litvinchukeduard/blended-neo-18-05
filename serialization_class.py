
class Character:

    def __init__(self, serializer):
        self.serializer

    def save_to_file(self):
        self.serializer.save_to_file('file_path')

class Serialize:

    def save_to_file(self, file_path):
        raise NotImplementedError
    
    def load_from_file(self, file_path):
        raise NotImplementedError
    

class SerializeToJson(Serialize):

    def save_to_file(self, file_path):
        pass # implement
    
    def load_from_file(self, file_path):
        pass # implement


class SerializeToPickle(Serialize):

    def save_to_file(self, file_path):
        pass # implement
    
    def load_from_file(self, file_path):
        pass # implement


