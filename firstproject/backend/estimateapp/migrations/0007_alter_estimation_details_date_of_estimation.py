# Generated by Django 4.1.3 on 2022-12-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimateapp', '0006_estimate_services_estimate_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimation_details',
            name='date_of_estimation',
            field=models.DateField(verbose_name='%d-%m-%Y'),
        ),
    ]
