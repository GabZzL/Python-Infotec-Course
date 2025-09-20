# Superclass
class Animal:
    def noise(self):
        return 'Making a noise'
    
# Subclass, Overwrite the method
class Dog(Animal):
    def noise(self):
        return 'wof wof'

class Cat(Animal):
    def noise(self):
        return 'miau miau'
    
class Cow(Animal):
    def noise(self):
        return 'mu mu'
    
def animal_noise(animal):
    print(animal.noise())
    
if __name__ == '__main__':
    my_dog = Dog()
    my_cat = Cat()
    my_cow = Cow()
    
    animals = [my_dog, my_cat, my_cow]
    
    print('Animal Noises')
    
    for animal in animals:
        animal_noise(animal)
    