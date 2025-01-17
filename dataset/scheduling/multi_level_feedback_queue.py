from collections import deque


class Process:
    def __init__(self, process_name: str, arrival_time: int, burst_time: int) -> None:
        self.process_name = process_name  
        self.arrival_time = arrival_time  
        
        self.stop_time = arrival_time
        self.burst_time = burst_time  
        self.waiting_time = 0  
        self.turnaround_time = 0  


class MLFQ:

    def __init__(
        self,
        number_of_queues: int,
        time_slices: list[int],
        queue: deque[Process],
        current_time: int,
    ) -> None:
        
        self.number_of_queues = number_of_queues
        
        self.time_slices = time_slices
        
        self.ready_queue = queue
        
        self.current_time = current_time
        
        self.finish_queue: deque[Process] = deque()

    def calculate_sequence_of_finish_queue(self) -> list[str]:
        sequence = []
        for i in range(len(self.finish_queue)):
            sequence.append(self.finish_queue[i].process_name)
        return sequence

    def calculate_waiting_time(self, queue: list[Process]) -> list[int]:
        waiting_times = []
        for i in range(len(queue)):
            waiting_times.append(queue[i].waiting_time)
        return waiting_times

    def calculate_turnaround_time(self, queue: list[Process]) -> list[int]:
        turnaround_times = []
        for i in range(len(queue)):
            turnaround_times.append(queue[i].turnaround_time)
        return turnaround_times

    def calculate_completion_time(self, queue: list[Process]) -> list[int]:
        completion_times = []
        for i in range(len(queue)):
            completion_times.append(queue[i].stop_time)
        return completion_times

    def calculate_remaining_burst_time_of_processes(
        self, queue: deque[Process]
    ) -> list[int]:
        return [q.burst_time for q in queue]

    def update_waiting_time(self, process: Process) -> int:
        process.waiting_time += self.current_time - process.stop_time
        return process.waiting_time

    def first_come_first_served(self, ready_queue: deque[Process]) -> deque[Process]:
        finished: deque[Process] = deque()  
        while len(ready_queue) != 0:
            cp = ready_queue.popleft()  

            
            if self.current_time < cp.arrival_time:
                self.current_time += cp.arrival_time

            
            self.update_waiting_time(cp)
            
            self.current_time += cp.burst_time
            
            cp.burst_time = 0
            
            cp.turnaround_time = self.current_time - cp.arrival_time
            
            cp.stop_time = self.current_time
            
            finished.append(cp)

        self.finish_queue.extend(finished)  
        
        return finished

    def round_robin(
        self, ready_queue: deque[Process], time_slice: int
    ) -> tuple[deque[Process], deque[Process]]:
        finished: deque[Process] = deque()  
        
        for _ in range(len(ready_queue)):
            cp = ready_queue.popleft()  

            
            if self.current_time < cp.arrival_time:
                self.current_time += cp.arrival_time

            
            self.update_waiting_time(cp)
            
            if cp.burst_time > time_slice:
                
                self.current_time += time_slice
                
                cp.burst_time -= time_slice
                
                cp.stop_time = self.current_time
                
                ready_queue.append(cp)
            else:
                
                self.current_time += cp.burst_time
                
                cp.burst_time = 0
                
                cp.stop_time = self.current_time
                
                cp.turnaround_time = self.current_time - cp.arrival_time
                
                finished.append(cp)

        self.finish_queue.extend(finished)  
        
        return finished, ready_queue

    def multi_level_feedback_queue(self) -> deque[Process]:

        
        for i in range(self.number_of_queues - 1):
            finished, self.ready_queue = self.round_robin(
                self.ready_queue, self.time_slices[i]
            )
        
        self.first_come_first_served(self.ready_queue)

        return self.finish_queue


if __name__ == "__main__":
    import doctest

    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    number_of_queues = 3
    time_slices = [17, 25]
    queue = deque([P1, P2, P3, P4])

    if len(time_slices) != number_of_queues - 1:
        raise SystemExit(0)

    doctest.testmod(extraglobs={"queue": deque([P1, P2, P3, P4])})

    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    number_of_queues = 3
    time_slices = [17, 25]
    queue = deque([P1, P2, P3, P4])
    mlfq = MLFQ(number_of_queues, time_slices, queue, 0)
    finish_queue = mlfq.multi_level_feedback_queue()

    
    print(
        f"waiting time:\
        \t\t\t{MLFQ.calculate_waiting_time(mlfq, [P1, P2, P3, P4])}"
    )
    
    print(
        f"completion time:\
        \t\t{MLFQ.calculate_completion_time(mlfq, [P1, P2, P3, P4])}"
    )
    
    print(
        f"turnaround time:\
        \t\t{MLFQ.calculate_turnaround_time(mlfq, [P1, P2, P3, P4])}"
    )
    
    print(
        f"sequence of finished processes:\
        {mlfq.calculate_sequence_of_finish_queue()}"
    )
