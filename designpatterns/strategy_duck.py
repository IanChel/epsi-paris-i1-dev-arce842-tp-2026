from abc import ABC, abstractmethod, abstractclassmethod

class QuackBehavior(ABC):
    
    @abstractmethod
    def quack(self):
        ...

class QuackQuack(QuackBehavior):
    
    def quack(self):
        print('Quack quack')
        
class SmallQuack(QuackBehavior):
    
    def quack(self):
        print('Small quack')

class FlyBehavior(ABC):
    
    @abstractclassmethod
    def fly(self):
        ...

class FlyToTheMoon(FlyBehavior):
    
    @classmethod
    def fly(self):
        print('Fly to the moon')

class FlyBackward(FlyBehavior):
    
    @classmethod
    def fly(self):
        print('Backward flying')


class Duck(ABC):
    
    def __init__(self, fly_behavior:FlyBehavior, quack_behavior:QuackBehavior):
        self.__fly_behavior = fly_behavior
        self.__quack_behavior = quack_behavior
    
    @abstractmethod
    def display(self):
        ...
        
    def fly(self):
        self.__fly_behavior.fly()
        
    def quack(self):
        self.__quack_behavior.quack()

    
class GreenDuck(Duck):
    
    def __init__(self):
        super().__init__(fly_behavior=FlyToTheMoon, quack_behavior=QuackQuack())

    def display(self):
        print('Greenduck says hello')
    
class MallardDuck(Duck):

    def __init__(self):
        super().__init__(fly_behavior=FlyBackward, quack_behavior=SmallQuack())

    def display(self):
        print('MallardDuck says hello')

class OtherDuck(Duck):

    def __init__(self):
        super().__init__(fly_behavior=FlyToTheMoon, quack_behavior=SmallQuack())
    
    def display(self):
        print('OtherDuck says hello')

if __name__ == '__main__':
    green_duck = GreenDuck()
    green_duck.display()
    green_duck.fly()
    green_duck.quack()
    
    mallard = MallardDuck()
    mallard.display()
    mallard.fly()
    mallard.quack()