# Generated by Django 4.1.5 on 2023-02-04 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_calculate_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculatehouse',
            name='calculate',
        ),
        migrations.DeleteModel(
            name='Calculate',
        ),
        migrations.DeleteModel(
            name='Calculatehouse',
        ),
    ]
