






from __future__ import annotations

import numpy as np

test_claim_vector = [8, 5, 9, 7]
test_allocated_res_table = [
    [2, 0, 1, 1],
    [0, 1, 2, 1],
    [4, 0, 0, 3],
    [0, 2, 1, 0],
    [1, 0, 3, 0],
]
test_maximum_claim_table = [
    [3, 2, 1, 4],
    [0, 2, 5, 2],
    [5, 1, 0, 5],
    [1, 5, 3, 0],
    [3, 0, 3, 3],
]


class BankersAlgorithm:
    def __init__(
        self,
        claim_vector: list[int],
        allocated_resources_table: list[list[int]],
        maximum_claim_table: list[list[int]],
    ) -> None:
        self.__claim_vector = claim_vector
        self.__allocated_resources_table = allocated_resources_table
        self.__maximum_claim_table = maximum_claim_table

    def __processes_resource_summation(self) -> list[int]:
        return [
            sum(p_item[i] for p_item in self.__allocated_resources_table)
            for i in range(len(self.__allocated_resources_table[0]))
        ]

    def __available_resources(self) -> list[int]:
        return np.array(self.__claim_vector) - np.array(
            self.__processes_resource_summation()
        )

    def __need(self) -> list[list[int]]:
        return [
            list(np.array(self.__maximum_claim_table[i]) - np.array(allocated_resource))
            for i, allocated_resource in enumerate(self.__allocated_resources_table)
        ]

    def __need_index_manager(self) -> dict[int, list[int]]:
        return {self.__need().index(i): i for i in self.__need()}

    def main(self, **kwargs) -> None:
        need_list = self.__need()
        alloc_resources_table = self.__allocated_resources_table
        available_resources = self.__available_resources()
        need_index_manager = self.__need_index_manager()
        for kw, val in kwargs.items():
            if kw and val is True:
                self.__pretty_data()
        print("_" * 50 + "\n")
        while need_list:
            safe = False
            for each_need in need_list:
                execution = True
                for index, need in enumerate(each_need):
                    if need > available_resources[index]:
                        execution = False
                        break
                if execution:
                    safe = True
                    
                    for original_need_index, need_clone in need_index_manager.items():
                        if each_need == need_clone:
                            process_number = original_need_index
                    print(f"Process {process_number + 1} is executing.")
                    
                    need_list.remove(each_need)
                    
                    available_resources = np.array(available_resources) + np.array(
                        alloc_resources_table[process_number]
                    )
                    print(
                        "Updated available resource stack for processes: "
                        + " ".join([str(x) for x in available_resources])
                    )
                    break
            if safe:
                print("The process is in a safe state.\n")
            else:
                print("System in unsafe state. Aborting...\n")
                break

    def __pretty_data(self):
        print(" " * 9 + "Allocated Resource Table")
        for item in self.__allocated_resources_table:
            print(
                f"P{self.__allocated_resources_table.index(item) + 1}"
                + " ".join(f"{it:>8}" for it in item)
                + "\n"
            )
        print(" " * 9 + "System Resource Table")
        for item in self.__maximum_claim_table:
            print(
                f"P{self.__maximum_claim_table.index(item) + 1}"
                + " ".join(f"{it:>8}" for it in item)
                + "\n"
            )
        print(
            "Current Usage by Active Processes: "
            + " ".join(str(x) for x in self.__claim_vector)
        )
        print(
            "Initial Available Resources:       "
            + " ".join(str(x) for x in self.__available_resources())
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
