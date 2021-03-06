# Generated by Django 4.0.3 on 2022-03-28 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_bloodgroup_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doner',
            name='blood_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.bloodgroup'),
        ),
        migrations.AlterField(
            model_name='doner',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.gender'),
        ),
    ]
