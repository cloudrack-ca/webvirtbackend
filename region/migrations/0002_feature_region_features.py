# Generated by Django 4.2.3 on 2023-09-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("region", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feature",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("ipv6", "IPv6"),
                            ("resize", "Resize"),
                            ("volume", "Volume"),
                            ("backup", "Backup"),
                            ("snapshot", "Snapshot"),
                            ("one_click", "One-Click"),
                        ],
                        max_length=100,
                        unique=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Feature",
                "verbose_name_plural": "Features",
                "ordering": ["-id"],
            },
        ),
        migrations.AddField(
            model_name="region",
            name="features",
            field=models.ManyToManyField(related_name="features", to="region.feature"),
        ),
    ]
