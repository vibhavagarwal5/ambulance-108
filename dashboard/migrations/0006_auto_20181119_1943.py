# Generated by Django 2.1.3 on 2018-11-19 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20181119_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='ambulance_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trips', to='dashboard.Ambulance'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='hospital_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trips', to='dashboard.Hospital'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='patient_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trips', to='dashboard.Patient'),
        ),
    ]