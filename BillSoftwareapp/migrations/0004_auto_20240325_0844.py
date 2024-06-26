# Generated by Django 3.2.24 on 2024-03-25 08:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BillSoftwareapp', '0003_alter_history_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='openingbalance',
        ),
        migrations.AddField(
            model_name='party',
            name='opening_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 25)),
        ),
        migrations.AlterField(
            model_name='purchasedebit',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BillSoftwareapp.parties'),
        ),
    ]
