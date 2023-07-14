"""
Reports application API URL configration
"""

from django.urls import path

from reports import resources

urlpatterns = [
    path(
        "teams/reports/",
        resources.AnnotatedHappinessReportTeamsListAPIView.as_view(),
        name="reports-teams"
    ),
    path(
        "teams/<team_id>/reports/",
        resources.AnnotatedHappinessReportTeamListAPIView.as_view(),
        name="reports-team"
    )
]
