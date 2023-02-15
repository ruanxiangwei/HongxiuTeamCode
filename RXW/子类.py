from 父类 import Dog
from 属性方法类 import leg

class dog_baby(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.Leg = leg(5)

    def sit(self):
        print("坐下下")