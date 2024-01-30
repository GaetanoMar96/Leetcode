class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = []
        for t, p in zip(position, speed):
            cars.append((t,p))
        cars = sorted(cars, key=lambda x: x[0])
        fleet = 0
        while cars:
            p1, s1 = cars.pop()
            if not cars:
                fleet += 1
                break
            p2, s2 = cars.pop()
            t1 = (target - p1) / s1
            t2 = (target - p2) / s2
            if t2 <= t1: #they collide
                cars.append((p1, s1))
            else:
                cars.append((p2, s2))
                fleet += 1
        return fleet


        