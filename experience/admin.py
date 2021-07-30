from django.contrib import admin

from experience.models import ExperienceType, ExperienceItem, LineItem

class ExperienceItemInline(admin.TabularInline):
    model = ExperienceItem

class LineItemInline(admin.TabularInline):
    model = LineItem

class ExperienceAdmin(admin.ModelAdmin):
    inlines = [
        LineItemInline
    ]
    list_display = ["title", "time_period", "type", "order"]
    list_editable = ["order"]

class ExperienceTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)

admin.site.register(ExperienceType, ExperienceTypeAdmin)
admin.site.register(ExperienceItem, ExperienceAdmin)
