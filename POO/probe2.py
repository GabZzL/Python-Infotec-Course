class Person:
    def __init__(self, name):
        self.__name = name
        
    # Decorator @property converts the method into a 'getter'   
    # you can call this method from the outside
    @property   
    def name(self):
        return self.__name
    
    # Decorator @name.setter (it needs to be equal to the property name)
    # Now you can assign a new value
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name.strip()) > 0:
            self.__name = new_name.strip()
        else:
            print('Insert a valid name')
    
person_one = Person('emilio')

person_one.name = 'armando'

print(person_one.name)