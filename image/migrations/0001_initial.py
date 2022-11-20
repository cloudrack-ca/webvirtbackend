# Generated by Django 4.1.3 on 2022-11-20 09:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
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
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("custom", "Custom"),
                            ("backup", "Backup"),
                            ("snapshot", "Snapshot"),
                            ("application", "Application"),
                            ("distribution", "Distribution"),
                        ],
                        default="snapshot",
                        max_length=50,
                    ),
                ),
                (
                    "distribution",
                    models.CharField(
                        choices=[
                            ("custom", "Custom"),
                            ("backup", "Backup"),
                            ("snapshot", "Snapshot"),
                            ("application", "Application"),
                            ("distribution", "Distribution"),
                        ],
                        default="Unknown",
                        max_length=50,
                    ),
                ),
                ("md5sum", models.CharField(max_length=50)),
                ("file_size", models.BigIntegerField()),
                ("disk_size", models.BigIntegerField()),
                ("file_name", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(default=False)),
                ("is_deleted", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now_add=True)),
                ("deleted", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Image",
                "verbose_name_plural": "Images",
                "ordering": ["-id"],
            },
        ),
    ]
