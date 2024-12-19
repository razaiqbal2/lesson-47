from abc import ABC

class Animal(ABC):
    def move(self):
        pass
class Snake(Animal):
    def move(self):
        print("Snake crawls on the ground")
class Frog(Animal):
    def move(self):
        print("Frog crawls on the ground")
class Human(Animal):
    def move(self):
        print("Human crawls on the ground")

s=Snake()
s.move()

s=Frog()
s.move()

s=Human()
s.move()