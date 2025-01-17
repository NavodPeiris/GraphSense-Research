
UNIVERSAL_GAS_CONSTANT = 8.314462  


def pressure_of_gas_system(moles: float, kelvin: float, volume: float) -> float:
    if moles < 0 or kelvin < 0 or volume < 0:
        raise ValueError("Invalid inputs. Enter positive value.")
    return moles * kelvin * UNIVERSAL_GAS_CONSTANT / volume


def volume_of_gas_system(moles: float, kelvin: float, pressure: float) -> float:
    if moles < 0 or kelvin < 0 or pressure < 0:
        raise ValueError("Invalid inputs. Enter positive value.")
    return moles * kelvin * UNIVERSAL_GAS_CONSTANT / pressure


def temperature_of_gas_system(moles: float, volume: float, pressure: float) -> float:
    if moles < 0 or volume < 0 or pressure < 0:
        raise ValueError("Invalid inputs. Enter positive value.")

    return pressure * volume / (moles * UNIVERSAL_GAS_CONSTANT)


def moles_of_gas_system(kelvin: float, volume: float, pressure: float) -> float:
    if kelvin < 0 or volume < 0 or pressure < 0:
        raise ValueError("Invalid inputs. Enter positive value.")

    return pressure * volume / (kelvin * UNIVERSAL_GAS_CONSTANT)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
