# Generated by Django 3.1.4 on 2021-08-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210802_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tower',
            name='conductor_type',
            field=models.CharField(blank=True, choices=[('Partridge', 'Partridge'), ('Ostrich', 'Ostrich'), ('Merlin', 'Merlin'), ('Pelican', 'Pelican'), ('Drake', 'Drake'), ('Pheasant', 'Pheasant')], default='', max_length=200),
        ),
    ]
