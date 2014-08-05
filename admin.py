from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from leads.models import  TalkWithUs, VisitBuilding, BookBuilding, Register, TalkWithUsResource

class TalkWithUsAdmin(ImportExportModelAdmin):
    resrouce_class = TalkWithUsResource
    list_display = ('name', 'email', 'phone', 'consultor_name' ,'created_date')
    list_filter = ('origin_contact', 'custom_page')

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'city', 'created_date')


admin.site.register(TalkWithUs, TalkWithUsAdmin)
admin.site.register(Register, RegisterAdmin)
