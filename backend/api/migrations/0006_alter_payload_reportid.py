# Generated by Django 3.2.5 on 2021-08-26 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_report_resolved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payload',
            name='reportId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reference'),
        ),
    ]