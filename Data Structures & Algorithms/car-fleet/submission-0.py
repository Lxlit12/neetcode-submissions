class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for p, s in cars:
            # Calculate time to arrive at target
            time = (target - p) / s
            
            # If the stack has a car ahead that takes MORE time, 
            # this current car catches up and merges (we don't push its time)
            if not stack or time > stack[-1]:
                stack.append(time)
                
        # The number of remaining times in the stack represents the number of fleets
        return len(stack)