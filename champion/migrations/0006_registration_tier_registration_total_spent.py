# Generated by Django 5.0.7 on 2024-09-07 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("champion", "0005_champ_testimonial"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="tier",
            field=models.CharField(
                choices=[
                    ("Bronze", "Bronze"),
                    ("Silver", "Silver"),
                    ("Gold", "Gold"),
                    ("Platinum", "Platinum"),
                    ("Titanium", "Titanium"),
                    ("Emerald", "Emerald"),
                ],
                default="Bronze",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="registration",
            name="total_spent",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
