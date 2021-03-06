# Generated by Django 2.0.7 on 2018-07-17 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayacab', '0009_auto_20180715_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='status',
            field=models.CharField(choices=[('AV', 'AVAILABLE'), ('OFF', 'OFFLINE'), ('BK', 'BOOKED')], default='OFF', max_length=10),
        ),
        migrations.AlterField(
            model_name='trip',
            name='fare',
            field=models.IntegerField(null=True),
        ),
    ]
