
from dataclasses import dataclass


@dataclass
class GasStation:
    gas_quantity: int
    cost: int


def get_gas_stations(
    gas_quantities: list[int], costs: list[int]
) -> tuple[GasStation, ...]:
    return tuple(
        GasStation(quantity, cost) for quantity, cost in zip(gas_quantities, costs)
    )


def can_complete_journey(gas_stations: tuple[GasStation, ...]) -> int:
    total_gas = sum(gas_station.gas_quantity for gas_station in gas_stations)
    total_cost = sum(gas_station.cost for gas_station in gas_stations)
    if total_gas < total_cost:
        return -1

    start = 0
    net = 0
    for i, gas_station in enumerate(gas_stations):
        net += gas_station.gas_quantity - gas_station.cost
        if net < 0:
            start = i + 1
            net = 0
    return start


if __name__ == "__main__":
    import doctest

    doctest.testmod()
