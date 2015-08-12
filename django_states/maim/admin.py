from django.contrib import admin

from maim.models import State, StateCapital, City

# Register your models here.

class StateAdmin(admin.ModelAdmin):
	list_display = ('name', 'abbreviation')

admin.site.register(State, StateAdmin)
admin.site.register(StateCapital)
admin.site.register(City)

