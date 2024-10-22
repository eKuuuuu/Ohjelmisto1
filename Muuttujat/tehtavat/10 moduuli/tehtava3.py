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

class House:
    def __init__(self, lower, upper, elevator_count):
        self.lower = lower
        self.upper = upper
        self.elevator_count = elevator_count
        self.elevators = []
        for i in range(elevator_count):
            elevator = Elevator(self.lower, self.upper)
            self.elevators.append(elevator)

    def move_elevator(self, elevator_num, what_floor):
        moving_elevator = self.elevators[elevator_num - 1]
        moving_elevator.movement(what_floor)

    def firealarm(self):
        for i in range(self.elevator_count):
            self.move_elevator(i, self.lower)
        return

firsthouse = House(1, 5, 3)

firsthouse.move_elevator(1, 3)

firsthouse.move_elevator(2, 4)

for h in firsthouse.elevators:
    print(f"Hissi on kerroksessa {h.floor}")

print("Palohälytys!")
firsthouse.firealarm()

print("Hissin sijanti palohälytyksen jälkeen:")
for example in firsthouse.elevators:
    print(f"Hissi on kerroksessa {example.floor}")