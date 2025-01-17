
from collections import defaultdict


class AssignmentUsingBitmask:
    def __init__(self, task_performed, total):
        self.total_tasks = total  

        
        
        self.dp = [
            [-1 for i in range(total + 1)] for j in range(2 ** len(task_performed))
        ]

        self.task = defaultdict(list)  

        
        
        self.final_mask = (1 << len(task_performed)) - 1

    def count_ways_until(self, mask, task_no):
        
        if mask == self.final_mask:
            return 1

        
        if task_no > self.total_tasks:
            return 0

        
        if self.dp[mask][task_no] != -1:
            return self.dp[mask][task_no]

        
        total_ways_util = self.count_ways_until(mask, task_no + 1)

        
        
        if task_no in self.task:
            for p in self.task[task_no]:
                
                if mask & (1 << p):
                    continue

                
                
                total_ways_util += self.count_ways_until(mask | (1 << p), task_no + 1)

        
        self.dp[mask][task_no] = total_ways_util

        return self.dp[mask][task_no]

    def count_no_of_ways(self, task_performed):
        
        for i in range(len(task_performed)):
            for j in task_performed[i]:
                self.task[j].append(i)

        
        return self.count_ways_until(0, 1)


if __name__ == "__main__":
    total_tasks = 5  

    
    task_performed = [[1, 3, 4], [1, 2, 5], [3, 4]]
    print(
        AssignmentUsingBitmask(task_performed, total_tasks).count_no_of_ways(
            task_performed
        )
    )
