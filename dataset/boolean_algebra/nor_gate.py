
from collections.abc import Callable


def nor_gate(input_1: int, input_2: int) -> int:
    
    return int(input_1 == input_2 == 0)


def truth_table(func: Callable) -> str:
    

    def make_table_row(items: list | tuple) -> str:
        
        return f"| {' | '.join(f'{item:^8}' for item in items)} |"

    return "\n".join(
        (
            "Truth Table of NOR Gate:",
            make_table_row(("Input 1", "Input 2", "Output")),
            *[make_table_row((i, j, func(i, j))) for i in (0, 1) for j in (0, 1)],
        )
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(truth_table(nor_gate))
