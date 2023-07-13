"""
Reports application services
"""

import datetime

from django.utils import timezone


def get_today() -> datetime.date:
    """Return current date"""

    return timezone.now().date()


def get_date_by_days_delta(days: int) -> datetime.date:
    return get_today() - timezone.timedelta(days=days)
