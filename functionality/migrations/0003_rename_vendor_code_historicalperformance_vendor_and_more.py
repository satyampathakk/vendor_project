# Generated by Django 4.2.11 on 2024-05-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functionality', '0002_rename_vendor_historicalperformance_vendor_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalperformance',
            old_name='vendor_code',
            new_name='vendor',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='vendor_code',
            new_name='vendor',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='average_response_time',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='fulfillment_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.FloatField(default=0),
        ),
    ]