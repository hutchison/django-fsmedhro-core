from django.contrib import admin

from .models import (
    FachschaftUser,
    Gender,
    Studienabschnitt,
    Studiengang,
)


class StudiengangAdmin(admin.ModelAdmin):
    model = Studiengang
    # If you don't specify this, you will get a multiple select widget:
    filter_horizontal = ('studienabschnitt',)


admin.site.register(FachschaftUser)
admin.site.register(Gender)
admin.site.register(Studienabschnitt)
admin.site.register(Studiengang, StudiengangAdmin)
