from django.contrib import admin
from .models import UnderConstruction

@admin.register(UnderConstruction)
class UnderConstructionAdmin(admin.ModelAdmin):
    list_display = ['is_under_construction', 'uc_note', 'uc_duration']

    def has_add_permission(self, request):
        # prevent adding multiple rows
        return not UnderConstruction.objects.exists()
    
    def has_delete_permission(self, request):
        # Prevent deletion
        return False