
from dataclasses import dataclass
from operator import attrgetter


@dataclass
class Task:
    task_id: int
    deadline: int
    reward: int


def max_tasks(tasks_info: list[tuple[int, int]]) -> list[int]:
    tasks = sorted(
        (
            Task(task_id, deadline, reward)
            for task_id, (deadline, reward) in enumerate(tasks_info)
        ),
        key=attrgetter("reward"),
        reverse=True,
    )
    return [task.task_id for i, task in enumerate(tasks, start=1) if task.deadline >= i]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{max_tasks([(4, 20), (1, 10), (1, 40), (1, 30)]) = }")
    print(f"{max_tasks([(1, 10), (2, 20), (3, 30), (2, 40)]) = }")
