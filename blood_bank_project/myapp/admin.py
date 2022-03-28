from django.contrib import admin
from .models import District, Center, Gender, BloodGroup, Doner


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}


class CenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'district', ]
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(District, DistrictAdmin)
admin.site.register(Center, CenterAdmin)
admin.site.register(Gender)
admin.site.register(BloodGroup)
admin.site.register(Doner)