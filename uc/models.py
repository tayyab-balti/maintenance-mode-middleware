from django.db import models

class UnderConstruction(models.Model):
    is_under_construction = models.BooleanField(default=False)
    uc_note = models.CharField(max_length=255, null=True, blank=True, help_text="Note to show on maintenance page")
    uc_duration = models.CharField(max_length=100, null=True, blank=True, help_text="e.g., '2 hours', 'until 5 PM'")

    def __str__(self):
        return "Maintenance Mode (ON)" if self.is_under_construction else "Site Live"
