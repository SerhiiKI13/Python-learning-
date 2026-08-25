class Engine:
    def start(self):
        print("Engine started")
        
class Car:
    def __init__(self):
        self.engine = Engine()
        
car = Car()
car.engine.start()