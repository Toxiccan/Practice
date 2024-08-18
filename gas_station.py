class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        tot, current = 0, 0
        start = 0
        
        for i in range(n):
            tot += gas[i] - cost[i]
            current += gas[i] - cost[i]
            
            if current< 0:
                start= i + 1
                current = 0
        
        return start if tot >= 0 else -1



