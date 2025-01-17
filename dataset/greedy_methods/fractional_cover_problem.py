

from dataclasses import dataclass
from operator import attrgetter


@dataclass
class Item:
    weight: int
    value: int

    @property
    def ratio(self) -> float:
        return self.value / self.weight


def fractional_cover(items: list[Item], capacity: int) -> float:
    if capacity < 0:
        raise ValueError("Capacity cannot be negative")

    total_value = 0.0
    remaining_capacity = capacity

    
    for item in sorted(items, key=attrgetter("ratio"), reverse=True):
        if remaining_capacity == 0:
            break

        weight_taken = min(item.weight, remaining_capacity)
        total_value += weight_taken * item.ratio
        remaining_capacity -= weight_taken

    return total_value


if __name__ == "__main__":
    import doctest

    if result := doctest.testmod().failed:
        print(f"{result} test(s) failed")
    else:
        print("All tests passed")
