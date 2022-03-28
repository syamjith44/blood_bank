# Generated by Django 4.0.3 on 2022-03-27 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('wiki', models.URLField()),
            ],
            options={
                'verbose_name': 'District',
                'verbose_name_plural': 'Districts',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Doner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=10)),
                ('address_line_1', models.CharField(max_length=250)),
                ('address_line_2', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=6)),
                ('blood_group', models.CharField(max_length=6)),
                ('district', models.CharField(max_length=20)),
                ('center', models.CharField(max_length=20)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Doner',
                'verbose_name_plural': 'Doners',
                'ordering': ('first_name',),
            },
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.district')),
            ],
            options={
                'verbose_name': 'Center',
                'verbose_name_plural': 'Centers',
                'ordering': ('name',),
            },
        ),
    ]
