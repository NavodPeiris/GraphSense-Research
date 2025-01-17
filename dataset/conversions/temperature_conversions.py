

def celsius_to_fahrenheit(celsius: float, ndigits: int = 2) -> float:
    
    return round((float(celsius) * 9 / 5) + 32, ndigits)


def celsius_to_kelvin(celsius: float, ndigits: int = 2) -> float:
    
    return round(float(celsius) + 273.15, ndigits)


def celsius_to_rankine(celsius: float, ndigits: int = 2) -> float:
    
    return round((float(celsius) * 9 / 5) + 491.67, ndigits)


def fahrenheit_to_celsius(fahrenheit: float, ndigits: int = 2) -> float:
    
    return round((float(fahrenheit) - 32) * 5 / 9, ndigits)


def fahrenheit_to_kelvin(fahrenheit: float, ndigits: int = 2) -> float:
    
    return round(((float(fahrenheit) - 32) * 5 / 9) + 273.15, ndigits)


def fahrenheit_to_rankine(fahrenheit: float, ndigits: int = 2) -> float:
    
    return round(float(fahrenheit) + 459.67, ndigits)


def kelvin_to_celsius(kelvin: float, ndigits: int = 2) -> float:
    
    return round(float(kelvin) - 273.15, ndigits)


def kelvin_to_fahrenheit(kelvin: float, ndigits: int = 2) -> float:
    
    return round(((float(kelvin) - 273.15) * 9 / 5) + 32, ndigits)


def kelvin_to_rankine(kelvin: float, ndigits: int = 2) -> float:
   
    return round((float(kelvin) * 9 / 5), ndigits)


def rankine_to_celsius(rankine: float, ndigits: int = 2) -> float:
    
    return round((float(rankine) - 491.67) * 5 / 9, ndigits)


def rankine_to_fahrenheit(rankine: float, ndigits: int = 2) -> float:
    
    return round(float(rankine) - 459.67, ndigits)


def rankine_to_kelvin(rankine: float, ndigits: int = 2) -> float:
    
    return round((float(rankine) * 5 / 9), ndigits)


def reaumur_to_kelvin(reaumur: float, ndigits: int = 2) -> float:
    
    return round((float(reaumur) * 1.25 + 273.15), ndigits)


def reaumur_to_fahrenheit(reaumur: float, ndigits: int = 2) -> float:
    
    return round((float(reaumur) * 2.25 + 32), ndigits)


def reaumur_to_celsius(reaumur: float, ndigits: int = 2) -> float:
    
    return round((float(reaumur) * 1.25), ndigits)


def reaumur_to_rankine(reaumur: float, ndigits: int = 2) -> float:
    
    return round((float(reaumur) * 2.25 + 32 + 459.67), ndigits)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
