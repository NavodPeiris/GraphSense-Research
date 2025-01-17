
from __future__ import annotations


def allocation_num(number_of_bytes: int, partitions: int) -> list[str]:
    if partitions <= 0:
        raise ValueError("partitions must be a positive number!")
    if partitions > number_of_bytes:
        raise ValueError("partitions can not > number_of_bytes!")
    bytes_per_partition = number_of_bytes // partitions
    allocation_list = []
    for i in range(partitions):
        start_bytes = i * bytes_per_partition + 1
        end_bytes = (
            number_of_bytes if i == partitions - 1 else (i + 1) * bytes_per_partition
        )
        allocation_list.append(f"{start_bytes}-{end_bytes}")
    return allocation_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
