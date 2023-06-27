class Adder:
    def __init__(self, a:int, b:int) -> int:
        self.a = a
        self.b = b
    
    def input_func(self):
        self.a = input("A : ")
        self.b = input("B : ")
    
    def add(self):
        print(self.a + self.b)
    

class Multiplier(Adder):
    def multiply(self):
        self.input_func()
        print(self.a * self.b)

exam = Multiplier(0, 0)
exam.multiply()
