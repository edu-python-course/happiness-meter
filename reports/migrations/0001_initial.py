import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import reports.utils


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="HappinessReportModel",
            fields=[
                ("id",
                 models.BigAutoField(auto_created=True, primary_key=True,
                                     serialize=False, verbose_name="ID")),
                ("reported_on",
                 models.DateField(default=reports.utils.get_today,
                                  editable=False)),
                ("level", models.IntegerField(
                    choices=[(1, "Joy"), (2, "Excitement"), (3, "Gratitude"),
                             (4, "Pride"), (5, "Optimism"), (6, "Contentment"),
                             (7, "Satisfaction"), (8, "Love"), (9, "Serenity"),
                             (10, "Bliss")],
                    validators=[django.core.validators.MinValueValidator(1),
                                django.core.validators.MaxValueValidator(10)],
                    verbose_name="happiness level")),
                ("reporter",
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "happiness report",
                "verbose_name_plural": "happiness reports",
                "db_table": "happiness",
                "ordering": ("-reported_on", "reporter__team"),
                "default_related_name": "happiness_reports",
                "unique_together": {("reporter", "reported_on")},
            },
        ),
    ]
