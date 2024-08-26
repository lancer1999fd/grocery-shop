# Generated by Django 5.0.4 on 2024-08-25 17:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personal", "0003_shoppinglist_shoppinglistitem"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Note",
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
                ("title", models.CharField(max_length=10, verbose_name="Titel")),
                ("content", models.TextField(max_length=200, verbose_name="Inhalte")),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("gray", "Grau"),
                            ("red", "Rot"),
                            ("orange", "Orange"),
                            ("green", "Grün"),
                            ("cyan", "Türkis"),
                            ("blue", "Blau"),
                            ("purple", "Violett"),
                        ],
                        default="gray",
                        max_length=10,
                        verbose_name="Farben",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Benutzer",
                    ),
                ),
            ],
        ),
    ]
