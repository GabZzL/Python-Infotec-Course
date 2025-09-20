# Superclass
class Animal:
    def eat(self):
        print('eating!!!')

# Subclass
class Dog(Animal):
    def bark(self):
        print('wof wof!!')
        
my_dog = Dog()

my_dog.bark()
my_dog.eat()

print(issubclass(Dog, Animal))
print(isinstance(my_dog, Dog))