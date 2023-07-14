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
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = MemberModel
        fields = (
            "pk", "username", "first_name", "last_name", "email",
            "team", "password", "confirm_password"
        )

    def validate(self, data):
        """Validate serialized data"""

        if data.get("password") != data.get("confirm_password"):
            error_message = "Password does not match"
            errors = {
                "password": error_message,
                "confirm_password": error_message
            }
            raise serializers.ValidationError(errors)

        return super().validate(data)

    def create(self, validated_data) -> MemberModel:
        """Create a member instance"""

        del validated_data["confirm_password"]

        return MemberModel.objects.create_user(**validated_data)

    def update(self, instance, validated_data) -> MemberModel:
        """Update a member instance"""

        instance = super().update(instance, validated_data)

        if "password" in validated_data:
            instance.set_password(validated_data["password"])

        return instance


class TeamModelSerializer(serializers.ModelSerializer):
    """Team model serializer"""

    members = MemberModelSerializer(many=True, read_only=True)

    class Meta:
        model = TeamModel
        fields = "__all__"
