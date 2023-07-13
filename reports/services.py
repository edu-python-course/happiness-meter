"""
Reports application services
"""

from django.db.models import Avg, F, QuerySet
from django.db.models.functions import Round

from members.models import TeamModel
from reports.models import HappinessReportModel


def get_annotated_teams_reports() -> QuerySet:
    """Return an annotated query set with average happiness level"""

    return \
        HappinessReportModel.objects.filter(
            reporter__team__isnull=False
        ).order_by(
            "-reported_on",
            F("reporter__team__name")
        ).annotate(
            date=F("reported_on"),
            team=F("reporter__team__name")
        ).values(
            "date",
            "team"
        ).annotate(
            level=Round(Avg("level"))
        )


def get_annotated_team_reports(team: TeamModel) -> QuerySet:
    """Return an annotated query set for a specific team"""

    return get_annotated_teams_reports().filter(team=team)
