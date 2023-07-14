"""
Reports application API resources
"""

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response

from members.models import TeamModel
from reports import models, serializers, services


class AnnotatedHappinessReportTeamsListAPIView(ListAPIView):
    serializer_class = serializers.AnnotatedHappinessReportSerializer
    queryset = services.get_annotated_teams_reports()


class AnnotatedHappinessReportTeamListAPIView(ListAPIView):
    serializer_class = serializers.AnnotatedHappinessReportSerializer

    def get_queryset(self):
        team = get_object_or_404(TeamModel.objects.all(),
                                 pk=self.kwargs["team_id"])
        return services.get_annotated_teams_reports().filter(team=team)


class HappinessReportListCreateAPIView(ListCreateAPIView):
    queryset = models.HappinessReportModel.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.HappinessReportReadModelSerializer

        return serializers.HappinessReportWriteModelSerializer

    def create(self, request, *args, **kwargs):
        context = {"request": request}
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
