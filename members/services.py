"""
Members application services
"""

from django.db.models.query import QuerySet

from members.models import MemberModel


def get_available_reporters() -> QuerySet:
    """Return a query set of non superusers who can create reports"""

    return MemberModel.objects.filter(is_superuser=False)
