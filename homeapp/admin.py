from django.contrib import admin
from .models import Empdata


class EmpAdmin(admin.ModelAdmin):
    list_display=('emp_id', 'working', 'jdate', 'ldate', 'dept', 'name', 'contact', 'add', 'state', 'idproof')
    #list_editable=('working', 'jdate', 'ldate', 'dept', 'name', 'contact', 'add', 'state', 'idproof')
    search_fields=('emp_id', 'working')
    list_filter=('jdate',)

# Register your models here.
admin.site.register(Empdata, EmpAdmin)

