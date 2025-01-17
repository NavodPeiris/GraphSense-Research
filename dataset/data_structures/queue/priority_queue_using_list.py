

class OverFlowError(Exception):
    pass


class UnderFlowError(Exception):
    pass


class FixedPriorityQueue:

    def __init__(self):
        self.queues = [
            [],
            [],
            [],
        ]

    def enqueue(self, priority: int, data: int) -> None:
        try:
            if len(self.queues[priority]) >= 100:
                raise OverflowError("Maximum queue size is 100")
            self.queues[priority].append(data)
        except IndexError:
            raise ValueError("Valid priorities are 0, 1, and 2")

    def dequeue(self) -> int:
        for queue in self.queues:
            if queue:
                return queue.pop(0)
        raise UnderFlowError("All queues are empty")

    def __str__(self) -> str:
        return "\n".join(f"Priority {i}: {q}" for i, q in enumerate(self.queues))


class ElementPriorityQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data: int) -> None:
        if len(self.queue) == 100:
            raise OverFlowError("Maximum queue size is 100")
        self.queue.append(data)

    def dequeue(self) -> int:
        if not self.queue:
            raise UnderFlowError("The queue is empty")
        else:
            data = min(self.queue)
            self.queue.remove(data)
            return data

    def __str__(self) -> str:
        return str(self.queue)


def fixed_priority_queue():
    fpq = FixedPriorityQueue()
    fpq.enqueue(0, 10)
    fpq.enqueue(1, 70)
    fpq.enqueue(0, 100)
    fpq.enqueue(2, 1)
    fpq.enqueue(2, 5)
    fpq.enqueue(1, 7)
    fpq.enqueue(2, 4)
    fpq.enqueue(1, 64)
    fpq.enqueue(0, 128)
    print(fpq)
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq)
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())


def element_priority_queue():
    epq = ElementPriorityQueue()
    epq.enqueue(10)
    epq.enqueue(70)
    epq.enqueue(100)
    epq.enqueue(1)
    epq.enqueue(5)
    epq.enqueue(7)
    epq.enqueue(4)
    epq.enqueue(64)
    epq.enqueue(128)
    print(epq)
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq)
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())


if __name__ == "__main__":
    fixed_priority_queue()
    element_priority_queue()
