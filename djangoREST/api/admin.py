from django.contrib import admin
from api.models import Company , Employee

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)

admin.site.register(Company , CompanyAdmin)
admin.site.register(Employee)
