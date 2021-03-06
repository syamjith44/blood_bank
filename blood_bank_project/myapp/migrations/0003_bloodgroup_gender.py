# Generated by Django 4.0.3 on 2022-03-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_doner_center_alter_doner_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'BloodGroups',
                'verbose_name_plural': 'BloodGroups',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
                'ordering': ('name',),
            },
        ),
    ]
