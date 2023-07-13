"""
Reports application admin site
"""

from django.contrib import admin

from members.models import TeamModel
from reports.models import HappinessReportModel


@admin.register(HappinessReportModel)
class HappinessReportModelAdmin(admin.ModelAdmin):
    """Happiness report model admin site"""

    list_display = "reporter", "level", "reported_on", "get_team"
    list_filter = "reported_on", "reporter__team"
    ordering = "-reported_on", "reporter__team"

    # happiness reports can not be added, changed or deleted from admin site
    actions = None

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @admin.display(description="team", empty_value="none")
    def get_team(self, obj: HappinessReportModel) -> TeamModel:
        """Return a team instance"""

        return obj.reporter.team
