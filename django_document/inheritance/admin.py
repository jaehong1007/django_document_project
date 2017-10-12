from django.contrib import admin

from .models import Student, Teacher, School, Place, Restaurant, Champion, Supporter


class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'champion_type', 'rank',)
    list_editable = ('rank',)
    ordering = ('rank',)


admin.site.register(School)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Champion, ChampionAdmin)
admin.site.register(Supporter, ChampionAdmin)