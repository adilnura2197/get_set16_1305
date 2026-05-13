class Car:
    def __init__(self, name, speed):
        self.name = name
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def set_speed(self, new_speed):
        self.__speed = new_speed


c1 = Car('BMW', 250)

print(c1.name)
print(c1.get_speed())

c1.set_speed(300)

print(c1.get_speed())
