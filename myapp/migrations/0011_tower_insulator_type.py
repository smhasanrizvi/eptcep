# Generated by Django 3.1.4 on 2021-08-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_tower_line_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tower',
            name='insulator_type',
            field=models.CharField(blank=True, choices=[('Pin type', 'Pin type'), ('Suspension type', 'Suspension type'), ('Strain type', 'Strain type')], default='', max_length=200),
        ),
    ]