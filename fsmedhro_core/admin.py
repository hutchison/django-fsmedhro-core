from django.contrib import admin

from .models import (
    FachschaftUser,
    Gender,
    Studienabschnitt,
    Studiengang,
)


@admin.register(FachschaftUser)
class FachschaftUserAdmin(admin.ModelAdmin):
    model = FachschaftUser
    fields = [
        'nickname',
        'user',
        'gender',
        'studiengang',
        'studienabschnitt',
    ]
    list_display = (
        'nickname',
        '__str__',
        'gender',
        'studiengang',
        'studienabschnitt',
    )
    search_fields = [
        'nickname',
        'user__first_name',
        'user__last_name',
    ]
    list_filter = (
        'gender',
        'studiengang',
        'studienabschnitt',
    )


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    model = Gender
    fields = ['bezeichnung', 'endung']


@admin.register(Studiengang)
class StudiengangAdmin(admin.ModelAdmin):
    model = Studiengang
    fields = ['bezeichnung']
    # If you don't specify this, you will get a multiple select widget:
    filter_horizontal = ('studienabschnitt',)

admin.site.register(Studienabschnitt)
