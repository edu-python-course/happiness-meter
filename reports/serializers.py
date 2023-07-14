"""
Reports application serializers
"""

from django.utils import timezone
from rest_framework import serializers

from reports.models import HappinessReportModel


class HappinessReportWriteModelSerializer(serializers.ModelSerializer):
    """Happiness report model serializer"""

    class Meta:
        model = HappinessReportModel
        fields = "pk", "level", "reported_on"

    def save(self, **kwargs):
        reporter = self.context["request"].user
        self.validated_data["reporter"] = reporter

        try:
            instance = HappinessReportModel.objects.get(
                reported_on=timezone.now().date(),
                reporter=reporter
            )
            self.update(instance, self.validated_data)
        except HappinessReportModel.DoesNotExist:
            self.create(self.validated_data)


class HappinessReportReadModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HappinessReportModel
        fields = "__all__"


class AnnotatedHappinessReportSerializer(serializers.Serializer):
    """Annotated happiness reports serializer"""

    date = serializers.DateField()
    team_id = serializers.IntegerField()
    team = serializers.CharField()
    avg = serializers.FloatField(source="level")
    avg_prev = serializers.FloatField(source="prev")

    def create(self, validated_data):
        raise NotImplementedError("Operation is restricted")

    def update(self, instance, validated_data):
        raise NotImplementedError("Operation is restricted")
