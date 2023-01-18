class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print('Inhales and exhales')


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print('Breathing under water')

    def swim(self):
        print("move under water")


nemo = Fish()
nemo.breathe()
nemo.swim()