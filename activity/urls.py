from django.urls import path, include

from activity.views import hi, RestTesView, StudentList, StudentDetail, StudentUpdate, StudentCreate, StudentDelete

urlpatterns = [
    path('', hi),
    path('rest/1', RestTesView.as_view()),
    path('students/list/', StudentList.as_view()),
    path('student/new/', StudentCreate.as_view()),
    path('student/<pk>/', StudentDetail.as_view()),
    path('student/update/<pk>/', StudentUpdate.as_view()),
    path('student/delete/<pk>/', StudentDelete.as_view()),
]
