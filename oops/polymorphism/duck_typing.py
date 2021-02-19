class Swift:
    def start(self):
        print("swift car start")
    def accelerate(self):
        print("swift car accelerate")
    def stop(self):
        print("swift car stop")

class Seltos:
    def start(self):
        print("seltos car start")
    def accelerate(self):
        print("seltos car accelerate")
    def stop(self):
        print("seltos car stop")

class Person:
    def person(self,car):
        car.start()
        car.accelerate()
        car.stop()
sw=Swift()
se=Seltos()
p=Person()
p.person(sw)
p.person(se)