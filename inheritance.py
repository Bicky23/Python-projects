class Parent():
    """ Initializes a class parent """
    def __init__(self, eye_color, skin_color):
        self.eye_color = eye_color
        self.skin_color = skin_color
        print("Parent constructed")

class Child(Parent):
    """ Initializes a child class """
    def __init__(self, eye_color, skin_color, age):
        Parent.__init__(self, eye_color, skin_color)
        self.age = age
        print("Child constructed")

me = Child("blue","white",23)
print(me.eye_color, me.age)
