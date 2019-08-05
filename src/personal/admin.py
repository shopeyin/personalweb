from django.contrib import admin
from personal.models import Contactus




class PersonalAdmin(admin.ModelAdmin):
    list_display                    = ('email','phonenumber', 'message','date_sent')
    search_fields                   = ('email',)
    readonly_fields                 = ('date_sent',)


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Contactus,PersonalAdmin)