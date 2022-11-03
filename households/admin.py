from django.contrib import admin
from .models import Household


@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "memo", "is_active")

    list_filter = ("is_active",)
