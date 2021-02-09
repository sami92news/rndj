from django.contrib import admin
from custom_views.models import AnalyticsModel


class AnalyticsAdmin(admin.ModelAdmin):
    change_list_template = 'analytics_list.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)
        extra_context = {
            'new_attr': 6770,
        }
        response.context_data.update(extra_context)
        return response


admin.site.register(AnalyticsModel, AnalyticsAdmin)