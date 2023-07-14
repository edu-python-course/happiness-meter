"""
Members application serializers
"""

from rest_framework import serializers

from members.models import MemberModel, TeamModel


class MemberModelSerializer(serializers.ModelSerializer):
    """Member model serializer"""

    team = serializers.PrimaryKeyRelatedField(
        queryset=TeamModel.objects.all(),
        allow_null=True,
        required=False,
        write_only=True
    )

    class Meta:
        model = MemberModel
        fields = (
            "pk", "username", "first_name", "last_name",
            "team"
        )


class TeamModelSerializer(serializers.ModelSerializer):
    """Team model serializer"""

    members = MemberModelSerializer(many=True, read_only=True)

    class Meta:
        model = TeamModel
        fields = "__all__"
