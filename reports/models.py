"""
Reports application models
"""

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from reports.services import get_today


class HappinessReportModel(models.Model):
    class Meta:
        db_table = "happiness"
        verbose_name = "happiness report"
        verbose_name_plural = "happiness reports"
        default_related_name = "happiness_reports"
        ordering = "-reported_on", "reporter__team"
        unique_together = "reporter", "reported_on"

    # happiness levels
    JOY = 1
    EXCITEMENT = 2
    GRATITUDE = 3
    PRIDE = 4
    OPTIMISM = 5
    CONTENTMENT = 6
    SATISFACTION = 7
    LOVE = 8
    SERENITY = 9
    BLISS = 10
    HAPPINESS_LEVELS = (
        (JOY, "Joy"),
        (EXCITEMENT, "Excitement"),
        (GRATITUDE, "Gratitude"),
        (PRIDE, "Pride"),
        (OPTIMISM, "Optimism"),
        (CONTENTMENT, "Contentment"),
        (SATISFACTION, "Satisfaction"),
        (LOVE, "Love"),
        (SERENITY, "Serenity"),
        (BLISS, "Bliss"),
    )

    reporter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reported_on = models.DateField(default=get_today, editable=False)
    level = models.IntegerField(
        validators=[MinValueValidator(JOY), MaxValueValidator(BLISS)],
        choices=HAPPINESS_LEVELS,
        verbose_name="happiness level"
    )

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return f"{self.reporter} reported {self.level} on {self.reported_on}"
