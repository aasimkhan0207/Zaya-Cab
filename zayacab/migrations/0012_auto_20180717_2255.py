# Generated by Django 2.0.7 on 2018-07-17 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayacab', '0011_auto_20180717_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='status',
            field=models.CharField(choices=[('AV', 'AVAILABLE'), ('OFF', 'OFFLINE'), ('BK', 'BOOKED')], default='AV', max_length=10),
        ),
    ]
