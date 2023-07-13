"""
Members application admin site
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from members import models


@admin.register(models.MemberModel)
class MemberModelAdmin(UserAdmin):
    """Member model admin site"""

    list_display = (
        "username",
        "email",
        "get_full_name",
        "get_team",
        "is_staff"
    )
    list_filter = "team", "is_superuser"
    ordering = "first_name", "last_name"
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name", "email")}),
        (_("Membership"), {"fields": ("team",)})
    )

    # display is modified to provide a custom empty value
    @admin.display(description="full name")
    def get_full_name(self, obj: models.MemberModel) -> str:
        """Return a member's full name"""

        return obj.get_full_name()

    @admin.display(description="team", empty_value="none")
    def get_team(self, obj: models.MemberModel) -> models.TeamModel:
        """Return a related team model instance"""

        return obj.team


@admin.register(models.TeamModel)
class TeamModelAdmin(admin.ModelAdmin):
    """Team model admin site"""

    list_display = "name", "get_members_count"

    @admin.display(description="members")
    def get_members_count(self, obj: models.TeamModel) -> int:
        """Return a team members count number"""

        return obj.members.count()
