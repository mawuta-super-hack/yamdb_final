# Generated by Django 2.2.16 on 2022-08-11 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_merge_20220811_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(max_length=50, null=True, verbose_name='Код подтверждения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
