class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse = True)
        fleet = 0
        slowest = 0
        for pos,spd in cars:
            time = (target - pos) / spd
            if time > slowest:
                fleet += 1
                slowest = time
        return fleet