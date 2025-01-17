
import math
from datetime import UTC, datetime, timedelta


def gauss_easter(year: int) -> datetime:
    metonic_cycle = year % 19
    julian_leap_year = year % 4
    non_leap_year = year % 7
    leap_day_inhibits = math.floor(year / 100)
    lunar_orbit_correction = math.floor((13 + 8 * leap_day_inhibits) / 25)
    leap_day_reinstall_number = leap_day_inhibits / 4
    secular_moon_shift = (
        15 - lunar_orbit_correction + leap_day_inhibits - leap_day_reinstall_number
    ) % 30
    century_starting_point = (4 + leap_day_inhibits - leap_day_reinstall_number) % 7

    
    days_to_add = (19 * metonic_cycle + secular_moon_shift) % 30

    
    days_from_phm_to_sunday = (
        2 * julian_leap_year
        + 4 * non_leap_year
        + 6 * days_to_add
        + century_starting_point
    ) % 7

    if days_to_add == 29 and days_from_phm_to_sunday == 6:
        return datetime(year, 4, 19, tzinfo=UTC)
    elif days_to_add == 28 and days_from_phm_to_sunday == 6:
        return datetime(year, 4, 18, tzinfo=UTC)
    else:
        return datetime(year, 3, 22, tzinfo=UTC) + timedelta(
            days=int(days_to_add + days_from_phm_to_sunday)
        )


if __name__ == "__main__":
    for year in (1994, 2000, 2010, 2021, 2023, 2032, 2100):
        tense = "will be" if year > datetime.now(tz=UTC).year else "was"
        print(f"Easter in {year} {tense} {gauss_easter(year)}")
