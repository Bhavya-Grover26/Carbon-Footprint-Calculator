# Generated by Django 4.1.5 on 2023-02-04 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_rename_calculatehouse_individual'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='flightsless',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='individual',
            name='flightsmore',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField(null=True)),
                ('electricity', models.FloatField(null=True)),
                ('flightsless', models.FloatField(null=True)),
                ('flightsmore', models.FloatField(null=True)),
                ('newspaper', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Dont use', 'Dont use')], max_length=200, null=True)),
                ('ghg', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Dont use', 'Dont use')], max_length=200, null=True)),
                ('calculate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.calculate')),
            ],
        ),
    ]