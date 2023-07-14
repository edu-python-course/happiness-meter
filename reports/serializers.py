"""
Reports application serializers
"""

from rest_framework import serializers

from reports.models import HappinessReportModel


class HappinessReportModelSerializer(serializers.ModelSerializer):
    """Happiness report model serializer"""

    class Meta:
        model = HappinessReportModel
        fields = "level", "reporter"
