class Dog:
    name = ''
    age = 0
    _feeding = 'cannibalism'
    __fur = True
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print('wof wof!')
        
my_dog = Dog('Peluchin', 10)

print(my_dog.name)
print(my_dog._feeding)
my_dog.bark()
