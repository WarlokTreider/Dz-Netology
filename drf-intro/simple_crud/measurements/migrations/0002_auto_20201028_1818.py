# Generated by Django 3.1.2 on 2020-10-28 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meas', to='measurements.project'),
        ),
    ]
