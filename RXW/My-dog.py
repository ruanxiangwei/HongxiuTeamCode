from 父类 import Dog
from 子类 import dog_baby

my_dog = Dog('ym', 6)

print(f"name is {my_dog.name}")
print(f"age is {my_dog.age}")
my_dog.sit()
print(my_dog.roll_over())
num = 2
my_dog.change_girlfriend_num()
print(f"have {my_dog.read_girlfriend_num()} girlfriends")


my_baby_dog = dog_baby('one', 2)

my_baby_dog.sit()
my_baby_dog.Leg.put_log_num()
my_baby_dog.Leg.get_range()