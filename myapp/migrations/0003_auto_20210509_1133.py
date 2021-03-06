# Generated by Django 3.1.6 on 2021-05-09 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210509_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='None', max_length=100)),
                ('Number_Of_People', models.IntegerField(null=True)),
                ('date', models.DateField()),
                ('Day_or_Night', models.CharField(choices=[('Day', 'Day'), ('NIght', 'Night')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='check',
            name='Day_or_Night',
            field=models.CharField(choices=[('Day', 'Day'), ('NIght', 'Night')], max_length=100),
        ),
    ]
