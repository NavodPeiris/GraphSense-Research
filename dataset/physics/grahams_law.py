
from math import pow, sqrt  


def validate(*values: float) -> bool:
    result = len(values) > 0 and all(value > 0.0 for value in values)
    return result


def effusion_ratio(molar_mass_1: float, molar_mass_2: float) -> float | ValueError:
    return (
        round(sqrt(molar_mass_2 / molar_mass_1), 6)
        if validate(molar_mass_1, molar_mass_2)
        else ValueError("Input Error: Molar mass values must greater than 0.")
    )


def first_effusion_rate(
    effusion_rate: float, molar_mass_1: float, molar_mass_2: float
) -> float | ValueError:
    return (
        round(effusion_rate * sqrt(molar_mass_2 / molar_mass_1), 6)
        if validate(effusion_rate, molar_mass_1, molar_mass_2)
        else ValueError(
            "Input Error: Molar mass and effusion rate values must greater than 0."
        )
    )


def second_effusion_rate(
    effusion_rate: float, molar_mass_1: float, molar_mass_2: float
) -> float | ValueError:
    return (
        round(effusion_rate / sqrt(molar_mass_2 / molar_mass_1), 6)
        if validate(effusion_rate, molar_mass_1, molar_mass_2)
        else ValueError(
            "Input Error: Molar mass and effusion rate values must greater than 0."
        )
    )


def first_molar_mass(
    molar_mass: float, effusion_rate_1: float, effusion_rate_2: float
) -> float | ValueError:
    return (
        round(molar_mass / pow(effusion_rate_1 / effusion_rate_2, 2), 6)
        if validate(molar_mass, effusion_rate_1, effusion_rate_2)
        else ValueError(
            "Input Error: Molar mass and effusion rate values must greater than 0."
        )
    )


def second_molar_mass(
    molar_mass: float, effusion_rate_1: float, effusion_rate_2: float
) -> float | ValueError:
    return (
        round(pow(effusion_rate_1 / effusion_rate_2, 2) / molar_mass, 6)
        if validate(molar_mass, effusion_rate_1, effusion_rate_2)
        else ValueError(
            "Input Error: Molar mass and effusion rate values must greater than 0."
        )
    )
