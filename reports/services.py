"""
Reports application services
"""

import datetime

from django.utils import timezone


def get_today() -> datetime.date:
    """Return current date"""

    return timezone.now().date()


def get_date_before(days: int) -> datetime.date:
    """Return date the specified number of days before today"""

    return get_today() - timezone.timedelta(days=days)
