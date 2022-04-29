from django.contrib import admin

from .models import Farm, Plantation, Plantation_Water_Routine, Water_Tank

@admin.register(Farm, Water_Tank,Plantation,Plantation_Water_Routine)
class DefaultAdmin(admin.ModelAdmin):
    pass
