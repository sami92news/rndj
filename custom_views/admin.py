from custom_views.models import AnalyticsModel
from django.contrib import admin

# Register your models here.


class AnalyticsAdmin(admin.ModelAdmin):
    change_list_template = 'analytics_list.html'

    def get_osm_info(self):
        pass

    def changelist_view(self, request, extra_context=None):

        response = super(AnalyticsAdmin, self).changelist_view(request, extra_context)
        extra_context = {
            'currencies_count': [],
        }
        response.context_data.update(extra_context)

        # response = TemplateResponse(request, self.change_list_template, context)

        return response


admin.site.register(AnalyticsModel, AnalyticsAdmin)