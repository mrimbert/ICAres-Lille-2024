# Generated by Django 5.1 on 2024-10-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icares_site', '0008_lien_alter_user_formule_alter_user_isparticipant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lien',
            name='lille',
            field=models.CharField(default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='lien',
            name='lyon',
            field=models.CharField(default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='lien',
            name='marseille',
            field=models.CharField(default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='lien',
            name='nantes',
            field=models.CharField(default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='lien',
            name='paris',
            field=models.CharField(default='None', max_length=300),
        ),
    ]