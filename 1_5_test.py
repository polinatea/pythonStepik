class MoneyBox:
    def __init__(self, capacity): # конструктор с аргументом – вместимость копилки
        self.capacity=capacity
    def can_add(self, v):
        if(self.capacity-v >=0):
            return True
        else: 
            return False    # True, если можно добавить v монет, False иначе

    def add(self, v):
        if(self.can_add(v)==True):
            self.capacity-=v   # положить v монет в копилку
            print(self.capacity)
        else:
            print('huy')

x=MoneyBox(5)
x.add(2)
x.add(3)
x.add(7)
print(x.capacity)