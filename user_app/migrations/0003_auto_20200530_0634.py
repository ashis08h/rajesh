# Generated by Django 2.0.5 on 2020-05-30 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_auto_20200530_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='user_app.UserDetails'),
        ),
    ]