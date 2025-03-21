

from __future__ import annotations


def simple_interest(
    principal: float, daily_interest_rate: float, days_between_payments: float
) -> float:
    if days_between_payments <= 0:
        raise ValueError("days_between_payments must be > 0")
    if daily_interest_rate < 0:
        raise ValueError("daily_interest_rate must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")
    return principal * daily_interest_rate * days_between_payments


def compound_interest(
    principal: float,
    nominal_annual_interest_rate_percentage: float,
    number_of_compounding_periods: float,
) -> float:
    if number_of_compounding_periods <= 0:
        raise ValueError("number_of_compounding_periods must be > 0")
    if nominal_annual_interest_rate_percentage < 0:
        raise ValueError("nominal_annual_interest_rate_percentage must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")

    return principal * (
        (1 + nominal_annual_interest_rate_percentage) ** number_of_compounding_periods
        - 1
    )


def apr_interest(
    principal: float,
    nominal_annual_percentage_rate: float,
    number_of_years: float,
) -> float:
    if number_of_years <= 0:
        raise ValueError("number_of_years must be > 0")
    if nominal_annual_percentage_rate < 0:
        raise ValueError("nominal_annual_percentage_rate must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")

    return compound_interest(
        principal, nominal_annual_percentage_rate / 365, number_of_years * 365
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
