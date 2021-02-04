from django.contrib import admin

# Register your models here.
from activity.models import Student


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name','student_email','student_phone_number']
    pass


admin.site.register(Student, ArticleAdmin)