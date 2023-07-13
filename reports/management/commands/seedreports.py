"""
Seed random happiness reports
"""

import random

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from members.services import get_available_reporters
from reports.models import HappinessReportModel
from reports.services import get_date_by_days_delta as get_date


class Command(BaseCommand):
    """Seed reports command implementation"""

    help = "Seed random happiness reports"

    def add_arguments(self, parser):
        parser.add_argument(
            "days", default=30, type=int, nargs="?",
            help="Number of days to create reports. Defaults to 30."
        )

    def handle(self, *args, **options):
        iteration = options["days"] - 1
        reporters = get_available_reporters()
        reports = []

        while iteration >= 0:

            for reporter in reporters:
                level, _ = random.choice(HappinessReportModel.HAPPINESS_LEVELS)
                reported_on = get_date(iteration)
                reports.append(HappinessReportModel(
                    reporter=reporter, level=level, reported_on=reported_on
                ))

            iteration -= 1

        try:
            seeds = HappinessReportModel.objects.bulk_create(reports)
            created = len(seeds)
            self.stdout.write(self.style.SUCCESS("create %d reports" % created))
        except IntegrityError as err:
            self.stderr.write(self.style.ERROR(f"{err}"))
            return
