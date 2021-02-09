from django.contrib import admin
from activity.models import Student


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name','student_email','student_phone_number']
    search_fields = ['student_name', 'student_email']
    pass


admin.site.register(Student, ArticleAdmin)


