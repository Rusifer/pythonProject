class Unit:
    def __init__(self):
        print("Unit 생성자1")


class Flyable:
    def __init__(self):
        print("Flyable 생성자1")


class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()


# 드랍쉽
dropship = FlyableUnit()