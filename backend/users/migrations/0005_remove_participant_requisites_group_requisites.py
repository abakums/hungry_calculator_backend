# Generated by Django 4.1.1 on 2023-11-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_participant_requisites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='requisites',
        ),
        migrations.AddField(
            model_name='group',
            name='requisites',
            field=models.CharField(default='', max_length=100, verbose_name='Реквизиты'),
            preserve_default=False,
        ),
    ]
