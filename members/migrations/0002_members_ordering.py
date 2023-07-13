from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="membermodel",
            options={
                "default_related_name": "members",
                "ordering": ("first_name", "last_name"),
                "verbose_name": "member",
                "verbose_name_plural": "members"
            },
        ),
    ]
