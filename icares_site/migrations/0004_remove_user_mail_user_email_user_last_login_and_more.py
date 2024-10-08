# Generated by Django 5.1 on 2024-09-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icares_site', '0003_remove_user_epreuve_user_epreuve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mail',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='test', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='user',
            name='isParticipant',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
