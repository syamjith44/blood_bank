from django.db import models
from django.contrib.auth.models import User


class District(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    wiki = models.URLField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'District'
        verbose_name_plural = 'Districts'

    def __str__(self):
        return self.name


class Center(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Center'
        verbose_name_plural = 'Centers'

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

    def __str__(self):
        return self.name


class BloodGroup(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'BloodGroups'
        verbose_name_plural = 'BloodGroups'

    def __str__(self):
        return self.name


class Doner(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10)
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=250)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    center = models.ForeignKey(Center, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Doner'
        verbose_name_plural = 'Doners'

    def __str__(self):
        return self.first_name

