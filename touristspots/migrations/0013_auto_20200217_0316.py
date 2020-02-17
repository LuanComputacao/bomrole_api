# Generated by Django 3.0.3 on 2020-02-17 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('touristspots', '0012_auto_20200217_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristspotcomments',
            name='tourist_spot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='touristspots.TouristSpot'),
        ),
    ]