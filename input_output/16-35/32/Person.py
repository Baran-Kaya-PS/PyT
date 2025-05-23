class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def encode_in_dict(self):
        return {'name':self.name,'age':self.age}
    @staticmethod # Pour pouvoir appeler Person.decode_from_dict
    def decode_from_dict(obj):
        if isinstance(obj,dict) and 'name' in obj and 'age' in obj:
            return Person(obj['name'],obj['age'])
        return obj
    def __repr__(self):
        return f"Person(name={self.name},age={self.age})"