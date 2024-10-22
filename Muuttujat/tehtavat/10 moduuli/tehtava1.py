class Elevator:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.floor = lower

    def movement(self, floor):
        while self.floor != floor:
            if floor > self.floor:
                self.floor_up()
            elif floor < self.floor:
                self.floor_down()

        print("Elevator is on the chosen floor")
        return

    def floor_up(self):
        if self.floor < self.upper:
            self.floor = self.floor + 1
        print(f"Elevator is on {self.floor}")
        return

    def floor_down(self):
        if self.floor > self.lower:
            self.floor -= 1
        print(f"Elevator is on {self.floor}")
        return

hissi = Elevator(1, 10)
hissi.movement(3)
hissi.movement(5)