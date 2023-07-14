"""
Members application API resources
"""

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from members import models, serializers


class MemberListCreateAPIView(ListCreateAPIView):
    serializer_class = serializers.MemberModelSerializer
    queryset = models.MemberModel.objects.all()


class MemberRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MemberModelSerializer
    queryset = models.MemberModel.objects.all()


class TeamListCrateAPIView(ListCreateAPIView):
    serializer_class = serializers.TeamModelSerializer
    queryset = models.TeamModel.objects.all()


class TeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TeamModelSerializer
    queryset = models.TeamModel.objects.all()
