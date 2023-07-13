"""
Members application models
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class TeamModel(models.Model):
    """Team model"""

    class Meta:
        db_table = "team"
        verbose_name = "team"
        verbose_name_plural = "teams"

    name = models.CharField(max_length=64, unique=True, db_index=True)

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.name


class MemberModel(AbstractUser):
    """Happiness application user model"""

    class Meta:
        db_table = "member"
        verbose_name = "member"
        verbose_name_plural = "members"
        default_related_name = "members"
        ordering = "first_name", "last_name"

    team = models.ForeignKey(TeamModel, on_delete=models.SET_NULL,
                             null=True, blank=True,
                             related_name="members")

    def __str__(self) -> str:
        """Return a string representation of an instance"""

        return self.get_full_name() or self.username
