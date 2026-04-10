from datetime import datetime, timedelta
from dataclasses import dataclass


@dataclass
class TimeLeft:
    years: int
    days: int
    hours: int
    minutes: int
    seconds: int
    total_days: int
    expired: bool


def calculate_countdown(birth_year: int, birth_month: int, life_expectancy: float) -> TimeLeft:
    birth_date = datetime(birth_year, birth_month, 1)
    end_date = birth_date + timedelta(days=life_expectancy * 365.25)
    now = datetime.now()

    remaining = end_date - now
    expired = remaining.total_seconds() <= 0

    if expired:
        return TimeLeft(0, 0, 0, 0, 0, 0, True)

    total_seconds = int(remaining.total_seconds())

    years = total_seconds // (365 * 24 * 3600)
    total_seconds %= (365 * 24 * 3600)

    days = total_seconds // (24 * 3600)
    total_seconds %= (24 * 3600)

    hours = total_seconds // 3600
    total_seconds %= 3600

    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return TimeLeft(
        years=years,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        total_days=remaining.days,
        expired=False
    )
