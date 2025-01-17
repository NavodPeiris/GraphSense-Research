import argparse
import datetime


def zeller(date_input: str) -> str:
    days = {
        "0": "Sunday",
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday",
    }

    convert_datetime_days = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 0}

    
    if not 0 < len(date_input) < 11:
        raise ValueError("Must be 10 characters long")

    
    m: int = int(date_input[0] + date_input[1])
    
    if not 0 < m < 13:
        raise ValueError("Month must be between 1 - 12")

    sep_1: str = date_input[2]
    
    if sep_1 not in ["-", "/"]:
        raise ValueError("Date separator must be '-' or '/'")

    
    d: int = int(date_input[3] + date_input[4])
    
    if not 0 < d < 32:
        raise ValueError("Date must be between 1 - 31")

    
    sep_2: str = date_input[5]
    
    if sep_2 not in ["-", "/"]:
        raise ValueError("Date separator must be '-' or '/'")

    
    y: int = int(date_input[6] + date_input[7] + date_input[8] + date_input[9])
    
    if not 45 < y < 8500:
        raise ValueError(
            "Year out of range. There has to be some sort of limit...right?"
        )

    
    dt_ck = datetime.date(int(y), int(m), int(d))

    
    if m <= 2:
        y = y - 1
        m = m + 12
    
    c: int = int(str(y)[:2])
    k: int = int(str(y)[2:])
    t: int = int(2.6 * m - 5.39)
    u: int = int(c / 4)
    v: int = int(k / 4)
    x: int = int(d + k)
    z: int = int(t + u + v + x)
    w: int = int(z - (2 * c))
    f: int = round(w % 7)
    

    
    if f != convert_datetime_days[dt_ck.weekday()]:
        raise AssertionError("The date was evaluated incorrectly. Contact developer.")

    
    response: str = f"Your date {date_input}, is a {days[str(f)]}!"
    return response


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    parser = argparse.ArgumentParser(
        description=(
            "Find out what day of the week nearly any date is or was. Enter "
            "date as a string in the mm-dd-yyyy or mm/dd/yyyy format"
        )
    )
    parser.add_argument(
        "date_input", type=str, help="Date as a string (mm-dd-yyyy or mm/dd/yyyy)"
    )
    args = parser.parse_args()
    zeller(args.date_input)
