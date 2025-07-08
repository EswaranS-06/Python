class Animal():
    def speak(self):
        return "I am an animal"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
a = Animal()
d = Dog()
print(a.speak())  # → "I am an animal"
print(d.speak())  # → "Woof!"
