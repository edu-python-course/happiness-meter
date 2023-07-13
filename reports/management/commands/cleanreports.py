"""
Clean happiness reports
"""

from django.core.management.base import BaseCommand

from reports.models import HappinessReportModel


class Command(BaseCommand):
    help = "Remove all happiness reports from the database"

    def handle(self, *args, **options):
        deleted, _ = HappinessReportModel.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("%d reports deleted" % deleted))
