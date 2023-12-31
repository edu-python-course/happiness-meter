"""
Reports application services
"""

from django.db.models import Avg, F, QuerySet, Window
from django.db.models.functions import Lag, Round

from reports.models import HappinessReportModel


def get_annotated_teams_reports() -> QuerySet:
    """Return an annotated query set with average happiness level"""

    return \
        HappinessReportModel.objects.filter(
            reporter__team__isnull=False
        ).order_by(
            "-reported_on",
            F("reporter__team__name"),
        ).annotate(
            date=F("reported_on"),
            team=F("reporter__team__name")
        ).values(
            "date",
            "team"
        ).annotate(
            level=Round(Avg("level")),
        ).annotate(
            team_id=F("reporter__team_id"),
            prev=Window(
                expression=Lag("level"),
                partition_by="reporter__team",
                order_by="reported_on"
            )
        )
