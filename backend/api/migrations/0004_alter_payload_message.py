# Generated by Django 3.2.5 on 2021-08-23 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_report_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payload',
            name='message',
            field=models.CharField(max_length=100, null=True),
        ),
    ]