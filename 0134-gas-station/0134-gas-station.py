class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        start_idx = 0
        total_gas = 0
        current_gas = 0

        for i in range(0, len(gas)):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                start_idx = i + 1
                current_gas = 0
        if total_gas >= 0:
            return start_idx
        return -1
