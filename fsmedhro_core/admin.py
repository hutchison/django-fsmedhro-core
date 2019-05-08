from django.contrib import admin

from .models import (
    FachschaftUser,
    Gender,
    Studienabschnitt,
    Studiengang,
)


class FachschaftUserAdmin(admin.ModelAdmin):
    model = FachschaftUser
    fields = [
        'nickname',
        'user.first_name',
        'user.last_name',
        'gender',
        'studiengang',
        'studienabschnitt',
    ]


class GenderAdmin(admin.ModelAdmin):
    model = Gender
    fields = ['bezeichnung', 'endung']


class StudiengangAdmin(admin.ModelAdmin):
    model = Studiengang
    fields = ['bezeichnung']
    # If you don't specify this, you will get a multiple select widget:
    filter_horizontal = ('studienabschnitt',)


admin.site.register(FachschaftUser, FachschaftUserAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Studienabschnitt)
admin.site.register(Studiengang, StudiengangAdmin)
