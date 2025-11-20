class dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self):
        return f"{self.name} is barking"
d1=dog("tommy",3)
print(d1.speak())
