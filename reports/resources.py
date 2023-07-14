"""
Reports application API resources
"""

from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView
)

from members.models import TeamModel
from reports import serializers, services


class AnnotatedHappinessReportTeamsListAPIView(ListAPIView):
    serializer_class = serializers.AnnotatedHappinessReportSerializer
    queryset = services.get_annotated_teams_reports()


class AnnotatedHappinessReportTeamListAPIView(ListAPIView):
    serializer_class = serializers.AnnotatedHappinessReportSerializer

    def get_queryset(self):
        team = get_object_or_404(TeamModel.objects.all(),
                                 pk=self.kwargs["team_id"])
        return services.get_annotated_team_reports(team)
