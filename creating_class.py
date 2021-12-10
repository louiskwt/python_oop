class Dog(object):
    # Initialisation of the Dog class instance
    def __init__(self, name, age):
        # Public attribute
        self.name = name
        self.age = age
        print('Nice you made a new pet!')

    def speak(self):
        print('Hi, I am', self.name, ' and I am', self.age)

    def talk(self):
        print('Bark!')


class Cat(Dog):
    def __init__(self, name, age, color):
        # Calling super class to inherit from Dog; python3 allows 0 arg for super
        super().__init__(name, age)
        self.color = color

    # Overriding talk
    def talk(self):
        print('Meow!')


lucy = Cat('lucy', 1, 'yellow')
lucy.speak()
lucy.talk()

jim = Dog('jim', 2)
jim.talk()
