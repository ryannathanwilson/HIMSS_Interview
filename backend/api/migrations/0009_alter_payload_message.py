# Generated by Django 3.2.5 on 2021-08-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210826_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payload',
            name='message',
            field=models.CharField(default='null', max_length=100, null=True),
        ),
    ]
