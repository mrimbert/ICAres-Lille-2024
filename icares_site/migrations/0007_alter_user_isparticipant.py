# Generated by Django 5.1 on 2024-10-05 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icares_site', '0006_user_groups_user_has_paid_user_user_permissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isParticipant',
            field=models.IntegerField(default=False),
        ),
    ]
