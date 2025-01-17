
valid_colors: list = [
    "Black",
    "Brown",
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Violet",
    "Grey",
    "White",
    "Gold",
    "Silver",
]

significant_figures_color_values: dict[str, int] = {
    "Black": 0,
    "Brown": 1,
    "Red": 2,
    "Orange": 3,
    "Yellow": 4,
    "Green": 5,
    "Blue": 6,
    "Violet": 7,
    "Grey": 8,
    "White": 9,
}

multiplier_color_values: dict[str, float] = {
    "Black": 10**0,
    "Brown": 10**1,
    "Red": 10**2,
    "Orange": 10**3,
    "Yellow": 10**4,
    "Green": 10**5,
    "Blue": 10**6,
    "Violet": 10**7,
    "Grey": 10**8,
    "White": 10**9,
    "Gold": 10**-1,
    "Silver": 10**-2,
}

tolerance_color_values: dict[str, float] = {
    "Brown": 1,
    "Red": 2,
    "Orange": 0.05,
    "Yellow": 0.02,
    "Green": 0.5,
    "Blue": 0.25,
    "Violet": 0.1,
    "Grey": 0.01,
    "Gold": 5,
    "Silver": 10,
}

temperature_coeffecient_color_values: dict[str, int] = {
    "Black": 250,
    "Brown": 100,
    "Red": 50,
    "Orange": 15,
    "Yellow": 25,
    "Green": 20,
    "Blue": 10,
    "Violet": 5,
    "Grey": 1,
}

band_types: dict[int, dict[str, int]] = {
    3: {"significant": 2, "multiplier": 1},
    4: {"significant": 2, "multiplier": 1, "tolerance": 1},
    5: {"significant": 3, "multiplier": 1, "tolerance": 1},
    6: {"significant": 3, "multiplier": 1, "tolerance": 1, "temp_coeffecient": 1},
}


def get_significant_digits(colors: list) -> str:
    digit = ""
    for color in colors:
        if color not in significant_figures_color_values:
            msg = f"{color} is not a valid color for significant figure bands"
            raise ValueError(msg)
        digit = digit + str(significant_figures_color_values[color])
    return str(digit)


def get_multiplier(color: str) -> float:
    if color not in multiplier_color_values:
        msg = f"{color} is not a valid color for multiplier band"
        raise ValueError(msg)
    return multiplier_color_values[color]


def get_tolerance(color: str) -> float:
    if color not in tolerance_color_values:
        msg = f"{color} is not a valid color for tolerance band"
        raise ValueError(msg)
    return tolerance_color_values[color]


def get_temperature_coeffecient(color: str) -> int:
    if color not in temperature_coeffecient_color_values:
        msg = f"{color} is not a valid color for temperature coeffecient band"
        raise ValueError(msg)
    return temperature_coeffecient_color_values[color]


def get_band_type_count(total_number_of_bands: int, type_of_band: str) -> int:
    if total_number_of_bands not in band_types:
        msg = f"{total_number_of_bands} is not a valid number of bands"
        raise ValueError(msg)
    if type_of_band not in band_types[total_number_of_bands]:
        msg = f"{type_of_band} is not valid for a {total_number_of_bands} band resistor"
        raise ValueError(msg)
    return band_types[total_number_of_bands][type_of_band]


def check_validity(number_of_bands: int, colors: list) -> bool:
    if number_of_bands >= 3 and number_of_bands <= 6:
        if number_of_bands == len(colors):
            for color in colors:
                if color not in valid_colors:
                    msg = f"{color} is not a valid color"
                    raise ValueError(msg)
            return True
        else:
            msg = f"Expecting {number_of_bands} colors, provided {len(colors)} colors"
            raise ValueError(msg)
    else:
        msg = "Invalid number of bands. Resistor bands must be 3 to 6"
        raise ValueError(msg)


def calculate_resistance(number_of_bands: int, color_code_list: list) -> dict:
    is_valid = check_validity(number_of_bands, color_code_list)
    if is_valid:
        number_of_significant_bands = get_band_type_count(
            number_of_bands, "significant"
        )
        significant_colors = color_code_list[:number_of_significant_bands]
        significant_digits = int(get_significant_digits(significant_colors))
        multiplier_color = color_code_list[number_of_significant_bands]
        multiplier = get_multiplier(multiplier_color)
        if number_of_bands == 3:
            tolerance_color = None
        else:
            tolerance_color = color_code_list[number_of_significant_bands + 1]
        tolerance = (
            20 if tolerance_color is None else get_tolerance(str(tolerance_color))
        )
        if number_of_bands != 6:
            temperature_coeffecient_color = None
        else:
            temperature_coeffecient_color = color_code_list[
                number_of_significant_bands + 2
            ]
        temperature_coeffecient = (
            0
            if temperature_coeffecient_color is None
            else get_temperature_coeffecient(str(temperature_coeffecient_color))
        )
        resisitance = significant_digits * multiplier
        if temperature_coeffecient == 0:
            answer = f"{resisitance}Ω ±{tolerance}% "
        else:
            answer = f"{resisitance}Ω ±{tolerance}% {temperature_coeffecient} ppm/K"
        return {"resistance": answer}
    else:
        raise ValueError("Input is invalid")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
