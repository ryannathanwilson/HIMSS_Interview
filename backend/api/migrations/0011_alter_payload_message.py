# Generated by Django 3.2.5 on 2021-08-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_payload_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payload',
            name='message',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
